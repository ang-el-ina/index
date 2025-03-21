import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import numpy as np
import matplotlib as plt


#--CONFIGS--
DATA_URL= r"C:\Users\angel\OneDrive - Kerry Education and Training Board (1)\2024-2025\Computer Science\265969_LCCS_Project_2025\Report\Resources\new_data.csv"


#---PAGE SETUP---
st.set_page_config(
    page_title="Index.py",
    page_icon="📊",
    )

st.title("LC Computer Science Project 2025")
st.write("Exam no: 265969")

# Navigation bar
with st.sidebar:
    selected = option_menu(
        menu_title = "Main menu",
        options=["Home", "Brief", "Investigation", "Plan & Design", "Creation", "Evaluation", "Reference & Word Count"],
        icons=["house-door-fill", "journal-bookmark", "search-heart", "pencil-square", "pc-display-horizontal", "list-check", "stickies-fill"],
        menu_icon="cast",
        default_index=0,   
    )
    
if selected =="Home":
    st.title(f"You have selected {selected}")
if selected =="Brief":
    st.title(f"You have selected {selected}")   
if selected =="Investigation":
    st.title(f"You have selected {selected}")
if selected =="Plan & Design":
    st.title(f"You have selected {selected}")
if selected =="Creation":
    st.title(f"You have selected {selected}")
if selected =="Evaluation":
    st.title(f"You have selected {selected}")
if selected =="Reference & Word Count":
    st.title(f"You have selected {selected}")
    
#LOAD DATA
data = pd.read_csv(DATA_URL)
st.dataframe(data)

#Drop first column
new_data = df = data.iloc[:, 1:]

st.title("The Gender Pay Gap")
#chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])

st.bar_chart(new_data)

st.line_chart(new_data)

st.scatter_chart(new_data)

#Brief
st.title("Meeting The Brief")
st.write("Exam no: 265969")

tab1, tab2 = st.tabs(["Context", "Requirements"])

with tab1:
    st.header("Context on the Brief")
    st.subheader("Data is the new oil. Like oil, data is valuable but if unrefined, it cannot really be used. :red[-clive Humby]")
    st.write("During my research on the brief, I visited different databases, most of which holds public data. I came across interactive datasets where you could click on a map and you would get the data of that specific country. I also discovered that databases had missing data and/ or ireliable data.")
    st.subheader("The data I chose to do my project on:")
    st.write("I chose to my project on the gender pay gap in different countries. I actually found the website on the project coursework brief. After downloading the csv file, I read, cleaned and extracted the data to make this project.")
    
with tab2:
    st.header("Requirements of the Brief")
    st.subheader("1)Collect and Prepare Data", divider=True)
    st.image(r"C:\Users\angel\OneDrive\Pictures\Screenshots 1\Screenshot 2025-03-20 191834.png")
    st.write("I selected the pay gap csv file off this website. I imported the csv file into microsoft Excel where I cleaned the data before changing the format back to csv. I also experimented with jupyter Notebook.")
    st.subheader("2)Data analytics and visualisation", divider=True)
    st.write("Using visual studio code, python, streamlit, matplotlib, numpy, anaconda and pandas, I was able to create different analytics and visuals such as bar chart, line graph, scatter chart and table.")
    st.subheader("Create a basic interactive information system interface", divider=True)
    st.write("The information system is interactive as the user can zoom in, out, view in full, etc.")

    
    
    #Investigation
st.title("My Investigation")
st.write("Exam no: 265969")

tab1, tab2= st.tabs(["Research", "References"])

with tab1:
    st.header("Research conducted")
    st.subheader("The websites I used are referenced in the second tab.")
    st.write("I pulled my data from a government based database so I know it is reliable and can be trusted. The raw csv folder can be found in recources folder. It had missing data and out of range that I manually cleaned when I went through it. I visited most websites that were included on the brief and that's when I came across crime datasets which were in a way, my :blue[Inspiration] for my project.")
    st.subheader("Data Background:", divider= True)
    st.write("The research was conducted by an organisation that collected data on the countries in the EU over a number of years. In most cases, there is a noticable decrease in the pay gap from the starting year :green[2017] to the end year of :green[2022]. Specifically for Ireland there was a gradual decrease from :green[14 Euros] to :green[9 Euros]. ")
    
with tab2:
    st.page_link("https://european-union.europa.eu/principles-countries-history/eu-countries_en", label= "Data Gov")
    st.subheader("I used this website to find my main database, it was cited on the brief also.")
    st.page_link("https://eige.europa.eu/gender-equality-index/2021/domain/money/EL", label="Gender Equality Index")
    st.write("I used the website cited above as an attempt to fill in the missing data on the csv file but there were a few countries that had absolutely no data on the gender pay gap.", divider=True)
    st.write("Other Resources:")
    st.page_link("https://www.w3schools.com/", label="W3 Schools")
    st.page_link("https://docs.streamlit.io/", label="Streamlit Documentation")
    st.page_link("https://icons.getbootstrap.com/", label="Bootsraps Icons")
    st.page_link("https://code.visualstudio.com/", label="Visual Studio Code")
    st.page_link("https://github.com/", label="Github")
   
   
   
st.title("Plan and Design")
st.write("Exam no: 265969")

st.header("Wireframe Diagram")
st.image(r"C:\Users\angel\OneDrive\Pictures\Screenshots 1\Screenshot 2025-03-21 004133.png")


st.title("The Creation")
st.write("Exam no: 265969")

tab1, tab2, tab3, tab4, tab5 = st.tabs(["Week 1", "Week 2", "Week 3", "Week 4", "Week 5"])

with tab1:
    st.write("I visited a few websites and I might do my project on screentime/ phone usage in ireland.")
    st.write("I can't find sufficient data for my project on screentime.")
    st.write("I've downloaded the data on gender pay gap as a csv file.")

with tab2:
    st.write("Data was cleaned in excel microsoft.")
    st.write("File was converted back into csv file.")
    st.write("I made a wireframe diagram")
    st.write("Used Thonny to test out algorithms that I can implement on my final project.")
    
with tab3:
    st.write("Made the index. file and started programming the page using HTML and CSS")
    st.image(r"C:\Users\angel\OneDrive\Pictures\Screenshots 1\Screenshot 2025-03-21 010700.png")
    st.image(r"C:\Users\angel\OneDrive\Pictures\Screenshots 1\Screenshot 2025-03-21 010723.png")
    st.write("I didn't want to use css and I found Streamlit")
    st.write("I decided to use streamlit and write the project, completely in Python.")
    st.write("Ran Pycharm to try launch streamlit website.")
    st.write("Tried to run it on kali linux on vmWare player but unfortunately, I found it quite slow")
    st.image(r"C:\Users\angel\OneDrive\Pictures\Screenshots 1\Screenshot 2025-03-21 011507.png")
    
with tab4:
    st.write("Anaconda, Visual studio code and github made it easy to properly launch streamlit.")
    st.write("used jupyter notebook to extract and manipulate data")
    st.image(r"C:\Users\angel\OneDrive\Pictures\Screenshots 1\Screenshot 2025-03-21 012259.png")
    st.write("Used matplotlib. pypi etc to create visuals for data.")
    st.write("created the other sections on the project")

with tab5:
    st.write("Recorded video of final project.")
    
st.video(r"C:\Users\angel\OneDrive\Videos\Screen Recordings\Screen Recording 2025-03-21 014543.mp4", format="video, , start_time= 0")
    