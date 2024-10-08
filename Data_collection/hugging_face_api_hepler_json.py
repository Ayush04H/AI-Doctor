# JSON
import requests
import os
import json

# Define the base URL and parameters for the API request
base_url = "https://datasets-server.huggingface.co/rows"
dataset_name = "ruslanmv/ai-medical-chatbot"
config = "default"
split = "train"
length = 100
total_rows = 1000

# Initialize an empty list to store the data
data = []
offset = 0

# Fetch data in chunks of 100 until reaching 1000 rows
while offset < total_rows:
    # Create the full API URL
    api_url = f"{base_url}?dataset={dataset_name}&config={config}&split={split}&offset={offset}&length={length}"
    
    # Send the GET request
    response = requests.get(api_url)
    
    # Check for successful response
    if response.status_code == 200:
        response_data = response.json()
        
        # Break if no more data is available
        if not response_data['rows']:
            break
        
        # Append the response JSON data to the list
        data.extend(response_data['rows'])
        
        # Update the offset for the next request
        offset += length
        
        # Stop if we've collected the desired amount of data
        if len(data) >= total_rows:
            data = data[:total_rows]
            break
    else:
        print(f"Failed to fetch data. Status code: {response.status_code}")
        break

# Create the Dataset folder if it doesn't exist
output_folder = "Dataset/json"
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Define the file path for saving the data as JSON
json_file_path = os.path.join(output_folder, "test_dataset.json")

# Save the data in JSON format
with open(json_file_path, 'w') as json_file:
    json.dump(data, json_file, indent=4)

print(f"Data has been successfully saved to {json_file_path}")
