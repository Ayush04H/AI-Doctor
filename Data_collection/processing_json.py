import json

# Load the dataset from the input file
input_file = 'Dataset/json/test_dataset.json'
output_file = 'Dataset/json/processed_test_dataset.json'

def process_data(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as file:
        data = json.load(file)

    # Remove unnecessary data and create the new dataset
    new_data = []
    for entry in data:
        # Extract the required fields
        new_entry = {
            "Description": entry['row']['Description'],
            "Patient": entry['row']['Patient'],
            "Doctor": entry['row']['Doctor']
        }
        new_data.append(new_entry)

    # Save the new dataset to the output file
    with open(output_file, 'w', encoding='utf-8') as file:
        json.dump(new_data, file, indent=4)

# Process the input file and generate the new output
process_data(input_file, output_file)

print(f"Processed data saved to {output_file}")
