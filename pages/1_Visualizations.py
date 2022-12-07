# Import Custom Module
import pathlib
from pathlib import Path
import sys
sys.path.append(str(pathlib.Path().absolute()).split("/src")[0] + "/src")
import streamlit as st
import pandas as pd
import base64
import plotly.express as px
from utils import load_css, load_logo
import numpy as np
from matplotlib import pyplot as plt


load_css("style.css")


###### Sidebar information ######
with st.sidebar:
    st.markdown(
        f"""
        <div class="center">
            Made in &#x1F1E6;&#x1F1F7; with &#x1F60D; by Carolina
        """,
        unsafe_allow_html=True
    )
    st.title("About")
    st.info(
            "🎈 **BETA:** This app is pushed through Github, please contact us for more details"
        )


###### Visualization Page ######

### We open the dataframe
st.markdown("# Data Overview")
df = pd.read_excel("saudi_jobs.xlsx") 
st.dataframe(df)

### PLOT 1: Saudi Job Data: What are the most common Job Titles in Saudi? ###

st.subheader("What are the most common Job Titles in Saudi?")

titles_list = ["HR", "IT support", "Data engineer", 'NFT', 'Crypto', 'Software engineer', 'Computer science', 'Data Analyst', 'Business Analyst', 'Assurance Sales', 'Translation', 'Web manager', 'Project manager', 'Real Estate', 'Field engineer',
    'Data scientist', 'Teacher Marketing', 'Data collect', 'Quality Assurance Engineer', 'Accounting', 'Receptionist', 'Waiter', 'Architect',
    'Finance', 'Procurement', 'Web developer', 'Big Data', 'Tutor','Supply chain',' Store keeper', 'Fashion consultant', 'Site engineer', 'Risk Linguist', 'Civil engineer', 'Consultant']

titles_dict = {}

for title in titles_list:
    title = title.lower()
    titles_dict[title] = 0

for title in df.title:
    title = title.lower()
    for x in titles_dict.keys():
        if(x in title):
            titles_dict[x] +=1

selected_titles_dict = {}

for x in titles_dict.keys():
    if(titles_dict[x] >=10):
        selected_titles_dict[x] = titles_dict[x]

### BAR PLOT: matplotlib 

#fig1, ax1 = plt.subplots(figsize = (25, 10))
#x = list(selected_titles_dict.keys())
#y = list(selected_titles_dict.values())
#y = [z*3 for z in y]
#ax1.bar(x, y , width=0.4)
#st.pyplot(fig1, use_container_width=True)


### BAR PLOT: plotly 
plot_title = "What are the most common Job Titles in Saudi?"
df_plot = pd.DataFrame({'job': selected_titles_dict.keys(), 'counts': selected_titles_dict.values()}) # Series to dataframe so we can add the percentage
fig = px.bar(x=selected_titles_dict.keys(), y= selected_titles_dict.values(), title = str(plot_title),width=800, height=400)
st.plotly_chart(fig, use_container_width=True)


### PIE PLOT: plotly 
fig = px.pie(df_plot, values='counts', names='job', title = str(plot_title),width=800, height=400)
st.plotly_chart(fig, use_container_width=True)


#### Plot 2: What are the most Needed Skills? ####
st.subheader("What are the most Needed Skills?")

skills_list = ['Quality Management System', 'QMS' ,'Analytical skills', 'Technical skills', 'Vaccination', 'Internal audit', 'Verbal skills', 'MS Office tools', 'MS-Project', 'Word',
 'Excel', 'PowerPoint', 'Visio', 'Creative', 'Energetic', 'Self-motivated', 'English', 'Arabic', 'Organized', 'BS in engineering', 
 'Engineering', 'Machine Learning', 'ML', 'project documentation', 'test artifacts creation', 'Jira', 'Testrails', 'Communication', 'Stress-resistant',
  'software testing', 'python', 'software engineering', 'coding', 'SQL', 'OAuth', 'SAML', 'SSO', 'speech recognition technology', 'Computer Science',
   'JAVA', 'software development', 'programming skills', 'blockchain',  'Microsoft Windows', 'Microsoft', 'Windows Live ID', 'research skills',  'analytical', 'comprehension',
'HR', 'decision making', 'IT support', 'customer serviceskills',  'Windows', 'network troubleshooting', 'HTML', 'JavaScript', 'troubleshooting skills', 'spark', 
'engineering degree', 'organizational skills', 'technical knowledge', 'computer', 'Artificial Intelligence',"ai"]

skills_dict = {}
for x in skills_list:
    x = x.lower()
    skills_dict[x] = 0

for desc in df.description:
    if(type(desc) == float):
        continue
    elif(type(desc) == str):
        desc = desc.lower()
        for x in skills_dict.keys():
            if(x in desc):
                skills_dict[x] +=1

# skills_dict

selected_skills_dict = {}

for x in skills_dict.keys():
    if(skills_dict[x] >=200):
        selected_skills_dict[x] = skills_dict[x]

#selected_skills_dict


### BAR PLOT: matplotlib 
fig1, ax1 = plt.subplots(figsize = (25, 10))

x = list(selected_skills_dict.keys())
y = list(selected_skills_dict.values())
y = [z*3 for z in y]
ax1.bar(x, y , width=0.4)


### BAR PLOT: plotly 
plot_title = "What are the most Needed Skills?"
df_plot = pd.DataFrame({'skill': selected_skills_dict.keys(), 'counts': selected_skills_dict.values()}) # Series to dataframe so we can add the percentage
fig = px.bar(x=selected_skills_dict.keys(), y= selected_skills_dict.values(), title = str(plot_title),width=800, height=400)
st.plotly_chart(fig, use_container_width=True)


### PIE PLOT: plotly 
fig = px.pie(df_plot, values='counts', names='skill', title = str(plot_title),width=800, height=400)
st.plotly_chart(fig, use_container_width=True)
