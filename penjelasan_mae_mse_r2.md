# Evaluasi Model Regresi: MAE, MSE, dan R²

## 1. Pendahuluan

Dalam machine learning, khususnya pada masalah regresi, performa model
dapat dievaluasi menggunakan beberapa metrik. Tiga metrik yang umum
digunakan adalah **Mean Absolute Error (MAE)**, **Mean Squared Error
(MSE)**, dan **Coefficient of Determination (R²)**.

Secara umum:

-   **MAE** semakin baik jika nilainya semakin mendekati 0.
-   **MSE** semakin baik jika nilainya semakin mendekati 0.
-   **R²** semakin baik jika nilainya semakin mendekati 1.

Ketiga metrik tersebut mengukur aspek yang berbeda. MAE dan MSE mengukur
besarnya kesalahan prediksi, sedangkan R² mengukur kemampuan model dalam
menjelaskan variasi pada variabel target.

## 2. Mean Absolute Error (MAE)

MAE adalah rata-rata nilai absolut dari selisih antara nilai aktual dan
nilai prediksi. Metrik ini menunjukkan seberapa jauh rata-rata prediksi
model dari nilai sebenarnya.

### Rumus

\[ MAE =
`\frac{1}{n}`{=tex}`\sum`{=tex}\_{i=1}\^{n}\|y_i-`\hat{y}`{=tex}\_i\| \]

Keterangan:

-   (n): jumlah data.
-   (y_i): nilai aktual.
-   (`\hat{y}`{=tex}\_i): nilai prediksi.

### Interpretasi

Nilai MAE ideal adalah **0**, yang berarti seluruh prediksi sama dengan
nilai aktual. Semakin kecil MAE, semakin kecil rata-rata kesalahan
absolut model.

MAE memiliki satuan yang sama dengan variabel target. Karena itu, besar
atau kecilnya MAE perlu dinilai berdasarkan skala dan konteks data.
Sebagai contoh, MAE sebesar 3 berarti rata-rata kesalahan absolut
prediksi adalah 3 satuan target, bukan otomatis berarti model buruk.

## 3. Mean Squared Error (MSE)

MSE adalah rata-rata kuadrat selisih antara nilai aktual dan nilai
prediksi. Karena kesalahan dikuadratkan, kesalahan yang besar mendapat
penalti lebih besar dibandingkan kesalahan kecil.

### Rumus

\[ MSE =
`\frac{1}{n}`{=tex}`\sum`{=tex}\_{i=1}\^{n}(y_i-`\hat{y}`{=tex}\_i)\^2
\]

Keterangan:

-   (n): jumlah data.
-   (y_i): nilai aktual.
-   (`\hat{y}`{=tex}\_i): nilai prediksi.

### Interpretasi

Nilai MSE ideal adalah **0**. Semakin kecil MSE, semakin kecil rata-rata
kuadrat kesalahan prediksi.

MSE menggunakan satuan kuadrat dari variabel target. Oleh sebab itu,
nilainya tidak boleh langsung dibandingkan dengan MAE atau ditafsirkan
tanpa mempertimbangkan skala target. MSE juga lebih sensitif terhadap
kesalahan prediksi yang besar karena proses pengkuadratan.

## 4. Coefficient of Determination (R²)

R² adalah metrik yang menggambarkan seberapa besar variasi pada variabel
target dapat dijelaskan oleh model dibandingkan dengan baseline yang
memprediksi rata-rata target.

### Rumus

\[ R\^2 = 1 - `\frac{\sum_{i=1}^{n}(y_i-\hat{y}_i)^2}`{=tex}
{`\sum`{=tex}\_{i=1}^{n}(y_i-`\bar`{=tex}{y})^2} \]

Keterangan:

-   (y_i): nilai aktual.
-   (`\hat{y}`{=tex}\_i): nilai prediksi.
-   (`\bar`{=tex}{y}): rata-rata nilai aktual.
-   (n): jumlah data.

### Interpretasi

-   **R² = 1**: prediksi sempurna pada data yang dievaluasi (selama
    target tidak konstan).
-   **R² = 0**: model memiliki performa setara dengan baseline yang
    selalu memprediksi rata-rata target pada data evaluasi.
-   **R² \< 0**: model lebih buruk daripada baseline tersebut.
-   **R² mendekati 1**: model menjelaskan proporsi variasi target yang
    lebih besar.

Contohnya, R² sebesar 0,97 berarti model menjelaskan sekitar 97% variasi
target pada data evaluasi menurut definisi R². Angka tersebut **bukan**
berarti 97% dari seluruh prediksi pasti benar.

