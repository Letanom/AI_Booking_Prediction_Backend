import json
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib

# JSON dosyasından veri okuma
with open('data.json', 'r') as file:
    data = json.load(file)

# Veri setini DataFrame'e dönüştürme
df = pd.DataFrame(data)

# Özellikler (X) ve hedef değişken (y) belirleniyor
X = df[['Age', 'Income', 'FamilySize', 'HotelStar', 'TravelFrequency', 'PreviousBookings', 'VacationSpendLastYear', 'ChildrenCount', 'StayDuration']]
y = df['BookingStatus']

# Eğitim ve test verilerini ayırma
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Modeli oluşturma ve eğitme
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Modeli test etme ve doğruluğu hesaplama
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Doğruluğu: {accuracy * 100:.2f}%")

# Modeli kaydetme
joblib.dump(model, 'model.pkl')
print("Model kaydedildi.")
