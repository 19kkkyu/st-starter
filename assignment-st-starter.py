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

fig, ax = plt.subplot(1, 3, figsize=(15, 5))
for i, pclass in enumerate(sorted(df['Pclass'].unique()), start=1):
    fig, ax = plt.subplot(1, 3, i)
    df[df['Pclass'] == pclass].boxplot(column='Fare', ax=ax)
    ax.xlabel(f'PClass = {pclass}')
    ax.ylabel('Fare')

st.pyplot(fig)
