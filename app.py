import streamlit as st
import numpy as np
from num2words import num2words
import pickle
pipe=pickle.load(open('Ridge.pkl','rb'))
data=pickle.load(open('data.pkl','rb'))
st.title("House Price Predictor!!!")

loc=st.selectbox('Location',data['location'].unique())

bhk=st.selectbox('BHK',data['BHK'].unique())

bath=st.selectbox('Bath',data['bath'].unique())

sq_feet=st.number_input('Square_Feet')

if st.button('Predict Price'):
    inp=np.array([loc,bhk,bath,sq_feet])
    inp=inp.reshape(1,4)
    #price=int(np.exp(pipe.predict(inp)[0]))
    price=int(pipe.predict(inp)[0])
    price=price*100000
    st.title(price)
    st.title("The Predicted Price is:"+num2words(price))