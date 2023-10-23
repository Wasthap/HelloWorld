
import streamlit as st
import numpy as np
import pandas as pd

"""st.write("Hello world!")
st.sidebar.text_input("Name")

st.text_input("Nam")

st.write(st.sidebar.text_input("Na")) """

""" my_list = [1,2,3]
print(my_list)

print(pd.__version__)

data = pd.Series([5,10,15,20])
print(data)
print(data.values)
print(data.index)
print(data[0])
print(data[2])
print(data[1:3])
print()
liste = [1,2,3,4,5]
indice = ['a','b', 4,'c','ab']
serie = pd.Series(data = liste, index = indice)
print(serie)
print()
serie2 = pd.Series(liste, indice)
print(serie2)
print()
serie3 = pd.Series([5,10,15,20,25],['a','b','ab',3,4])
print(serie3)
print(serie3['a']) """

"""notes_math_dic = {"Christophe":17, "Clara":10, "Amine":13, "Amandine":10.5, "Lina":13.5}
notes_math = pd.Series( notes_math_dic)
print(notes_math)
print(notes_math["Christophe"])
print()
notes_math1 = pd.Series (notes_math_dic, index = ["Clara", "Amine"])
print(notes_math1)"""

"""data = pd.Series([5,10,20,30,40], index = ["a","b","c","d","e"])
print(data)
data["a"] = 100
print(data)
data["x"] = 1000
print(data)
data["y"] = 2000
print(data)"""

""" notes_math_dic = {"Christophe":17, "Clara":10, "Amine":13, "Amandine":10.5, "Lina":13.5}
notes_math = pd.Series( notes_math_dic)
notes_12 = notes_math[notes_math>=12]
print(notes_12)
print()
notes_10_15 = notes_math[(notes_math<=15)&(notes_math>=10)]
print(notes_10_15)

dataframe_maths = pd.DataFrame(notes_math, columns = ["Note"])
print(dataframe_maths)
print()
d1 = {"a":5, "b":10, "c":15, "d":20}
d2 = {"a":25, "b":3, "c":35, "d":40}
d3 = {"a":45, "b":50, "c":55, "d":60}
dataframe_dic = pd.DataFrame([d1,d2,d3])
print(dataframe_dic)
print()
d4 = {"a":5, "b":10, "c":15, "d":20}
d5 = {"a":25, "d":40}
d6 = {"a":45, "b":50,  "d":60}

dataframe1 = pd.DataFrame([d4,d5,d6])
print(dataframe1)
print()
data_liste_dic = [{"a":i, "b":i*2, "c":i*i} for i in range(10)]
print(data_liste_dic)
dataframe_dic2 = pd.DataFrame(data_liste_dic)
print(dataframe_dic2) """

import numpy as np
import altair as alt
import pandas as pd
import streamlit as st

st.header('st.write')

# Example 1

st.write('Hello, *World!* :sunglasses:')

# Example 2

st.write(1234)

# Example 3

df = pd.DataFrame({
     "première colonne": [1, 2, 3, 4],
     "deuxième colonne": [10, 20, 30, 40]
     })
st.write(df)

# Example 4

st.write('Ci-dessous se trouve un DataFrame:', df, 'Ci-dessus se trouve un DataFrame.')

# Example 5

df2 = pd.DataFrame(
     np.random.randn(200, 3),
     columns=['amp', 'b', 'c'])
c = alt.Chart(df2).mark_circle().encode(
     x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])
st.write(c)

chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)
