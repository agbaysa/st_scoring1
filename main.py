
# model_dtr_lean streamlit test
import streamlit as st
import pickle
import pandas as pd
import sklearn
from sklearn.tree import DecisionTreeClassifier
import time


model_dtc_lean = pickle.load(open('model_dtc_lean.pkl', 'rb'))

st.image('finance1.jpg')
st.header('Loan Application Scoring')

with st.form('my_form'):
    st.write('Please encode the details of the Loan Application:')

    prin = st.number_input('Enter Principal Amount of the Loan (e.g. 32000):', key='ni_prin')
    int = st.number_input('Enter Total Interest Amount of the Loan (e.g. .4500):', key='ni_int')
    loan = st.number_input('Enter Total Loan Amount of the Loan (e.g. 36000):', key='ni_loan')
    term = st.number_input('Enter Term Days of the Loan (e.g. 250):', key='ni_term')
    mo_amort = st.number_input('Enter Monthly Amortization Amount of the Loan (e.g. 6500):', key='ni_mo_amort')
    gmi = st.number_input('Enter Gross Monthly Income of Borrower (e.g. 50000):', key='ni_gmi')
    emp_tenure = st.number_input('Enter Employment Tenure of Borrower in Years (e.g. 3):', key='ni_emp_tenure')
    age = st.number_input('Enter Age of Borrower in Years (e.g. 55):', key='ni_age')
    
    if mo_amort ==0 or gmi == 0:
        pass
    else:
        debt_repayment = mo_amort/gmi
        
    no_dependents = st.number_input('Enter Number of Dependents of Borrower (e.g. 2):', key='ni_no_dependents')
    credit_score = st.number_input('Enter Borrower Credit Score (e.g. 0 for A, 1 for B, and 2 for C):', key='ni_credit_score')


    submitted = st.form_submit_button('Get Application Rating')
    st.write('')


if submitted:

    progress = st.progress(0)
    my_status = 'Running calculations...'
    st.write(my_status)

    for i in range(100):
        time.sleep(0.01)
        progress.progress(i + 1)

    if prin==0 or int==0 or loan==0 or term==0 or mo_amort==0 or gmi==0 or age==0 or debt_repayment==0 or int > 1 or credit_score > 2:
        st.warning('Please complete the details to compute the Loan Scoring or check the details if correct')
    else:

        df = pd.DataFrame(
            {'principal__amount': [prin],
             'interest_rate': [int],
             'total_loan_amount': [loan],
             'term_days': [term],
             'monthly_amortization': [mo_amort],
             'gross_monthly_income': [gmi],
             'employment_tenure': [emp_tenure],
             'age': [age],
             'debt_repayment': [debt_repayment],
             'no._of_dependents': [no_dependents],
             'credit_score': [credit_score]
            }
        )

        st.write('')
        st.write('The following were the details provided:')
        st.dataframe(df)

        predict = model_dtc_lean.predict(df)

        st.write('')
        st.write('')
        st.write('Loan Application Decision:')
        st.write('')
        if predict == 0:
            st.success('The Loan Application is good. Please proceed with the booking of the loan.')
            st.balloons()
            st.warning('Please encode new details above if doing another loan scoring evaluation and click Get Application Rating button')

        else:
            st.warning('Please review the Loan Application further as.')
            st.warning('Please encode new details above if doing another loan scoring evaluation and click Get Application Rating button')



