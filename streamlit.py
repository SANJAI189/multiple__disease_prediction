# -*- coding: utf-8 -*-
"""
Created on Fri Sep 29 18:42:02 2023

@author: sanja
"""

import streamlit as st

st.write("hello")

st.success("success")

st.warning("error")

#Get Help info ABout python
st.help(range)


st.exception("name_error('number 3 not defined')")

#images
from PIL import Image
img = Image.open("C:/Users/sanja/OneDrive/Pictures/Screenshots/Screenshot 2023-07-06 231328.png")
st.image(img,width=300,caption = "Dream house")


#Videos
#vid_file = open("B:\AUSTRALIA VLOGS\Australia ல ஒரு ஊட்டி இருக்கு _ A day in Blue Mountains _ Sydney _ Australia _ Way2go தமிழ்(720P_HD).mp4","rb").read()
#st.video(vid_file)

# checkbox

if st.checkbox("Show/Hide"):
    st.text("Showing or Hiding widget")
    
    
status = st.radio("What is your status",('Active','Inactive'))
    
if status == 'Active':
      st.success('You are active')
else:
    st.warning("Inactive,activate")      
  
#Occupation

occupation = st.selectbox("Your Occupation",["DATA SCIENTIST","DATA ANALYST","DATA ENGINEER"])    
if (occupation != 0):
    st.write("you selected ",occupation)    
    

#Multiselect

location = st.multiselect("Where do you work",
                          ('PERTH','ADELAIDE','SYDNEY',
                           'MELBOURNE',
                           'AUCKLAND',
                           'WELLINGTON'))



st.write("You selected",len(location),'locations')

#slider
level = st.slider("what is your level",1,5)

#Button
st.button("Submit")

if st.button("About"):
    st.text("Chasing Dreams")
    
#Text input
first_name = st.text_input("Enter your first name","Type here..")    
if st.button("submit"):
    result = first_name.title()
    st.success(result)

#Text Area
message = st.text_input("Enter the message","Type here..")    
if st.button("click"):
    result = message.title()
    st.success(result)

#Date Input
import datetime
date = st.date_input("Today is",datetime.datetime.now())


#Time
time = st.time_input("Time is",datetime.time())

#json
st.text('Display json')
st.json({'Name':"Sanjai",
         'Age':"19"})

#raw code
st.text("Displaying code")
st.code("import pandas as pd\nimport numpy as np")
        

#another method
with st.echo():
    #this will display comment also
    import streamlit as st
    import pandas as pd

#Progress
my_bar = st.progress(0)
for i in range(100):
    my_bar.progress(i+1)

#spinner
import time
with st.spinner("Waiting..."):
    time.sleep(5)
    st.success('Finished')

st.balloons()


st.sidebar.header('About')
st.sidebar.text("this is my page")


    
    
    
    
    