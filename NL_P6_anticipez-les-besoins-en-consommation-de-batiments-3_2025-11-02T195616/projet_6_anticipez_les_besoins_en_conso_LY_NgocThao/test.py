import requests

data = {
    "PropertyGFATotal": 3,
    "NumberofFloors": 3,
    "NumberofBuildings": 1,
    "YearBuilt": 1,
    "YearsENERGYSTARCertified": 1
}

response = requests.post("http://localhost:3000/predict", json=data)
print(response.json())