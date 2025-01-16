import json
import random

# Veriyi yükle
data = [
    { "Age": 25, "Income": 30000, "FamilySize": 1, "HotelStar": 1, "HotelCost": 1000, "BookingStatus": 0, "TravelFrequency": 2, "PreviousBookings": 1, "VacationSpendLastYear": 5000.0, "ChildrenCount": 0, "StayDuration": 3 },
    { "Age": 29, "Income": 35000, "FamilySize": 2, "HotelStar": 2, "HotelCost": 2500, "BookingStatus": 0, "TravelFrequency": 1, "PreviousBookings": 0, "VacationSpendLastYear": 2000.0, "ChildrenCount": 1, "StayDuration": 2 },
    { "Age": 32, "Income": 45000, "FamilySize": 3, "HotelStar": 3, "HotelCost": 3000, "BookingStatus": 1, "TravelFrequency": 3, "PreviousBookings": 2, "VacationSpendLastYear": 8000.0, "ChildrenCount": 2, "StayDuration": 5 },
    # Diğer veri kayıtları
]

# Veriyi 5 katına çıkarmak
expanded_data = []

for item in data:
    for _ in range(5):  # her kaydı 5 katına çıkar
        new_item = item.copy()  # mevcut kaydın bir kopyasını al
        # Veriye rastgele değişiklikler ekleyerek yeni kayıtlar oluştur (isteğe bağlı)
        new_item["Age"] = item["Age"] + random.randint(-5, 5)
        new_item["Income"] = item["Income"] + random.randint(-1000, 1000)
        new_item["FamilySize"] = item["FamilySize"] + random.randint(-1, 2)
        new_item["HotelStar"] = item["HotelStar"] + random.randint(-1, 1)
        new_item["HotelCost"] = item["HotelCost"] + random.randint(-100, 500)
        new_item["BookingStatus"] = item["BookingStatus"]
        new_item["TravelFrequency"] = item["TravelFrequency"] + random.randint(-1, 3)
        new_item["PreviousBookings"] = item["PreviousBookings"] + random.randint(-1, 2)
        new_item["VacationSpendLastYear"] = item["VacationSpendLastYear"] + random.uniform(-100, 500)
        new_item["ChildrenCount"] = item["ChildrenCount"] + random.randint(-1, 2)
        new_item["StayDuration"] = item["StayDuration"] + random.randint(-1, 2)

        expanded_data.append(new_item)

# Çıktıyı JSON formatında kaydetmek
with open('expanded_data.json', 'w') as f:
    json.dump(expanded_data, f, indent=4)

print("Veri başarıyla 5 katına çıkarıldı ve 'expanded_data.json' olarak kaydedildi.")
