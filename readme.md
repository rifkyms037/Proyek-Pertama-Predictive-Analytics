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

## Problem Statements
Berdasarkan masalah yang terpapar pada latar belakang, permasalahan yang dapat diselesaikan pada proyek ini adalah sebagai berikut :
- Bagaimana penerapan algoritma _Random Forest_ dalam prediksi pengunduran diri karyawan?
- Bagaimana hasil evaluasi performa algoritma _Random Forest_ menggunakan _Confusion Matrix_?

## Goals
Berdasarkan masalah tersebut, tujuan dari proyek ini adalah :
- Untuk memperoleh model klasifikasi Random Forest dalam memprediksi pengunduran diri karyawan
- Untuk mengetahui evaluasi performa model  Random Forest menggunakan _Confussion Matrix_ 


## Solution statements
Solusi yang dapat dilakukan agar goals terpenuhi adalah sebagai berikut :
1. Melakukan analisa, eksplorasi, pemrosesan pada data dengan memvisualisasikan data agar mendapat gambaran bagaimana data tersebut. Berikut adalah analisa yang dapat dilakukan :
   - Melakukan transformasi data dengan mengubah data kategorikal menjadi data numerik
   - Melakukan _balancing_ data untuk mengatasi ketidakseimbangan antara kelas atau target variabel yang ada dalam dataset
2. Membuat model regresi untuk memprediksi pengunduran di karyawan menggunakan algoritma Random Forest.
3. Melakukan evaluasi uji performa model menggunakan _Confusion Matrix_ 
      
