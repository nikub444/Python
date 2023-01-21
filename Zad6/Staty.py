import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import time

st.title('Aplikacja Streamlit')

upload_file = st.file_uploader('Wgraj dane')
if(upload_file):
    with st.spinner("Extracting"):
        time.sleep(1)
    with st.spinner("Processing"):
        time.sleep(1)
    st.success('Done!')
if upload_file is not None:
   df = pd.read_csv(upload_file)

   chart = st.radio(
      "Rodzaj wizualizacji",
      ('Wykres pudelkowy', 'Histogram'))

   if chart == 'Wykres pudelkowy':
      target = st.radio(
         "Zmienna",
         df.columns.tolist())

      fig, ax = plt.subplots()
      ax.boxplot(df[target])

      st.pyplot(fig)

   if chart == 'Histogram':
      target = st.radio(
         "Zmienna",
         df.columns.tolist())

      fig, ax = plt.subplots()
      ax.hist(df[target], bins=20)

      st.pyplot(fig)