## 5. Perbandingan MAE, MSE, dan R²

  -----------------------------------------------------------------------
  Metrik            Apa yang diukur?  Arah nilai yang   Nilai ideal
                                      diharapkan        
  ----------------- ----------------- ----------------- -----------------
  MAE               Rata-rata         Semakin kecil     0
                    kesalahan absolut semakin baik      

  MSE               Rata-rata kuadrat Semakin kecil     0
                    kesalahan         semakin baik      

  R²                Kemampuan model   Semakin besar     1
                    menjelaskan       semakin baik      
                    variasi target                      
  -----------------------------------------------------------------------

MAE dan MSE merupakan metrik *loss/error*, sehingga nilainya perlu
diminimalkan. R² merupakan *goodness-of-fit score*, sehingga nilainya
umumnya ingin dimaksimalkan.

Tidak ada ambang MAE atau MSE yang berlaku universal untuk semua
dataset. Penilaiannya bergantung pada satuan, rentang, distribusi
target, dan kebutuhan masalah. R² yang tinggi juga tidak dengan
sendirinya menjamin model akan memiliki kesalahan prediksi yang kecil
dalam satuan praktis. Karena itu, ketiga metrik sebaiknya dibaca
bersama-sama dan dihitung pada data pengujian yang tidak digunakan untuk
melatih model.

## 6. Contoh Interpretasi Hasil Evaluasi

Misalnya, suatu model regresi menghasilkan:

  ------------------------------------------------------------------------
  Metrik                                       Hasil Interpretasi
  --------------------- ---------------------------- ---------------------
  MAE                                              3 Rata-rata selisih
                                                     absolut prediksi
                                                     dengan nilai aktual
                                                     adalah 3 satuan
                                                     target.

  MSE                                              5 Rata-rata kuadrat
                                                     kesalahan adalah 5
                                                     satuan kuadrat
                                                     target.

  R²                                            0,97 Model menjelaskan
                                                     sekitar 97% variasi
                                                     target pada data
                                                     evaluasi.
  ------------------------------------------------------------------------

Hasil R² = 0,97 menunjukkan kemampuan menjelaskan variasi yang tinggi
pada data evaluasi. Namun, MAE = 3 dan MSE = 5 tetap perlu dinilai
berdasarkan skala variabel target dan dibandingkan dengan baseline atau
model lain. Tanpa informasi mengenai skala target, belum dapat
dipastikan apakah MAE sebesar 3 tergolong kecil atau besar.

## 7. Kesimpulan

MAE dan MSE semakin baik apabila nilainya semakin mendekati nol karena
keduanya mengukur kesalahan prediksi. Sebaliknya, R² semakin baik
apabila nilainya semakin mendekati satu karena menunjukkan bahwa model
mampu menjelaskan variasi target dengan lebih baik. R² dapat bernilai
negatif, sedangkan MAE dan MSE tidak negatif. Evaluasi model regresi
sebaiknya tidak hanya mengandalkan satu metrik: gunakan MAE dan MSE
untuk memahami besarnya kesalahan, serta R² untuk melihat kemampuan
model menjelaskan variasi target.

## 8. Referensi

1.  Chicco, D., Warrens, M. J., & Jurman, G. (2021). The coefficient of
    determination R-squared is more informative than SMAPE, MAE, MAPE,
    MSE and RMSE in regression analysis evaluation. *PeerJ Computer
    Science, 7*, e623. https://doi.org/10.7717/peerj-cs.623\
    Teks lengkap: https://pmc.ncbi.nlm.nih.gov/articles/PMC8279135/

2.  Scikit-learn Developers. (n.d.). *Model evaluation: Quantifying the
    quality of predictions*. Scikit-learn documentation.
    https://scikit-learn.org/stable/modules/model_evaluation.html

3.  Scikit-learn Developers. (n.d.). *r2_score*. Scikit-learn API
    documentation.
    https://scikit-learn.org/stable/modules/generated/sklearn.metrics.r2_score.html

------------------------------------------------------------------------

**Catatan:** Paper Chicco et al. (2021) merupakan artikel jurnal ilmiah.
Dokumentasi Scikit-learn adalah dokumentasi teknis resmi, bukan paper
jurnal. Keduanya digunakan sebagai sumber yang saling melengkapi: paper
untuk pembahasan ilmiah dan dokumentasi untuk definisi serta perilaku
metrik dalam implementasi Scikit-learn.