## Data Understanding
Dalam tahapan ini, berfokus pada pemahaman tentang data yang digunakan dalam proyek analisis atau prediksi pengunduran diri karyawan. 
Dataset yang digunakan diperoleh dari penyedia dataset online yaitu website [kaggle](https://docs.google.com/spreadsheets/d/111VK34hBgbLqy4kHpPUhvudcfSksUopz/edit?usp=drive_link)  yang terdiri dari 14993 record dan 11 atribut

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


## Exploratory Data Analysis:
Sebelum memulai pemrosesan data, baiknya untuk melakukan eksplorasi data guna memahami karakteristik data

1. Tingkat kepuasan rata-rata untuk setiap departemen
<div><img src="https://raw.githubusercontent.com/rifkyms037/Proyek-Pertama-Predictive-Analytics/main/assets/images/gaji.png" width="500"/></div>
Gambar diatas merupakan diagram batang yang memvisualisasikan tingkat kepuasan rata-rata untuk setiap departemen. Sumbu-x menampilkan departemen, dan sumbu-y menampilkan tingkat kepuasan rata-rata. Tinggi setiap batang sesuai dengan tingkat kepuasan rata-rata untuk departemen tersebut.

Sebagai contoh, departemen dengan tingkat kepuasan rata-rata tertinggi  adalah departemen nomor 6 yaitu _management_, sementara departemen dengan tingkat kepuasan rata-rata terendah  adalah departemen nomor 2 yaitu _accounting_.

Secara keseluruhan, gambar tersebut memberikan wawasan tentang tingkat kepuasan rata-rata karyawan di berbagai departemen dalam sebuah perusahaan, sehingga bisa membantu profesional sumber daya manusia atau manajer untuk mengidentifikasi tingkat kepuasan tiap departemen 

2. Pengaruh jumlah proyek terhadap jumlah jam kerja rata-rata per bulan
<div><img src="https://raw.githubusercontent.com/rifkyms037/Proyek-Pertama-Predictive-Analytics/main/assets/images/Pengaruh%20jumlah%20proyek.png" width="500"/></div>

Gambar diatas merupakan diagram garis yang memvisualisasikan jumlah proyek terhadap jumlah jam kerja rata-rata per bulan. Dalam gambar tersebut menunjukkan semakin tinggi jumlah projek semakin banyak jumlah jam kerja rata-rata per bulan.

4. Korelasi Tiap Variabel
<div><img src="https://raw.githubusercontent.com/rifkyms037/Proyek-Pertama-Predictive-Analytics/main/assets/images/heatmap.png" width="500"/></div>

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
Data mentah yang diperoleh pada tahap sebelumnya perlu melalui tahap Persiapan Data (_Data Preparation_). Berikut langkah-langkah yang harus dilakukan pada data _preparation_ :
### **Data _Transformation_**
Data _transformation_, adalah pengubahan format menjadi bentuk yang lebih sesuai proses _data mining_. Berikut merupakan proses transformasi data yang dilakukan :
<div><img src="https://raw.githubusercontent.com/rifkyms037/Proyek-Pertama-Predictive-Analytics/main/assets/images/transformasi.jpeg" width="300"/></div>
Berdasarkan Gambar diatas, proses transformasi data dilakukan pada atribut salary, dan departement dengan mengubah data kategorikal menjadi data numerik. Proses transformasi data dilakukan juga pada atribut satisfication_level, seperti mengubah isi baris 38% menjadi 0.38 dan seterusnya.

### **Data _Balancing_**
_Data balancing_, adalah proses memanipulasi dataset untuk mengatasi ketidakseimbangan antara kelas atau target variabel yang ada dalam dataset. Metode digunakan untuk mengatasi imbalance data yaitu SMOTE  (_Synthetic Minority Over-sampling Technique_) dengan penambahan lebih banyak sampel pada kelas minoritas untuk menyamakan jumlah sampel dengan kelas mayoritas.
<div><img src="https://raw.githubusercontent.com/rifkyms037/Proyek-Pertama-Predictive-Analytics/main/assets/images/imbalanced.png" width="500"/></div>
Berdasarkan Gambar 4, terdapat _imbalance data_ pada atribut target yaitu _left_, dimana  terdapat _imbalance_ pada kelas 0 tidak mengundurkan diri sebanyak 11.428 dan kelas 1 pengunduran diri sebanyak 3571, maka selanjutnya akan melakukan sampling data pada kelas 1 menyesuaikan dengan jumlah kelas 0 menggunakan teknik SMOTE menggunakan pemrograman _python._ Berikut hasil dari _data balancing_ yang telah dilakukan :
<div><img src="https://raw.githubusercontent.com/rifkyms037/Proyek-Pertama-Predictive-Analytics/main/assets/images/balanced.png" width="500"/></div>
Proses _balancing data_ telah berhasil dilakukan, sehingga kelas 0 dan kelas 1 sudah seimbang, sehingga setelah melakukan proses diatas bisa dilanjut ke tahap berikutnya yaitu tahap modelling.


## Modeling
Setelah melakukan beberapa proses sebelumnya, sehingga data siap untuk diproses, tahap selanjutnya yaitu melakukan proses modelling dengan tujuan untuk mengembangkan model prediktif yang dapat digunakan untuk melakukan analisis lebih lanjut dan membuat prediksi pengunduran diri karyawan. Teknik permodelan yang akan digunakan pada penelitian ini adalah algoritma Random Forest. Random Forest adalah  adalah algoritma machine learning yang terdiri dari banyak pohon keputusan yang dibuat melalui proses bagging atau bootstrap aggregating (Normah et al., 2022), lalu digabungkan untuk menghasilkan hasil akhir. Bagging atau bootstrap aggregating adalah teknik pembentukan model dengan membangun banyak model keputusan pada sampel data yang berbeda-beda dan akhirnya menggabungkan hasil prediksi dari model-model tersebut. Dengan demikian, Random Forest dapat menghasilkan prediksi yang lebih akurat dan tahan terhadap overfitting. 
Cara kerja dari Random Forest terdiri dari dua fase utama. Fase pertama yaitu menggabungkan jumlah N pohon keputusan dengan melibatkan pembuatan dari algoritma Random Forest, setelah pohon keputusan dari sejumlah N yang terbentuk, selanjutnya dilanjutkan pada fase kedua, yaitu membuat prediksi dari setiap decision tree yang telah dibuat pada fase pertama.
<div><img src="https://raw.githubusercontent.com/rifkyms037/Proyek-Pertama-Predictive-Analytics/main/assets/images/image.png" width="500"/></div>

Pada tahapan ini proses yang dilakukan terdiri dari pemilihan variabel X yang digunakan sebagai input dan variabel Y sebagai target yaitu mengundurkan diri atau tidak mengundurkan diri. Kemudian dilakukan pembagian dataset menjadi data training dan data testing dengan rasio sebesar 70%:30% dari jumlah dataset sebanyak 1499 data. Selanjutnya melakukan penyetelan parameter Random Forest untuk mencapai kinerja yang optimal, beberapa parameter yang digunakan pada penelitian ini adalah n_estimator sebanyak 10 pohon untuk mengontrol jumlah pohon yang dibangun  dan random state sebanyak 19. Setelah proses pengembangan model Random Forest dan penyetelan parameter dilakukan, selanjutnya dilakukan evaluasi uji performa untuk mengukur kinerja  suatu model.

## Evaluation
Pada tahap ini, untuk mengetahui kinerja performa pada model yang telah dibuat, diperlukan perhitungan matematis untuk menentukan seberapa akurat model dapat memprediksi nilai target, yaitu dengan menggunakan _Confussion Matrix_. _Confussion Matrix_ adalah sebuah metode yang digunakan untuk mengukur kinerja suatu metode_ classification_ . Gambar _confusion matrix_ ditunjukkan pada gambar berikut ini:
<div><img src="https://raw.githubusercontent.com/rifkyms037/Proyek-Pertama-Predictive-Analytics/main/assets/images/confussion.png" width="500"/></div>
Keterangan :

1. _True Positive_ (TP) adalah jumlah sampel positif yang berhasil diklasifikasikan dengan benar sebagai positif oleh model klasifikasi.
2. _True Negative_ (TN) adalah jumlah sampel negatif yang berhasil diklasifikasikan dengan benar sebagai negatif oleh model klasifikasi.
3. _False Positive_ (FP) adalah jumlah sampel negatif yang salah diklasifikasikan sebagai positif oleh model klasifikasi.
4. _False Negative_ (FN) adalah jumlah sampel positif yang salah diklasifikasikan sebagai negatif oleh model klasifikasi.

Dari _confusion matrix_, selanjutnya dapat menghitung beberapa metrik evaluasi yang berguna untuk mengukur kinerja suatu model klasifikasi. Berikut adalah beberapa metrik evaluasi yang dapat dihitung dari _confusion matrix_:

1. Akurasi
Akurasi adalah sebuah metrik evaluasi yang menghitung seberapa banyak prediksi yang benar dari seluruh prediksi yang dilakukan oleh sebuah model.  
Dengan rumus :
Akurasi = (TP + TN) / (TP + TN + FP + FN)
Keterangan :
TP = _True Positive_.
TN = _True Negative_.
FP = _False Positive_.
FN = _False Negative_.
2. Presisi
Presisi adalah metrik evaluasi yang menghitung seberapa banyak prediksi positif yang benar dari seluruh prediksi positif yang dilakukan oleh sebuah model. Dengan rumus :
Presisi=  TP/(TP+FP)                                                                                                   
Keterangan: 
TP = _True Positive_.
FP = _False Positive_.
3. _Recall_
_Recall_ adalah metrik evaluasi yang digunakan untuk mengukur kemampuan suatu model klasifikasi dalam mengidentifikasi secara benar semua sampel positif yang ada.
_Recall_ =  TP/(TP+FN)                                                                                                 
Keterangan:
TP = _True Positive_.
FN = _False Negative_.

Berikut merupakan nilai confussion matrix yang diperoleh :
|                     |     Predicted Not Left    |     Predicted Left    |
|---------------------|---------------------------|-----------------------|
|     True No Left    |     3381                  |     17                |
|     True Left       |     111                   |     3348              |

Berdasarkan Tabel diatas diperoleh prediksi tidak _left_ terhadap prediksi benar tidak _left_ sebanyak 3381 sedangkan prediksi tidak _left_ terhadap prediksi benar _left_ sebesar 111 dan prediksi left terhadap benar tidak _left_ sebesar 17 sedangkan prediksi left terhadap benar left sebanyak 3348. Sehingga dari Tabel 4 diperoleh nilai akurasi, presisi, dan _recall_ sebagai berikut :

Proses untuk mengetahui nilai akurasi dilakukan pada persamaan akurasi sebagai berikut :
- Akurasi = (TP+TN)/(TP+TN+FP+FN) 
=  (3348+3381)/(3348+3381+17+111)=0.98133 

Sedangkan, pada proses perhitungan presisi dilakukan pada persamaan presisi sebagai berikut :
- Presisi = TP/(TP+FP)     
=  3348/(3348+17)=0.99498 

Kemudian, untuk menghitung recall dilakukan pada persamaan _recall_ sebagai berikut :
- Recall = $$ TP = {TP \over TP+FN } $$ 
=  3348/(3348+111)=0.96791 

Setelah melakukan perhitungan performa model, diperoleh tingkat akurasi sebesar 98.13%, presisi sebesar 99.48% dan recall sebesar 96.79%. Sehingga prediksi pengunduran diri karyawan menggunakan confussion matrix dapat dikategorikan sebagai excellent classification (Koniyo & Sudarma, 2020)




**---Ini adalah bagian akhir laporan---**

_Catatan:_
- _Anda dapat menambahkan gambar, kode, atau tabel ke dalam laporan jika diperlukan. Temukan caranya pada contoh dokumen markdown di situs editor [Dillinger](https://dillinger.io/), [Github Guides: Mastering markdown](https://guides.github.com/features/mastering-markdown/), atau sumber lain di internet. Semangat!_
- Jika terdapat penjelasan yang harus menyertakan code snippet, tuliskan dengan sewajarnya. Tidak perlu menuliskan keseluruhan kode project, cukup bagian yang ingin dijelaskan saja.
