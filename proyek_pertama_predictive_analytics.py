# -*- coding: utf-8 -*-
"""Proyek Pertama : Predictive Analytics.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/13dlfsKGhZpd51EOWMF0LFkDFzp0C3qgK
"""

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from imblearn.over_sampling import SMOTE
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import cross_val_score
from sklearn.metrics import roc_auc_score

df = pd.read_csv('HR_Employee_Data.csv')
df.head(10)

"""# Menghapus kolom Emp_Id"""

df = df.drop("Emp_Id", axis=1)

"""# Cek Missing Value"""

df.isnull().sum()

df.info()

"""# Mengubah % menjadi desimal"""

df['satisfaction_level'] = df['satisfaction_level'].str.rstrip('%').astype(float) / 100
df['last_evaluation'] = df['last_evaluation'].str.rstrip('%').astype(float) / 100

"""# Mengubah Kolom Department menjadi Numerik"""

df['Department'].unique()

df['Department'].replace(to_replace = 'sales', value = 1, inplace = True)
df['Department'].replace(to_replace = 'accounting', value = 2, inplace = True)
df['Department'].replace(to_replace = 'hr', value = 3, inplace = True)
df['Department'].replace(to_replace = 'technical', value = 4, inplace = True)
df['Department'].replace(to_replace = 'support', value = 5, inplace = True)
df['Department'].replace(to_replace = 'management', value = 6, inplace = True)
df['Department'].replace(to_replace = 'IT', value = 7, inplace = True)
df['Department'].replace(to_replace = 'product_mng', value = 8, inplace = True)
df['Department'].replace(to_replace = 'marketing', value = 9, inplace = True)
df['Department'].replace(to_replace = 'RandD', value = 10, inplace = True)
df.head()

# dummies=pd.get_dummies(df['Department'],prefix='Department')
# df=pd.concat([df,dummies],axis=1)
# df.drop(['Department'],axis=1,inplace=True)
# df.head(10)

"""# Mengubah kolom salary menjadi kategorikal"""

# # Mengubah kolom Work_accident menjadi kategori
# df['Work_accident'] = df['Work_accident'].astype('category')

# # Mengubah kolom promotion_last_5years menjadi kategori
# df['promotion_last_5years'] = df['promotion_last_5years'].astype('category')

df['salary'] = df['salary'].apply(lambda s: 0 if s == 'low' else 1 if s == 'medium' else 2)

df.head()

"""## Pengaruh Gaji terhadap tingkat kepuasan"""

ret=df[['Department', 'satisfaction_level']].groupby(['Department'], as_index=False).mean().sort_values(by='satisfaction_level', ascending=False)
ret.plot.bar(x="Department", y="satisfaction_level", legend=False )

df.corr()

f, ax = plt.subplots(figsize=(8, 6))
corr = df.corr()

# Tambahkan angka pada heatmap
sns.heatmap(corr, mask=np.zeros_like(corr, dtype=np.bool), cmap=sns.diverging_palette(220, 10, as_cmap=True),
            square=True, ax=ax, annot=True, fmt=".2f")

plt.show()

"""## Pengaruh jumlah proyek terhadap jumlah jam kerja rata-rata per bulan."""

# Menentukan gaya plot menggunakan seaborn
sns.set(style="whitegrid")

# Membuat plot
plt.figure(figsize=(6, 4))  # Mengatur ukuran gambar

# Memplot data
sns.lineplot(data=df, x='number_project', y='average_montly_hours', marker='o')

# Menambahkan judul dan label sumbu
plt.title('Average Monthly Hours per Number of Projects', fontsize=16)
plt.xlabel('Number of Projects', fontsize=12)
plt.ylabel('Average Monthly Hours', fontsize=12)

# Menambahkan garis grid
plt.grid(True, linestyle='--', alpha=0.5)

# Menampilkan plot
plt.show()

"""##  Pengaruh jumlah proyek terhadap hasil evaluasi terakhir"""

# Menentukan gaya plot menggunakan seaborn
sns.set(style="whitegrid")

# Membuat plot
plt.figure(figsize=(6, 4))  # Mengatur ukuran gambar

# Memplot data
sns.lineplot(data=df, x='number_project', y='last_evaluation', marker='o')

# Menambahkan judul dan label sumbu
plt.title('Last Evaluation per Number of Projects', fontsize=16)
plt.xlabel('Number of Projects', fontsize=12)
plt.ylabel('Last Evaluation', fontsize=12)

# Menambahkan garis grid
plt.grid(True, linestyle='--', alpha=0.5)

# Menampilkan plot
plt.show()

# X = df[['satisfaction_level', 'last_evaluation', 'number_project', 'average_montly_hours', 'time_spend_company']]
X = df.drop(['left'],axis=1)
y = df['left']

# Visualize distribution of target variable
sns.countplot(x=y)
plt.show()
df.shape

smote = SMOTE(sampling_strategy='auto', random_state=73)
X_resampled, y_resampled = smote.fit_resample(X, y)
print("Sebelum SMOTE:", y.value_counts())
print("Setelah SMOTE:", y_resampled.value_counts())

y_resampled.shape

# Visualize distribution of target variable
sns.countplot(x=y_resampled)
plt.show()



"""## Melatih Model"""

X_train, X_test, y_train, y_test = train_test_split(X_resampled, y_resampled, random_state=1, test_size = 0.3)

model = RandomForestClassifier(n_estimators=10, random_state=19)
model.fit(X_train, y_train)
labels_predict = model.predict(X_test)
accuracy = accuracy_score(y_test, labels_predict)
precision = precision_score(y_test, labels_predict)
recall = recall_score(y_test, labels_predict)

print("Accuracy :", accuracy)
print("Precision:", precision)
print("Recall:", recall)

from sklearn import tree

# Mendapatkan daftar estimator dari model Random Forest
estimators = model.estimators_

# Visualisasi setiap pohon dalam Random Forest
for i in range(len(estimators)):
    fig, axes = plt.subplots(nrows=1, ncols=1, figsize=(7, 7))
    tree.plot_tree(estimators[i], feature_names=X_train.columns, class_names=["0", "1"], filled=True)
    plt.title('Decision Tree {}'.format(i+1))
    plt.show()

"""## Confussion Matrix"""

pd.DataFrame(
    confusion_matrix(y_test, labels_predict),
    columns=['Predicted Not Left', 'Predicted Left'],
    index=['True No Left', 'True Left']
)