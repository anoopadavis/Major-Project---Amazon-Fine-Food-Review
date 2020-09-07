# -*- coding: utf-8 -*-
"""app.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1yVYn97VJIW6b_h5d9Lc-riVXarbH_NKv
"""

import streamlit as st
from PIL import Image
from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score,confusion_matrix,classification_report
df=pd.read_csv('https://media.githubusercontent.com/media/anoopadavis/Major-Project---Amazon-Fine-Food-Review/master/RDS.csv')
df.drop(['Id','ProductId','UserId','ProfileName','Time','Text','HelpfulnessNumerator','HelpfulnessDenominator'],axis=1,inplace=True)
df.dropna(axis=0,inplace=True)
df['Sentiment']=df['Score'].apply(lambda Score: 'Positive' if Score>3 else('Negative' if Score<3 else "Neutral"))
index=df[df['Sentiment']==0].index
df.drop(index=index,axis=0,inplace=True)

x=df.iloc[:,1].values
y=df.iloc[:,2].values
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=0)
cv = CountVectorizer()
x_train_tr = cv.fit_transform(x_train)
x_test_tr= cv.transform(x_test)
from sklearn.linear_model import LogisticRegression
clf=LogisticRegression()
clf.fit(x_train_tr,y_train)        






st.title("SENTIMENT ANALYSIS")
image=Image.open('IMG-20200904-WA0251.jpg')
st.image(image,width=800)
review = st.text_input('Enter your short review :')
df= {'review':review}
df=pd.DataFrame(df,index=[0])
to_pred=df.iloc[:,0]
result=clf.predict(cv.transform(to_pred))
if(st.button('Predict')):
    st.write(result[0])
    
    