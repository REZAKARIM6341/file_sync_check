
# In[4]:


import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
from streamlit_autorefresh import st_autorefresh
import numpy as np
#import altair as alt
import matplotlib.pyplot as plt
#import my_module # initial import of my_module

#from importlib import reload 
#my_module = reload(my_module)	# reload of my_module

# Set the figure size
plt.rcParams["figure.figsize"] = [7.00, 3.50]
plt.rcParams["figure.autolayout"] = True

# Make a list of columns
columns = ['ID', 'NAME', 'RANK', 'ARTICLE','COUNTRY']

# Read a CSV file
df = pd.read_csv("event.csv", usecols=columns)

# Plot the lines
#df.plot()

#plt.show()
st.bar_chart(data=df, x="ID", y=None, width=0, height=0, use_container_width=True)
st_autorefresh(interval=2*1000, key="dataframerefresh")

def s(x,y):
    return x+y

