#importing libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

#loading data file using pandas
data = pd.read_csv('data/prices.csv')

#predict prices moving up or down and remove non number values
data['target'] = (data['price'].shift(-1) > data['price'].astype(int))
data = data.dropna()

X = data[['price', 'volume']]
Y = data['target']

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

model = RandomForestClassifier(random_state=42)
model.fit(X_train, Y_train)
Y_pred = model.predict(X_test)
accuracy = accuracy_score(Y_test, Y_pred)
print(f"Model Accuracy: {accuracy:.2f}")

new_data = [[17000, 15000]]  
prediction = model.predict(new_data)
print("Prediction (1=Price Up, 0=Price Down):", prediction[0])