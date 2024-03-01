# Laporan Proyek Machine Learning - Rifky Muhammad Shidiq
---

## Domain Proyek
---

### Latar Belakang
Pengunduran diri karyawan adalah merupakan keluarnya karyawan dari suatu perusahaan yang bisa disebabkan oleh faktor-faktor tertentu. Karyawan yang mengundurkan diri pada suatu perusahaan mengakibatkan pemutusan hubungan kerja dengan perusahaan, maka dengan itu berakhirlah kewajiban dan juga hak karyawan juga perusahaan. Pengunduran diri karyawan juga merupakan suatu isu yang signifikan dalam manajemen sumber daya manusia. Pengunduran diri karyawan ini juga dapat menyebabkan kerugian finansial bagi suatu perusahaan (Pangkey, 2012). Menurut data yang diambil dari Data Indonesia.id. penduduk Indonesia yang melakukan resign memiliki persentase sebesar 84% dimana itu merupakan angka yang cukup besar. Jumlah karyawan mengundurkan diri yang tinggi pada perusahaan dapat menimbulkan kemunduran bisnis, oleh karena itu perusahaan membutuhkan suatu model prediksi yang dapat membantu mengidentifikasi karyawan potensial yang mungkin akan mengundurkan diri di masa mendatang.

Salah satu metode yang dapat digunakan untuk prediksi tersebut adalah menggunakan algoritma _Random Forest_. _Random Forest_ adalah metode pembelajaran mesin yang menggabungkan beberapa pohon keputusan (_decision tree_) untuk membuat prediksi yang lebih akurat. Dengan menggunakan algoritma _Random Forest_, perusahaan dapat memanfaatkan data historis, seperti riwayat karyawan, umur, pendidikan, kepuasan kerja, dan faktor-faktor lain yang relevan, untuk membangun model yang dapat memprediksi kemungkinan pengunduran diri karyawan.

Berdasarkan permasalahan tersebut, maka akan dilakukan prediksi pengunduran diri karyawan menggunakan _Random Forest_ agar  perusahaan dapat mengambil langkah-langkah pencegahan yang tepat untuk meminimalisir pengunduran diri karyawan, mengurangi pengeluaran yang harus dikeluarkan dalam bentuk uang pesangon, serta menghindari kesulitan dalam mencari dan melatih ulang karyawan baru.


## Business Understanding
---

_Business understanding_ bertujuan untuk menggali pengetahuan (_discovering   knowledge_) mengenai pemodelan aturan untuk memprediksi pengunduran diri karyawan apakah tergolong dalam klasifikasi mengundurkan diri atau tidak berdasarkan dataset yang dimiliki perusahaan.

### Problem Statements
Menjelaskan pernyataan masalah latar belakang:
- Bagaimana penerapan algoritma _Random Forest_ dalam prediksi pengunduran diri karyawan?
- Bagaimana hasil evaluasi performa algoritma _Random Forest_ dengan menggunakan Confusion Matrix dan Cross Validation

### Goals
Berdasarkan masalah tersebut, tujuan dari proyek ini adalah :
- Untuk memperoleh model klasifikasi Random Forest dalam memprediksi pengunduran diri karyawan
- Untuk mengetahui evaluasi performa model  Random Forest menggunakan Confussion Matrix 


### Solution statements
Solusi yang dapat dilakukan agar goals terpenuhi adalah sebagai berikut :
1. Melakukan analisa, eksplorasi, pemrosesan pada data dengan memvisualisasikan data agar mendapat gambaran bagaimana data tersebut. Berikut adalah analisa yang dapat dilakukan :
   - Menangani_ missing value_ pada data
   - Melakukan transformasi data dengan mengubah data kategorikal menjadi data numerik
   - Melakukan _balancing_ data untuk mengatasi ketidakseimbangan antara kelas atau target variabel yang ada dalam dataset
   - Melakukan normalisasi pada data terutama pada fitur numerik
2. Membuat model regresi untuk memprediksi pengunduran di karyawan menggunakan algoritma Random Forest.
3. Melakukan evaluasi uji performa model menggunakan Confusion Matrix dan Cross Validation
      
