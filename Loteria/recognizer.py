"""Train Model to recognize numbers."""
import cv2

import numpy as np

import pandas as pd

import matplotlib
import matplotlib.pyplot as plt

from sklearn.tree import DecisionTreeClassifier
from sklearn.externals import joblib

matplotlib.use('TkAgg')

data = pd.read_csv("train.csv").as_matrix()
clf = DecisionTreeClassifier()

xtrain = data[0:21000, 1:]
train_label = data[0:21000, 0]

clf.fit(xtrain, train_label)

xtest = data[21000:, 1:]
actual_label = data[21000:, 0]

filename = 'finalized_model.sav'
joblib.dump(clf, filename)

d = xtest[8]
d.shape = (28, 28)
plt.imshow(255 - d, cmap='gray')
print(clf.predict([xtest[8]]))

img = cv2.imread('test-img/test.png')

loaded_model = joblib.load(filename)
result = loaded_model.predict([img])
print(result)

plt.show()
