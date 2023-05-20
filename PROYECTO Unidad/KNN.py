
import pandas as pd

# Importar el dataset
df = pd.read_csv("datos.txt", sep=", ", header=None, names=["Index", "Value"])
numeros = df["Value"].tolist()
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

# Ajuste de escalas
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

# Entrenamiento del modelo KNN
from sklearn.neighbors import KNeighborsClassifier
classifier = KNeighborsClassifier(n_neighbors = 5, metric = 'minkowski', p = 2)
classifier.fit(X_train, y_train)

# Predicción del conjunto de prueba
y_pred = classifier.predict(X_test)
print(y_pred)

# Matriz de confusion
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test.argmax(axis=1), y_pred.argmax(axis=1))
print("Matriz de confusión: "+str(cm))

