import streamlit as st
import joblib
#Data
import numpy as np
import pandas as pd
from sklearn.preprocessing import OneHotEncoder
#Model
from sklearn.metrics import classification_report, accuracy_score, make_scorer, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import cross_val_predict
from sklearn.metrics import accuracy_score
from sklearn.svm import SVC

#On Web
st.title('การทำนายระดับผลการเรียน')
st.markdown('กรุณากรอกข้อมูลให้ครบเพื่อใช้ในการทำนาย')
st.image('img.png',caption='ขั้นตอนการกรอกผลการเรียนแต่ละวิชาชั้นปีที่ 1')
st.header('ผลการเรียนแต่ละรายวิชาชั้นปีที่ 1 ')
col1, col2 = st.columns(2)
with col1:
  st.text('สาขา')
  major1 = st.selectbox("สาขาที่เรียน",('คณิตศาสตร์','สถิติ','ฟิสิกส์','ฟิสิกส์ประยุกต์','เคมี','ชีววิทยา','วิทยาการคอมพิวเตอร์','เทคโนโลยีสารสนเทศ'))
with col2:
  st.text('เกรดแต่ละรายวิชาชั้นปีที่ 1')
  grade1 = st.text_input('copy ผลการเรียนชั้นปีที่ 1')
re = st.button('Predict class of grade')

#predict
def predict(data):
  model_rf = joblib.load('rf_model.sav')
  return model_rf.predict(data)
