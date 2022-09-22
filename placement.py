import pickle
import streamlit as st
from PIL import Image

# loading the model
pickle_in = open('placement_predictor.pkl', 'rb')
classifier = pickle.load(pickle_in)

# defining the function which willl make the predictin using the data which the user input


def prediction(ssc_p, hsc_p, degree_p, workex, etest_p,
               specialisation, mba_p, gender, ssc_b, degree_t):

    if(workex == 'Yes'):
        workex = 1
    else:
        workex = 0
    if(specialisation == 'Marketing and Finance'):
        specialisation = 0
    else:
        specialisation = 1
    if(gender == 'Male'):
        gender = 1
    else:
        gender = 0
    if(ssc_b == 'Central'):
        ssc_b = 0
    else:
        ssc_b = 1
    if(degree_t == 'Science and Technology'):
        degree_t = 2
    elif(degree_t == 'Commerce and Management'):
        degree_t = 0
    else:
        degree_t == 1

    prediction = classifier.predict([[ssc_p, hsc_p, degree_p, workex, etest_p,
                                      specialisation, mba_p, gender, ssc_b, degree_t]])

    if(prediction == 1):
        return "Student Placed, congratulations!!!!!!"
    else:
        return "Sorry student not placed, better Luck next time"


def main():
    theme = []

    st.set_page_config(layout="wide")
    # img=Image.open('ymaAeU.jpg')
    # st.image(img,use_column_width=True)
    # front end elements of the web page
    html_temp = """ 
    <div style ="background-color:purple;padding:13px"> 
    <h1 style ="color:white;text-align:center;">Streamlit Placement Prediction ML App</h1> 
    </div> 
    """
    st.markdown(html_temp, unsafe_allow_html=True)
    ssc_p = st.number_input("Enter your SSC percentage")
    hsc_p = st.number_input("Enter your HSC percentage")
    degree_p = st.number_input("Enter your Degree percentage")
    workex = st.selectbox("Have any work experience",
                          ("Yes", "No"))  # no-0 and yes-1
    etest_p = st.number_input("Enter your Etest percentage")
    specialisation = st.selectbox("Enter the specilisation you have", (
        "Marketing and Finance", 'Marketing and HR'))  # hr-1 and finance-0
    mba_p = st.number_input("Enter your MBA percentage")
    gender = st.selectbox("Gender", ("Male", "Female"))  # male-1 and female-0
    # others-1 and central-0
    ssc_b = st.selectbox("Enter your SSC board", ("Central", "Others"))
    degree_t = st.selectbox("Enter you Degree type", ("Science and Technology",
                                                      "Commerce and Management", "Others"))  # sci-2,com-0,others-1
    result = ''

    if st.button("Predict Placement"):
        result = prediction(ssc_p, hsc_p, degree_p, workex, etest_p,
                            specialisation, mba_p, gender, ssc_b, degree_t)
        st.success('Result based on data you provided: {}'.format(result))


if __name__ == "__main__":
    main()
