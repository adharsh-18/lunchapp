import streamlit as st
import pandas as pd
import numpy as np
from streamlit.components.v1 import html
import openpyxl


def process(inp_key):
    xls = pd.ExcelFile("data.xlsx")
    data = pd.read_excel(xls,"data")
    data = data[["ID","COMMITTEE","NAME","FOOD","STATUS"]]
    data.index = data["ID"]
    flag = 0
    for i in list(data["ID"]):
        if inp_key==i:
            flag =1
            rdata = data[data["ID"]==inp_key]
            my_html = f"<h3>COMMITTEE : {rdata["COMMITTEE"][inp_key]}</h3><br><h3>NAME : {rdata["NAME"][inp_key]}</h3><br><h3>FOOD : {rdata["FOOD"][inp_key]}</h3>"
            st.header(f"COMMITTEE : {rdata["COMMITTEE"][inp_key]} ")
            st.header(f"NAME : {rdata["NAME"][inp_key]} ")
            st.header(f"FOOD : {rdata["FOOD"][inp_key]} ")
            if not(rdata["STATUS"][inp_key]=="done"):
                data.at[inp_key,"STATUS"] = "done"
                data.to_excel(xls,sheet_name="data")
                st.success("SUCCESS")
            else:
                st.warning("FOOD TAKEN")
            
    if flag==0:
        st.error("wrong code")

    


def main():
    st.title("SSN SNUC LUNCHAPP")
    xls = pd.ExcelFile("data.xlsx")
    data = pd.read_excel(xls,"data")
    data.index = data["ID"]
    data = data[["NAME","FOOD","STATUS"]]
    inp_key = st.text_input("Enter Delegate key :")
    if st.button("ENTER",type="primary"):
        process(inp_key)

if __name__=="__main__":
    main()