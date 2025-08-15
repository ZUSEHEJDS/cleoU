import requests

# Setze hier die URL deiner RegisterView!
URL = "https://backendforcleoai.onrender.com/api/accounts/register/"

payload = {
    "username": "testuser123",
    "email": "testuser123@example.com",
    "password": "Geheim123!",
    "agreed_to_privacy_policy_and_terms_of_use": True
}

response = requests.post(URL, json=payload)

print("Status Code:", response.status_code)
print("Antwort:", response.json())