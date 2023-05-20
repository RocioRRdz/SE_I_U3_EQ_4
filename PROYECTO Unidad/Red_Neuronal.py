import tensorflow as tf
import pandas as pd
import numpy as np

df = pd.read_csv("datos.txt", sep=", ", header=None, names=["Index", "Value"])
numeros = df["Value"].tolist()
#################################
##split data
X = df.iloc[:, :3].values
print("\n", X[0:5]) #first 5 inputs
print(X.shape)

#################################
##Convert target into LabelEncoder
from sklearn.preprocessing import LabelEncoder
encoder = LabelEncoder()

#################################
#Convert target into one hot encoding
Y = pd.get_dummies(df["Index"]).values
print("\n", Y[0:5])

#################################
###Convert X and Y into train and test data
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=0)

print("\nTrain: ")
print(X_train[0:5])
print("")
print(y_train[0:5])
print("\n\n Test: ")
print(X_test[0:5])
print("")
print(y_test[0:5])

#################################
model = tf.keras.Sequential([
    tf.keras.layers.Dense(10, activation='relu'),
    tf.keras.layers.Dense(10, activation='relu'),
    tf.keras.layers.Dense(50, activation='softmax')  # Adjust the number of units to match the number of classes
])

print("Model: ")
print(model)
#################################

model.compile(optimizer='rmsprop',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

model.fit(X_train, y_train, batch_size=50, epochs=100) #train the model

print("\n\n")
loss, accuracy = model.evaluate(X_test, y_test, verbose=0) #evaluate the model with test data
print('Test loss:', loss)
print('Test accuracy:', accuracy)

#print("\n\nPredictions:")
#y_pred = model.predict(X_test)
#print(y_pred)

#print("\n\nValues Comparision:")
#actual = np.argmax(y_test,axis=1)
#predicted = np.argmax(y_pred,axis=1)
#print(f"Actual: {actual}")
#print(f"Predicted: {predicted}")


