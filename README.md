# Open-Jobs-Recommendation-System

Overview

The Job Recommendation System is a web application built with Streamlit, designed to help users find job openings based on various criteria such as experience, degree, skills, and location. The system provides an intuitive interface for users to filter and search for relevant job postings from a dataset.

Features

- User-Friendly Interface: The system offers an easy-to-use interface for setting 
  preferences and filtering job listings.

- Filtering Options: Users can specify their minimum and maximum years of experience, 
  degree, skills, and location to narrow down job search results.

- Dynamic Recommendations: The system dynamically updates job recommendations based on 
  the user's selected criteria.

Getting Started

To run the Job Recommendation System locally, follow these steps:

1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/MonicaRohit/Open-Jobs-Recommendation-System.git
   ```
2. Navigate to the project directory:
   ```bash
   cd Open-Jobs-Recommendation-System
   ```
3. Install the required dependencies using pip:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```
Usage
1. Minimum and Maximum Experience: Use the sliders in the sidebar to set your desired 
   minimum and maximum years of experience.

2. Degree: Choose your preferred degree from the dropdown list.

3. Skills: Select the skills you possess from the available options.

4. Location: Multiselect locations that you are interested in.

5. The system will automatically update the job recommendations based on your selected 
   criteria.

6. Scroll down to view the recommended job listings in a tabular format.

Customization
You can easily customize the application:

- Data: Replace the example dataset with your own job postings dataset. Make sure it has 
        the same structure.

- Design: Modify the HTML and CSS code in the Streamlit app to match your desired design 
          preferences.

- Styles: Change the styles, colors, and fonts in the Streamlit app to align with your 
          branding.

Dependencies
- Streamlit
- Pandas
- NumPy



