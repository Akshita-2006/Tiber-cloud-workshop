import numpy as np #numerical operations
import pandas as pd #data manipulation and data loading
import seaborn as sns#data visualisation
from sklearn.model_selection import train_test_split#to split the data into training sets
from sklearn.metrics import accuracy_score, classification_report#for performance
import matplotlib.pyplot as plt#data visualisation
#from sklearn.preprocessing import LabelEncoder#to encode categorical values into numeric form
from sklearn.ensemble import RandomForestClassifier#classification tasks
import streamlit as st

data=pd.read_csv('loan_approval_dataset.csv')#loading the file

type(data)#checking type of dataset

data.head()# displaying first 5 rows

#data.shape#rows and column number ki kitne hai

data.describe()

data.isnull().sum()#kitne aise columns hai jinmai koi missing value hai

sns.countplot(x=' education',hue=' loan_status',data=data)
plt.title('Count of Loan Status by Education Level')#visualising that how much graduated/non graduated are approved or rejected for loan
#plt.show()
st.pyplot(plt)

#approved vs rejected loan status
plt.figure(figsize=(8, 6))
sns.countplot(data=data, x=' loan_status', palette='viridis')#colour scheme
plt.title("Distribution of Loan Status")
plt.xlabel("Loan Status (Approved / Rejected)")
plt.ylabel("Count")
#plt.show()
st.pyplot(plt)

plt.figure(figsize=(8, 6))
sns.scatterplot(data=data, x=' income_annum', y=' loan_amount', hue=' loan_status', palette='coolwarm')
plt.title("Income vs. Loan Amount")
plt.xlabel("Annual Income")
plt.ylabel("Loan Amount")
plt.legend(title="Loan Status")#basically kind of scale
#plt.show()
st.pyplot(plt)

# now we will convert into categorical forms like yes/no to 0/1 for machine understanding
data.replace({" loan_status":{' Rejected':0,' Approved':1}},inplace=True)

data.head()

data.replace({" education":{' Not Graduate':0,' Graduate':1}},inplace=True)

data.replace({" self_employed":{' No':0,' Yes':1}},inplace=True)

data.head()

X = data.drop(['loan_id', ' loan_status'], axis=1)  # Drop ID and target columns
y = data[' loan_status']  # Target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
#split into training sets

model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)#trains the model
#builds multiple decision trees and combines their predictions for a final output

y_pred = model.predict(X_test)
#model.predict generates predictions based on the test features (X_test).
#y_pred stores the predicted values of loan_status.

accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy * 100:.2f}%")#model performance
print("\nClassification Report:\n", classification_report(y_test, y_pred))

plt.figure(figsize=(10, 6))
feature_importances = pd.Series(model.feature_importances_, index=X.columns)
feature_importances.nlargest(10).sort_values().plot(kind='barh', color='skyblue')
plt.title("Top 10 Feature Importances")
plt.xlabel("Importance Score")
plt.ylabel("Features")
#plt.show()
st.pyplot(plt)
