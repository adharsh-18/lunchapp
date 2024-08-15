import streamlit as st
import pandas as pd
import numpy as np
from streamlit.components.v1 import html
import openpyxl

   


def main():
    st.title("SSN SNUC LUNCHAPP")
    xls = pd.ExcelFile("main.xlsx")
    data = pd.read_excel(xls,"data")
    # data.index = data["ID"]
    data = data[["ID","NAME","FOOD","COMMITTEE","STATUS"]]
    l = ["UNHRC","Arab League","NATO","NITI Aayog","IPC","Plenary"]
    comm = st.selectbox("Enter committee:",l)
    inp_key = st.text_input("Enter Delegate key :")
    sdata = data[data["ID"].str.contains(inp_key)]
    sdata = sdata[sdata["COMMITTEE"]==comm]
    st.write(sdata)
main()