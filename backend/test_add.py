import requests
import json

# Test data
test_data = {
    "type": "lost",
    "item_name": "Test Wallet",
    "description": "Black leather wallet",
    "location": "Test Station", 
    "vehicle_id": "BUS001",
    "contact_info": "test@test.com"
}

# Try both endpoints
print("Testing regular endpoint...")
response = requests.post('http://127.0.0.1:5000/api/report', json=test_data)
print(f"Regular endpoint: {response.json()}")

print("\nTesting blockchain endpoint...")
response = requests.post('http://127.0.0.1:5000/api/blockchain/add', json=test_data)
print(f"Blockchain endpoint: {response.json()}")

print("\nChecking blockchain...")
response = requests.get('http://127.0.0.1:5000/api/blockchain/chain')
print(f"Blockchain: {response.json()}")