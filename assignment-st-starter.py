# import packages
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

# show the title
st.title('Titanic App by Junjie Zheng')

# read csv and show the dataframe
df = pd.read_csv('train.csv')
st.write(df)

# create a figure with three subplots, size should be (15, 5)
# show the box plot for ticket price with different classes
# you need to set the x labels and y labels
# a sample diagram is shown below
fig, ax = plt.subplots(1, 3, figsize=(15, 5))
for i, pclass in enumerate(sorted(df['Pclass'].unique()), start=0):
    df[df['Pclass'] == pclass].boxplot(column='Fare', ax=ax[i])
    ax[i].set_xlabel(f'PClass = {pclass}')
    ax[i].set_ylabel('Fare')

st.pyplot(fig)
