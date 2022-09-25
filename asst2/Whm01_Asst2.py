### Importing libraries
import pandas as pd
import numpy as np
import plotly 
import streamlit as st
import plotly.express as px
from  streamlit_option_menu import option_menu

#Set Streamlit Title
st.title('Enjoy my Streamlit Visualization of Assignment 1 PLots!')

#streamlit menu
selected = option_menu(
    menu_title="Main Menu",
    options=["Home", "Author Information"],
    icons=["house", "envelope"],
    menu_icon="cast",
    orientation="horizontal"
    #defualt_index=0
    
)
# author introduction
if selected== "Author Information":
    st.write("The author is Wissam Malaeb, a humble AUB graduate passionate about coding!        / id: 201801182       / Nationality: Lebanese")

# Importing dataset
df=pd.read_csv("ds_salaries.csv")


#Inspect the raw data if checked (check box)
if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(df.head())

#cleaning data: unused columns
df.drop(columns=['Unnamed: 0', 'salary', 'salary_currency'], axis=1, inplace=True)

# Salaries for the Full Timers Mid level data scientists according to the company location
mi_ds_data = df.loc[(df.job_title == 'Data Scientist')&(df.experience_level == "MI") & (df.employment_type == "FT")]

average_data_mid  = pd.DataFrame(mi_ds_data.groupby('company_location').mean()["salary_in_usd"]).reset_index()
# average_data_mid

## Plot 1: Barplot
# plot bar graph of salary in usd vs company location
st.header('This bar graph represents salaries in USD vs company location ')
fig1 = px.bar(average_data_mid, x="company_location", y='salary_in_usd')
st.plotly_chart(fig1)

import plotly.express as px

# Salaries for the Full Timers data scientists according to the company location and experience level

mi_ds_data = df.loc[(df.job_title == 'Data Scientist')& (df.employment_type == "FT")]
average_data  = pd.DataFrame(mi_ds_data.groupby(['experience_level',"company_location"]).mean())
average_data = average_data.reset_index()

#3d scatter plotting

st.header('This 3d scatter plot represents salaries in USD vs company location and experience level')
fig2 = px.scatter_3d(average_data, x='company_location', y='salary_in_usd', z='experience_level')
# fig2.update_layout(height=800, width=2400)
st.plotly_chart(fig2)

## Plot 3: Interactive Barplot
#Interactive barplot of salary in usd vs company location for different experience levels
st.header('This Interactive barplot represents salaries in USD for different experience levels')
fig3 = px.scatter(average_data, x="company_location", y="salary_in_usd", animation_frame="experience_level")
st.plotly_chart(fig3)

## Plot 4: Interactive World Map
# adjusting 2 letter to 3 letter country names so the map can read them
average_data_mid.loc[average_data_mid.company_location == "AU", "company_location"] = "AUS"
average_data_mid.loc[average_data_mid.company_location == "CA", "company_location"] = "CAN"
average_data_mid.loc[average_data_mid.company_location == "DE", "company_location"] = "GER"
average_data_mid.loc[average_data_mid.company_location == "FR", "company_location"] = "FRA"
average_data_mid.loc[average_data_mid.company_location == "IN", "company_location"] = "IND"
average_data_mid.loc[average_data_mid.company_location == "MY", "company_location"] = "MYS"
average_data_mid.loc[average_data_mid.company_location == "US", "company_location"] = "USA"
average_data_mid.loc[average_data_mid.company_location == "VN", "company_location"] = "VNM"
average_data_mid.loc[average_data_mid.company_location == "AT", "company_location"] = "AUT"
average_data_mid.loc[average_data_mid.company_location == "BR", "company_location"] = "BRA"
average_data_mid.loc[average_data_mid.company_location == "CH", "company_location"] = "CHE"
average_data_mid.loc[average_data_mid.company_location == "CL", "company_location"] = "CHL"
average_data_mid.loc[average_data_mid.company_location == "ES", "company_location"] = "ESP"
average_data_mid.loc[average_data_mid.company_location == "GB", "company_location"] = "GBR"
average_data_mid.loc[average_data_mid.company_location == "HU", "company_location"] = "HUN"
average_data_mid.loc[average_data_mid.company_location == "IL", "company_location"] = "ISR"
average_data_mid.loc[average_data_mid.company_location == "LU", "company_location"] = "LUX"
average_data_mid.loc[average_data_mid.company_location == "MX", "company_location"] = "MEX"
average_data_mid.loc[average_data_mid.company_location == "NG", "company_location"] = "NGA"
average_data_mid.loc[average_data_mid.company_location == "PL", "company_location"] = "POL"

#plotting interactive world map of company locations with bubble size representing salaries 
st.header('This Interactive world map represents salaries in USD by varying bubble sizes in different company locations')
interactive_map = px.scatter_geo(average_data_mid, locations="company_location", hover_name ="company_location", color="company_location", size="salary_in_usd",
                     projection="natural earth")
st.plotly_chart(interactive_map)

## Plot 5: Colored Barplot
# bar plotting of salart in usd vs experience level in different companies portrayed in different colors
st.header('This bar plot represents salaries in USD vs experience level in different companies portrayed in different colors')
fig4 = px.bar(average_data, x="experience_level", y="salary_in_usd", color="company_location")
st.plotly_chart(fig4)

    