import pandas as pd
import jsonlines
import os


def prepare_medical_dataset(input_path, output_path):
    # Load the JSON file as a DataFrame
    df = pd.read_json(input_path)
    print("DataFrame shape:", df.shape)
    print("DataFrame head:\n", df.head(4))

    finetuning_dataset = []
    
    # Iterate over the DataFrame and prepare the instruction-response pairs
    for i in range(len(df)):
        instruction = f"### Patient Query:\n{df['Patient'][i]}\n\n\n### Doctor Response:\n"
        response = df['Doctor'][i]
        finetuning_dataset.append({
            "Question": instruction,
            "Answer": response
        })
    
    # Save the processed dataset into jsonlines format
    with jsonlines.open(output_path, 'w') as writer:
        writer.write_all(finetuning_dataset)
    
    print(f"Data has been successfully processed and saved to '{output_path}'.")


if __name__ == "__main__":
    # Define the input and output file paths
    input_json_path = "Dataset/json/processed_test_dataset.json"
    output_jsonl_path = "Dataset/interim/processed_test_dataset.jsonl"

    # Check if the input JSON file exists
    if not os.path.exists(input_json_path):
        print(f"Error: The file '{input_json_path}' does not exist.")
    else:
        # Call the function with input and output paths
        prepare_medical_dataset(input_path=input_json_path, output_path=output_jsonl_path)
