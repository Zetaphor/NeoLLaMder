import os
import json
import glob

# Written by GPT-4

def extract_and_sort_messages(json_file_path):
    # Read the JSON file
    with open(json_file_path, 'r') as f:
        chat_data = json.load(f)

    # Initialize an empty list to store the extracted information
    extracted_data = []

    # Iterate through each message in the JSON list
    for message in chat_data:
        # Initialize a dictionary to store extracted data for each message
        message_data = {}

        # Extract message ID
        message_data['id'] = message.get('id', 'N/A')

        # Extract username
        message_data['username'] = message.get('username', 'N/A')

        # Extract timestamp
        message_data['timestamp'] = message.get('timestamp', 'N/A')

        # Extract message content
        message_data['content'] = message.get('content', 'N/A')

        # Append the extracted data to the list
        extracted_data.append(message_data)

    # Sort the list of dictionaries by timestamp from oldest to newest
    sorted_extracted_data = sorted(extracted_data, key=lambda x: x['timestamp'])

    return sorted_extracted_data

def process_folder(input_folder, output_folder):
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Iterate through all files in the input folder
    for filename in os.listdir(input_folder):
        if filename.endswith('.json'):
            input_file_path = os.path.join(input_folder, filename)

            # Extract and sort messages
            sorted_messages = extract_and_sort_messages(input_file_path)

            # Save to a new JSON file in the output folder
            output_file_path = os.path.join(output_folder, filename)
            with open(output_file_path, 'w') as f:
                json.dump(sorted_messages, f, indent=4)

if __name__ == "__main__":
    # Define the path to the folder containing the JSON files and the output folder
    input_folder_path = "discord_data"
    output_folder_path = "formatted_data"

    # Remove any existing JSON files in the output folder
    [os.remove(f) for f in glob.glob(os.path.join(output_folder_path, "*.json"))]

    # Process all JSON files in the folder
    process_folder(input_folder_path, output_folder_path)
