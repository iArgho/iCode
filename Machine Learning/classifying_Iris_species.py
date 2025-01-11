from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
import pandas as pd
import matplotlib.pyplot as plt
from pandas.plotting import scatter_matrix
import mglearn

iris_dataset = load_iris()

# Explore the dataset
print("Keys of iris_dataset: \n{}".format(iris_dataset.keys()))
print(iris_dataset['DESCR'][:193] + "\n")

print("Target names: {}".format(iris_dataset['target_names']))
print("Feature names: {}".format(iris_dataset['feature_names']))
print("Type of data: {}".format(type(iris_dataset['data'])))
print("Shape of data: {}".format(iris_dataset['data'].shape))
print("First 5 columns of data:\n{}".format(iris_dataset['data'][:5]))
print("Target:\n{}".format(iris_dataset['target']))

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    iris_dataset['data'], iris_dataset['target'], random_state=0
)

print("X_train shape: {}".format(X_train.shape))
print("y_train shape: {}".format(y_train.shape))
print("X_test shape: {}".format(X_test.shape))
print("y_test shape: {}".format(y_test.shape))

# Create a DataFrame from the training data
iris_dataframe = pd.DataFrame(X_train, columns=iris_dataset['feature_names'])

# Create a scatter matrix
grr = scatter_matrix(
    iris_dataframe, 
    c=y_train, 
    figsize=(15, 15), 
    marker='o', 
    hist_kwds={'bins': 20}, 
    s=60, 
    alpha=.8, 
    cmap=mglearn.cm3
)

#plt.show()

from sklearn.neighbors import KNeighborsClassifier
knn=KNeighborsClassifier(n_neighbors=1)

knn.fit(X_train, y_train)

import numpy as np
X_new=np.array([[5,2.9,1.0,.2]])

print("X_new.shape: {}".format(X_new.shape))

predition =knn.predict(X_new)
print("Prediction: {}".format(predition))
print("Prdiction Target Name: {}".format(
    iris_dataset['target_names'][predition]
)
)

y_pred=knn.predict(X_test)
print("Test set predictions\n{}".format(y_pred))

print("Test Score : {:.2f}\n".format(np.mean(y_pred==y_test)))

