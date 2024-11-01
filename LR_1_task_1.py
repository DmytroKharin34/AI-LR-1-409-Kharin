# -*- coding: utf-8 -*-
"""2.1.5 Label encoding.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1P1QHtCgtigd0FsA3RxUpzGD2_bT67ucI
"""

import numpy as np
from sklearn import preprocessing

# Надання позначок вхідних даних
input_labels = ['red', 'black', 'red', 'green', 'black', 'yellow', 'white']

# Створення кодувальника та встановлення відповідності між мітками та числами
encoder = preprocessing.LabelEncoder()
encoder.fit(input_labels)

# Виведення відображення
print("\n Label mapping:")
for i, item in enumerate(encoder.classes_):
  print(item, '-->', i)

# Перетворення міток за допомогою кодувальника
test_labels = ['green', 'red', 'black']
encoded_values = encoder.transform(test_labels)
print("\nLabels =", test_labels)
print("Encoded values =", list(encoded_values))

# Декодування набору чисел за допомогою декодера
encoded_values = [3, 0, 4, 1]
decoded_list = encoder.inverse_transform(encoded_values)
print("\nEncoded values =", encoded_values)
print("Decoded labels =", list(decoded_list))