
import numpy as np
import pickle
import streamlit as st
import pandas as pd
import seaborn as sns
from PIL import Image
from pages import report
import matplotlib.pyplot as plt

df = pd.read_csv("merge_data.csv")

loaded_model = pickle.load(open('model_re.sav', 'rb'))
img = Image.open('book.png')
st.set_page_config(page_title = 'Marks Predictor', page_icon = img)

hide_st_style = """
            <style>
           #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

st.set_option('deprecation.showPyplotGlobalUse', False)

# creating a function for Prediction


def marks_prediction(input_data):
    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    return round(prediction[0])

def greeting(val):
    if val <= 6:
     return "Weekly detention, You will have meeting with study counsellers"
    elif val <=12:
     return "You are doing average, you need to study hard"
    elif val <=16:
     return "You can do better with little hardwork"
    else:
     return "Keep up the good work"


def main():
    # giving a title
    st.title('Marks Prediction Web App')

    # getting the input data from the user

    age  = st.text_input('Age')
    address    = st.selectbox('Residance', ["","Urban","Rural"])
    Medu = st.text_input("Mother's Education")
    Mjob = st.selectbox("Mother's Job", ["","Teacher", "Health care","Civil services", "Homeworker", "Other"])
    Fedu = st.text_input("Father's Education")
    Fjob = st.selectbox("Father's Job", ["","Teacher", "Health care","Civil services", "Homeworker", "Other"])
    studytime = st.text_input('Amount of time studied')
    failures  = st.text_input('Past failures')
    higher    = st.selectbox('Wants to take higher education', ["","Yes","No"])

    # code for Prediction
    #diagnosis = ''




    # creating a button for Prediction
    if st.button('End Sem Result'):
        arr = np.zeros(15)
        arr[0] = int(age)
        if address == "Urban":
            arr[14] = 1
        
        arr[1] = int(Medu)
        arr[2] = int(Fedu)
        arr[3] = int(studytime)
        arr[4] = int(failures)

        if Mjob == "Teacher":
            arr[8] = 1
        elif Mjob == "Health care":
            arr[5] = 1
        elif Mjob == "Civil services":
            arr[7] = 1
        elif Mjob == "Homeworker" or Mjob == "Other":
            arr[6] = 1

        if Fjob == "Teacher":
            arr[12] = 1
        elif Fjob == "Health care":
            arr[9] = 1
        elif Fjob == "Civil services":
            arr[11] = 1
        elif Fjob == "Homeworker" or Fjob == "Other":
            arr[10] = 1

        if higher == "Yes":
            arr[13] = 1
        diagnosis = marks_prediction(arr)
        st.title(f"Your predicted Marks {diagnosis}")
       
       # st.image(image, channels="BGR")
        st.subheader(f"{greeting(diagnosis)}.")
        






if __name__=='__main__':
    main()