## Data Understanding
Dalam tahapan ini, berfokus pada pemahaman tentang data yang digunakan dalam proyek analisis atau prediksi pengunduran diri karyawan. 
Dataset yang digunakan diperoleh dari penyedia dataset online yaitu website [kaggle](https://docs.google.com/spreadsheets/d/111VK34hBgbLqy4kHpPUhvudcfSksUopz/edit?usp=drive_link)  yang terdiri dari 1499 record dan 11 atribut

|     No     |     Emp_Id      |     satisfaction_level    |     last_evaluation    |     ...    |     salary    |
|------------|-----------------|---------------------------|------------------------|------------|---------------|
|     1.     |     IND02438    |     38%                   |     53%                |     ...    |     low       |
|     2.     |     IND28133    |     80%                   |     86%                |     ...    |     medium    |
|     3.     |     IND07164    |     11%                   |     88%                |     ...    |     medium    |
|     4.     |     IND30478    |     72%                   |     87%                |     ...    |     low       |
|     5.     |     IND24003    |     37%                   |     52%                |     ...    |     low       |
|     ...    |     ...         |     ...                   |     ...                |     ...    |     ...       |
|     14999  |     IND11649    |     37%                   |     52%                |     ...    |     low       |

### Variabel-variabel pada _HR Employee_ dataset adalah sebagai berikut: 
1. **Emp_Id**: Atribut ini adalah ID karyawan yang merupakan pengenal unik untuk setiap karyawan dalam dataset. ID ini digunakan untuk mengidentifikasi setiap entitas karyawan secara unik.
2.** satisfaction_level**: Atribut ini menggambarkan tingkat kepuasan karyawan dalam bentuk persentase. Ini dapat mencerminkan kepuasan karyawan terhadap pekerjaan, lingkungan kerja, manajemen, dan faktor-faktor lainnya yang mempengaruhi kepuasan mereka.
3. **last_evaluation**: Atribut ini mencerminkan penilaian terakhir karyawan dalam bentuk persentase. Hal ini dapat mencakup penilaian kinerja karyawan oleh atasan atau sistem evaluasi kinerja perusahaan.
4. **number_project**: Atribut ini menunjukkan jumlah proyek yang ditangani oleh karyawan. Ini dapat memberikan indikasi tentang tingkat tanggung jawab dan beban kerja karyawan.
5. **average_montly_hours**: Atribut ini mencerminkan rata-rata jumlah jam kerja bulanan oleh karyawan. Ini dapat mencerminkan tingkat kegiatan dan intensitas kerja karyawan.
6. **time_spend_company**: Atribut ini menunjukkan lama waktu yang telah dihabiskan oleh karyawan di perusahaan dalam tahun-tahun. Ini dapat mencerminkan pengalaman kerja dan loyalitas karyawan terhadap perusahaan.
7. **Work_accident**: Atribut ini menunjukkan apakah karyawan tersebut pernah mengalami kecelakaan kerja atau tidak. Nilai 1 menunjukkan adanya kecelakaan kerja, sedangkan nilai 0 menunjukkan tidak adanya kecelakaan.
8. **left**: Atribut ini menunjukkan apakah karyawan tersebut telah meninggalkan perusahaan atau masih bekerja. Nilai 1 menunjukkan karyawan yang telah meninggalkan perusahaan, sedangkan nilai 0 menunjukkan karyawan yang masih bekerja.
9. **promotion_last_5years**: Atribut ini menunjukkan apakah karyawan tersebut mendapatkan promosi dalam 5 tahun terakhir atau tidak. Nilai 1 menunjukkan adanya promosi, sedangkan nilai 0 menunjukkan tidak adanya promosi.
10. **Department**: Atribut ini menunjukkan departemen di mana karyawan bekerja. Contoh nilai departemen dalam dataset ini adalah "sales", yang menunjukkan karyawan bekerja di departemen penjualan.
11. **salary**: Atribut ini menunjukkan tingkat gaji karyawan. Nilai gaji dalam contoh dataset ini adalah "low" (rendah) dan "medium" (sedang). Gaji dapat memberikan indikasi tentang tingkat kompensasi dan penghargaan karyawan.


**Exploratory Data Analysis:
Sebelum memulai pemrosesan data, baiknya untuk melakukan eksplorasi data guna memahami karakteristik data
1. Tingkat kepuasan rata-rata untuk setiap departemen

Gambar diatas merupakan diagram batang yang memvisualisasikan tingkat kepuasan rata-rata untuk setiap departemen. Sumbu-x menampilkan departemen, dan sumbu-y menampilkan tingkat kepuasan rata-rata. Tinggi setiap batang sesuai dengan tingkat kepuasan rata-rata untuk departemen tersebut.

Sebagai contoh, departemen dengan tingkat kepuasan rata-rata tertinggi  adalah departemen nomor 6 yaitu _management_, sementara departemen dengan tingkat kepuasan rata-rata terendah  adalah departemen nomor 2 yaitu _accounting_.

Secara keseluruhan, gambar tersebut memberikan wawasan tentang tingkat kepuasan rata-rata karyawan di berbagai departemen dalam sebuah perusahaan, sehingga bisa membantu profesional sumber daya manusia atau manajer untuk mengidentifikasi tingkat kepuasan tiap departemen 

2. Pengaruh jumlah proyek terhadap jumlah jam kerja rata-rata per bulan

Gambar diatas merupakan diagram garis yang memvisualisasikan jumlah proyek terhadap jumlah jam kerja rata-rata per bulan. Dalam gambar tersebut menunjukkan semakin tinggi jumlah projek semakin banyak jumlah jam kerja rata-rata per bulan.

3. Korelasi Tiap Variabel

Berdasarkan gambar tersebut, interpretasinya yaitu :
* Korelasi antara satisfaction_level dengan variabel lain:
  - Korelasi negatif yang sedang dengan _left_ (-0.388375) yang menunjukkan bahwa semakin rendah tingkat kepuasan karyawan (_satisfaction_level_), semakin tinggi kemungkinan mereka akan meninggalkan perusahaan (_left_).
  - Korelasi positif yang lemah dengan _last_evaluation_ (0.105021) yang menunjukkan bahwa ada hubungan positif lemah antara tingkat kepuasan dan hasil evaluasi terakhir.

* Korelasi antara last_evaluation dengan variabel lain:
  - Korelasi positif yang sedang dengan _number_project_ (0.349333) dan _average_montly_hours_ (0.339742) yang menunjukkan bahwa hasil evaluasi terakhir cenderung meningkat seiring dengan peningkatan jumlah proyek dan jam kerja bulanan rata-rata.

* Korelasi antara number_project dengan variabel lain:
  - Korelasi positif yang sedang dengan average_montly_hours (0.417211) yang menunjukkan bahwa jumlah proyek yang lebih tinggi cenderung berkorelasi positif dengan jam kerja bulanan rata-rata yang lebih tinggi.

* Korelasi antara average_montly_hours dengan variabel lain:
  - Korelasi positif yang lemah dengan time_spend_company (0.127755) yang menunjukkan bahwa jam kerja bulanan rata-rata cenderung meningkat seiring dengan peningkatan lama bekerja di perusahaan.

* Korelasi antara left dengan variabel lain:
  - Korelasi negatif yang sedang dengan promotion_last_5years (-0.061788) yang menunjukkan bahwa ada hubungan negatif sedang antara keputusan karyawan untuk meninggalkan perusahaan dan apakah mereka mendapat promosi dalam lima tahun terakhir.


## Data Preparation
Pada bagian ini Anda menerapkan dan menyebutkan teknik data preparation yang dilakukan. Teknik yang digunakan pada notebook dan laporan harus berurutan.

**Rubrik/Kriteria Tambahan (Opsional)**: 
- Menjelaskan proses data preparation yang dilakukan
- Menjelaskan alasan mengapa diperlukan tahapan data preparation tersebut.

## Modeling
Tahapan ini membahas mengenai model machine learning yang digunakan untuk menyelesaikan permasalahan. Anda perlu menjelaskan tahapan dan parameter yang digunakan pada proses pemodelan.

**Rubrik/Kriteria Tambahan (Opsional)**: 
- Menjelaskan kelebihan dan kekurangan dari setiap algoritma yang digunakan.
- Jika menggunakan satu algoritma pada solution statement, lakukan proses improvement terhadap model dengan hyperparameter tuning. **Jelaskan proses improvement yang dilakukan**.
- Jika menggunakan dua atau lebih algoritma pada solution statement, maka pilih model terbaik sebagai solusi. **Jelaskan mengapa memilih model tersebut sebagai model terbaik**.

## Evaluation
Pada bagian ini anda perlu menyebutkan metrik evaluasi yang digunakan. Lalu anda perlu menjelaskan hasil proyek berdasarkan metrik evaluasi yang digunakan.

Sebagai contoh, Anda memiih kasus klasifikasi dan menggunakan metrik **akurasi, precision, recall, dan F1 score**. Jelaskan mengenai beberapa hal berikut:
- Penjelasan mengenai metrik yang digunakan
- Menjelaskan hasil proyek berdasarkan metrik evaluasi

Ingatlah, metrik evaluasi yang digunakan harus sesuai dengan konteks data, problem statement, dan solusi yang diinginkan.

**Rubrik/Kriteria Tambahan (Opsional)**: 
- Menjelaskan formula metrik dan bagaimana metrik tersebut bekerja.

**---Ini adalah bagian akhir laporan---**

_Catatan:_
- _Anda dapat menambahkan gambar, kode, atau tabel ke dalam laporan jika diperlukan. Temukan caranya pada contoh dokumen markdown di situs editor [Dillinger](https://dillinger.io/), [Github Guides: Mastering markdown](https://guides.github.com/features/mastering-markdown/), atau sumber lain di internet. Semangat!_
- Jika terdapat penjelasan yang harus menyertakan code snippet, tuliskan dengan sewajarnya. Tidak perlu menuliskan keseluruhan kode project, cukup bagian yang ingin dijelaskan saja.