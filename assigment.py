import streamlit as st
st.set_page_config(page_title="assigment task",layout='wide')
st.title('assinment task')
if "history" not in st.session_state:
    st.session_state.history = []
left , right = st.columns(2)
with left:
    name=st.text_input("ENTER YOUR NAME ")
    age=st.slider('age',min_value=10,max_value=30,value=18)
    weight=st.slider('weight',min_value=100,max_value=220,step=10)
    height = st.number_input("Height", min_value=100.0, max_value=220.0)
    Activity_level=st.selectbox("what's your activty leve?",['Sedentary','Light','Moderate','Active'])
    smoke=st.radio("are you smoking",['yes','no'])
    medical_condition=st.radio("do you have any medical condition",['yes','no'])
    water_intake=st.slider("water intake",min_value=0,max_value=4000)
    date_of_birth=st.date_input("Enter your date of birth")



def bmi_cal (weight,height):
    bmi_cal=weight/((height/100)**2)
def calculate_calories(weight, height, age, activity_level, smoke):
    
    bmr = 10 * weight + 6.25 * height - 5 * age + 5