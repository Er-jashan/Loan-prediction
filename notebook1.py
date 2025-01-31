import streamlit as st
from PIL import Image
import pickle
import os

# Load the model (Ensure the path is correct for your local environment)
model_path = os.path.join('main/Model.pkl', 'Model.pkl')
model = pickle.load(open(model_path, 'rb'))

def run():
    # Load and display the image (Ensure the path is correct for your local environment)
    img_path = os.path.join('main/bank.png', 'bank.png')
    img1 = Image.open(img_path)
    img1 = img1.resize((156, 145))
    st.image(img1, use_column_width=False)
    st.title("Bank Loan Prediction using Machine Learning")

    # Account No
    account_no = st.text_input('Account number')

    # Full Name
    fn = st.text_input('Full Name')

    # Gender
    gen_display = ('Female', 'Male')
    gen_options = list(range(len(gen_display)))
    gen = st.selectbox("Gender", gen_options, format_func=lambda x: gen_display[x])

    # Marital Status
    mar_display = ('No', 'Yes')
    mar_options = list(range(len(mar_display)))
    mar = st.selectbox("Marital Status", mar_options, format_func=lambda x: mar_display[x])

    # No of dependents
    dep_display = ('No', 'One', 'Two', 'More than Two')
    dep_options = list(range(len(dep_display)))
    dep = st.selectbox("Dependents", dep_options, format_func=lambda x: dep_display[x])

    # Education
    edu_display = ('Not Graduate', 'Graduate')
    edu_options = list(range(len(edu_display)))
    edu = st.selectbox("Education", edu_options, format_func=lambda x: edu_display[x])

    # Employment Status
    emp_display = ('Job', 'Business')
    emp_options = list(range(len(emp_display)))
    emp = st.selectbox("Employment Status", emp_options, format_func=lambda x: emp_display[x])

    # Property Area
    prop_display = ('Rural', 'Semi-Urban', 'Urban')
    prop_options = list(range(len(prop_display)))
    prop = st.selectbox("Property Area", prop_options, format_func=lambda x: prop_display[x])

    # Credit Score
    cred_display = ('Between 300 to 500', 'Above 500')
    cred_options = list(range(len(cred_display)))
    cred = st.selectbox("Credit Score", cred_options, format_func=lambda x: cred_display[x])

    # Applicant Monthly Income
    mon_income = st.number_input("Applicant's Monthly Income($)", value=0)

    # Co-Applicant Monthly Income
    co_mon_income = st.number_input("Co-Applicant's Monthly Income($)", value=0)

    # Loan Amount
    loan_amt = st.number_input("Loan Amount", value=0)

    # Loan Duration
    dur_display = ['2 Month', '6 Month', '8 Month', '1 Year', '16 Month']
    dur_options = range(len(dur_display))
    dur = st.selectbox("Loan Duration", dur_options, format_func=lambda x: dur_display[x])

    if st.button("Submit"):
        duration = 0
        if dur == 0:
            duration = 60
        elif dur == 1:
            duration = 180
        elif dur == 2:
            duration = 240
        elif dur == 3:
            duration = 360
        elif dur == 4:
            duration = 480
        
        features = [[gen, mar, dep, edu, emp, mon_income, co_mon_income, loan_amt, duration, cred, prop]]
        prediction = model.predict(features)
        lc = [str(i) for i in prediction]
        ans = int("".join(lc))
        
        if ans == 0:
            st.error(
                "Hello: " + fn + " || "
                "Account number: " + account_no + ' || '
                'According to our Calculations, you will not get the loan from Bank'
            )
        else:
            st.success(
                "Hello: " + fn + " || "
                "Account number: " + account_no + ' || '
                'Congratulations!! you will get the loan from Bank'
            )

run()
