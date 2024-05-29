# Annual-Cause-Death-Analysis

Proyek ini bertujuan untuk menganalisis data kematian tahunan berdasarkan berbagai penyebab kematian di seluruh dunia, dengan fokus khusus pada Indonesia. Analisis ini mencakup tren waktu, identifikasi penyebab kematian utama, korelasi antar penyebab kematian, serta tren kematian akibat HIV/AIDS dan penyakit menular serta tidak menular di Indonesia.

## Tujuan Analisis
1. Analisis Tren Waktu: Meneliti perubahan jumlah kematian dari tahun ke tahun untuk setiap penyebab kematian.
2. Analisis Penyebab Kematian Utama: Mengidentifikasi penyebab kematian utama secara global.
3. Korelasi Antar Penyebab Kematian: Menganalisis korelasi antara berbagai penyebab kematian untuk mengidentifikasi hubungan di antara mereka.
4. Tren Kematian akibat HIV/AIDS di Indonesia: Menganalisis tren kematian akibat HIV/AIDS di Indonesia dari tahun ke tahun.
5. Tren Kematian Penyakit Menular dan Tidak Menular di Indonesia: Membandingkan tren kematian akibat penyakit menular dan tidak menular di Indonesia.

## Dataset
Dataset yang digunakan dalam proyek ini adalah data publik yang tersedia di https://www.kaggle.com/datasets/willianoliveiragibin/annual-cause-death-numbers. Data ini mencakup informasi tahunan tentang berbagai penyebab kematian di seluruh dunia.

## Langkah Analisis dan Visualisasi
1. Pembersihan Data
   - Mengkonversi kolom 'Year' menjadi tipe data datetime.

2. Analisis Tren Waktu
   - Membuat subset data untuk masing-masing penyebab kematian.
   - Membuat visualisasi garis untuk melihat perubahan jumlah kematian dari tahun ke tahun untuk setiap penyebab kematian.
  
3. Analisis Penyebab Kematian Utama
   - Menghitung total kematian untuk setiap penyebab kematian.
   - Mengidentifikasi 10 penyebab kematian utama secara global.
   - Membuat visualisasi bar horizontal untuk 10 penyebab kematian utama.
  
4. Korelasi Antar Penyebab Kematian
   - Menghitung matriks korelasi antara berbagai penyebab kematian.
   - Membuat visualisasi heatmap untuk melihat hubungan antara penyebab kematian.
  
5. Tren Kematian akibat HIV/AIDS di Indonesia
   - Menyaring data untuk negara Indonesia dan penyebab kematian HIV/AIDS.
   - Membuat plot garis untuk melihat tren kematian akibat HIV/AIDS di Indonesia.

6. Tren Kematian Penyakit Menular dan Tidak Menular di Indonesia
   - Menyaring data untuk negara Indonesia.
   - Membuat plot garis untuk melihat tren kematian akibat penyakit menular dan tidak menular di Indonesia.
  
## Hasil dan Temuan
Proyek ini menghasilkan visualisasi dan analisis yang memberikan wawasan tentang tren kematian global dan di Indonesia. Temuan utama mencakup identifikasi penyebab kematian utama, hubungan antara berbagai penyebab kematian, serta tren spesifik kematian akibat HIV/AIDS dan penyakit menular dan tidak menular di Indonesia.

## Teknologi dan Tools yang Digunakan
- Python: Bahasa pemrograman utama yang digunakan untuk analisis data.
- Pandas: Untuk manipulasi dan analisis data.
- NumPy: Untuk operasi numerik.
- Matplotlib dan Seaborn: Untuk visualisasi data.

Proyek ini menyediakan wawasan yang komprehensif tentang penyebab kematian di seluruh dunia dan khususnya di Indonesia, yang dapat berguna bagi peneliti, pembuat kebijakan, dan masyarakat umum dalam memahami dan menangani isu kesehatan global.
