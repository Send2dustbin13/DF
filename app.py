import streamlit as st


import pandas as pd

data=[(1, 'John Deo', 'Four', 75, 'female'),\
(0, 'Max Ruin', 'Three', 85, 'male'),\
(0, 'Arnold', 'Three', 55, 'male'),\
(1, 'Krish Star', 'Four', 60, 'female'),\
(1, 'John Mike', 'Four', 60, 'female'),\
(1, 'Gain Toe', 'Seven', 69, 'male'),\
(0, 'Rows Noump', 'Six', 88, 'female')]

schema = [ "id", "name", "grade", "dob", "gender" ]


df = df = pd.DataFrame(data, columns =schema )


block = st.container()

with st.expander("parameter"):
    st.write(df)
    
with block:
    block.title = "heading"
    block.markdown("Hello")
    block.write(df)

