# Import necessary libraries
import pandas as pd
import numpy as np
import streamlit as st

# Suppress warnings
st.set_option('deprecation.showPyplotGlobalUse', False)

# Import the dataset
data = pd.read_csv('naukri.csv')

# Remove unnecessary columns
drop = ['jobdescription', 'jobid', 'site_name', 'uniq_id', 'jobtitle', 'postdate']
data = data.drop(columns=drop)

# Cleaning and Analysing Column Experience
data.experience.fillna("2 - 7 yrs", inplace=True)
year_experience = data.experience.str.split(' ')
data['min_year_exp'] = year_experience.apply(lambda x: x[0])
data['max_year_exp'] = year_experience.apply(lambda x: x[2] if len(x) > 2 else x[0])
data['min_year_exp'] = np.where(data.min_year_exp == 'Not', '2', data.min_year_exp)
data['max_year_exp'] = np.where(data.max_year_exp == 'Not', '7', data.max_year_exp)
data['max_year_exp'] = np.where(data.max_year_exp == '-1', '1', data.max_year_exp)
data['min_year_exp'] = data['min_year_exp'].astype(int)
data['max_year_exp'] = data['max_year_exp'].astype(int)

# Cleaning and Analysing Column Education
data.education.fillna('UG: Any Graduate - Any Specialization', inplace=True)
data_edu = data.education.apply(lambda x: x.replace(" PG:", "|")).apply(lambda x: x.replace(" Doctorate:", "|"))
data_edu = data_edu.apply(lambda x: x.split("|"))
data_edu = data_edu.apply(lambda x: x[0])
data_edu = data_edu.apply(lambda x: x.replace("UG: Any Graduate - Any Specialization", "UG: Any Graduate"))
data_edu = data_edu.apply(lambda x: x.replace("UG: Any Graduate - Any Specialization, Graduation Not Required", "UG: Any Graduate"))
data_edu = data_edu.apply(lambda x: x.replace("UG: Any Graduate, Graduation Not Required", "UG: Any Graduate"))
data_edu = data_edu.apply(lambda x: x.replace("B.Tech/B.E. - Any Specialization", "UG: B.Tech/B.E."))
data_edu = data_edu.apply(lambda x: x.replace("UG: UG: B.Tech/B.E.", "UG: B.Tech/B.E."))
data_edu = data_edu.apply(lambda x: x.replace("UG: Graduation Not Required", "UG: Any Graduate"))
data_edu = data_edu.apply(lambda x: x.replace("UG: Any Graduate, UG: B.Tech/B.E.", "UG: B.Tech/B.E."))
data_edu = data_edu.apply(lambda x: x.replace("UG: B.Tech/B.E., Computers", "UG: B.Tech/B.E. - Computers"))
data_edu = data_edu.apply(lambda x: x.replace("UG: B.Tech/B.E., Computers", "UG: B.Tech/B.E. - Computers"))
data_edu = data_edu.apply(lambda x: x.replace("UG: B.Com - Commerce", "UG: B.Com"))
data_edu = data_edu.apply(lambda x: x.replace("UG: ", ""))
data["degree"] = data_edu

# Cleaning and Analysing Column Industry
data.industry.fillna(data.industry.mode()[0], inplace=True)

# Cleaning and Analysing Column Job Address
data.joblocation_address.fillna('Not Mentioned', inplace=True)
data['loc'] = data.joblocation_address
data['loc'] = data['loc'].apply(lambda x: [location.strip() for location in x.split(",")])  # Convert to a list of locations

# Define the Streamlit app
# Use HTML to improve typography
st.markdown("<h1 style='color: #ff5733; text-align: center;'>Open Jobs Recommendation System</h1>", unsafe_allow_html=True)

# Add a custom background color
st.markdown(
    """
    <style>
    body {
        background-color: #f3f3f3;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Customize the sidebar
st.sidebar.markdown(
    """
    <style>
    .sidebar .sidebar-content {
        background-color: #2c3e50;
        color: #ecf0f1;
        font-weight: bold;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.sidebar.header("Job Recommendation")

min_exp = st.sidebar.slider("Minimum Experience", 0, 25, 0)
max_exp = st.sidebar.slider("Maximum Experience", 0, 27, 0)
degree = st.sidebar.selectbox("Select Degree", data.degree.unique())
skills = st.sidebar.selectbox("Select Skills", data.skills.unique())

# Get unique locations and drop duplicates
loc_options = data['loc'].explode().unique()
selected_loc = st.sidebar.multiselect("Select Location", loc_options)

# Create a boolean mask for the selected locations
loc_mask = data['loc'].apply(lambda x: any(l in selected_loc for l in x))

# Improve data presentation with custom CSS for tables
st.markdown(
    """
    <style>
    table.dataframe {
        border: 2px solid #333;
        border-radius: 5px;
        margin: 1em 0;
    }
    table.dataframe th {
        background-color: #3498db;
        color: white;
    }
    table.dataframe tr:nth-child(even) {
        background-color: #f2f2f2;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Display your data table
filtered_data = data[
    (data["min_year_exp"] >= min_exp) & (data["max_year_exp"] <= max_exp) &
    (data["degree"] == degree) & (data["skills"] == skills)
][['company', 'loc', 'industry', 'degree', 'experience', 'skills', 'numberofpositions', 'payrate']]

st.write("Recommended Jobs:")
st.dataframe(filtered_data)

# Filter the data using the mask
#filtered_data = data[
    #(data["min_year_exp"] >= min_exp) &
    #(data["max_year_exp"] <= max_exp) &
    #(data["degree"] == degree) &
    #(data["skills"] == skills) &
    #loc_mask
#][['company', 'loc', 'industry', 'degree', 'experience', 'skills', 'numberofpositions', 'payrate']]

#st.write("Recommended Jobs:")
#st.dataframe(filtered_data)




