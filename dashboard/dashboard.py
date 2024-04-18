import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
death_df = pd.read_csv('https://raw.githubusercontent.com/rizanss/Annual-Cause-Death-Analysis/main/data/annual_cause_death.csv')

# Sidebar
st.sidebar.title('Menu')
analysis_option = st.sidebar.selectbox('Pilih Analisis', ['Tren Waktu', 'Penyebab Kematian Utama', 'Korelasi Penyebab Kematian', 
                                                          'Tren Kematian HIV/AIDS di Indonesia', 'Tren Kematian Penyakit di Indonesia'])

# Main content
st.title('Dashboard Analisis Data Kematian Tahunan')

if analysis_option == 'Tren Waktu':
    st.subheader('Tren Jumlah Kematian Berdasarkan Penyebab dari Tahun ke Tahun')
    # Membuat subset data untuk masing-masing penyebab kematian
    penyebab_kematian = death_df.columns[3:]
    death_subset = death_df.melt(id_vars=['Entity', 'Code', 'Year'], value_vars=penyebab_kematian, var_name='Penyebab', value_name='Kematian')
    # Visualisasi
    st.write(death_subset)
    fig = plt.figure(figsize=(12, 6))
    sns.lineplot(data=death_subset, x='Year', y='Kematian', hue='Penyebab', ci=None)
    plt.title('Tren Jumlah Kematian Berdasarkan Penyebab dari Tahun ke Tahun')
    plt.xlabel('Tahun')
    plt.ylabel('Jumlah Kematian')
    plt.xticks(rotation=45)
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    st.pyplot(fig)

elif analysis_option == 'Penyebab Kematian Utama':
    st.subheader('10 Penyebab Kematian Utama')
    # Menghitung total kematian untuk setiap penyebab kematian
    total_kematian_penyebab = death_df.drop(columns=['Entity', 'Code', 'Year']).sum().reset_index()
    total_kematian_penyebab.columns = ['Penyebab', 'Total Kematian']
    total_kematian_penyebab = total_kematian_penyebab.sort_values(by='Total Kematian', ascending=False)
    # Mengambil 10 penyebab kematian utama
    top_10_penyebab = total_kematian_penyebab.head(10)
    st.write(top_10_penyebab)
    # Visualisasi
    fig = plt.figure(figsize=(12, 8))
    plt.barh(top_10_penyebab['Penyebab'], top_10_penyebab['Total Kematian'], color='skyblue')
    plt.xlabel('Total Kematian')
    plt.ylabel('Penyebab Kematian')
    plt.title('10 Penyebab Kematian Utama')
    plt.gca().invert_yaxis()
    st.pyplot(fig)

elif analysis_option == 'Korelasi Penyebab Kematian':
    st.subheader('Korelasi antar Penyebab Kematian')
    # Menghitung korelasi antara penyebab kematian
    corr_matrix = death_df.drop(columns=['Entity', 'Code', 'Year']).corr()
    st.write(corr_matrix)
    # Visualisasi
    fig = plt.figure(figsize=(24, 12))
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
    plt.title('Korelasi antar Penyebab Kematian')
    st.pyplot(fig)

elif analysis_option == 'Tren Kematian HIV/AIDS di Indonesia':
    st.subheader('Tren Kematian akibat HIV/AIDS di Indonesia')
    # Memilih data untuk negara Indonesia dan penyebab kematian HIV/AIDS
    data_indonesia_hiv = death_df[(death_df['Entity'] == 'Indonesia') & (death_df['HIV/AIDS fatalities'].notna())]
    # Memilih kolom 'Year' dan 'HIV/AIDS fatalities'
    tahun = data_indonesia_hiv['Year']
    kematian_hiv = data_indonesia_hiv['HIV/AIDS fatalities']
    # Visualisasi
    fig = plt.figure(figsize=(10, 6))
    plt.plot(tahun, kematian_hiv, marker='o', color='b')
    plt.title('Tren Kematian akibat HIV/AIDS di Indonesia')
    plt.xlabel('Tahun')
    plt.ylabel('Jumlah Kematian')
    plt.grid(True)
    plt.xticks(tahun, rotation=45)
    st.pyplot(fig)

else:  # analysis_option == 'Tren Kematian Penyakit di Indonesia'
    st.subheader('Tren Kematian Penyakit di Indonesia')
    # Memilih data untuk negara Indonesia
    data_indonesia = death_df[death_df['Entity'] == 'Indonesia']
    # Memilih kolom 'Year' untuk sumbu x
    tahun = data_indonesia['Year']
    # Memilih kolom kematian untuk penyakit menular
    penyakit_menular = ['Tuberculosis fatalities', 'Malaria fatalities', 'HIV/AIDS fatalities']
    # Memilih kolom kematian untuk penyakit tidak menular
    penyakit_tidak_menular = ['Cardiovascular fatalities', 'Diabetes fatalities', 'Neoplasm fatalities']
    # Plotting untuk penyakit menular
    fig = plt.figure(figsize=(12, 6))
    for penyakit in penyakit_menular:
        kematian = data_indonesia[penyakit]
        plt.plot(tahun, kematian, marker='o', label=penyakit)
    plt.title('Tren Kematian Penyakit Menular di Indonesia')
    plt.xlabel('Tahun')
    plt.ylabel('Jumlah Kematian')
    plt.grid(True)
    plt.xticks(tahun, rotation=45)
    plt.legend()
    st.pyplot(fig)

    # Plotting untuk penyakit tidak menular
    fig = plt.figure(figsize=(12, 6))
    for penyakit in penyakit_tidak_menular:
        kematian = data_indonesia[penyakit]
        plt.plot(tahun, kematian, marker='o', label=penyakit)
    plt.title('Tren Kematian Penyakit Tidak Menular di Indonesia')
    plt.xlabel('Tahun')
    plt.ylabel('Jumlah Kematian')
    plt.grid(True)
    plt.xticks(tahun, rotation=45)
    plt.legend()
    st.pyplot(fig)
