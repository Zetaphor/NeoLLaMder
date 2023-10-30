
import json
import os
import glob
from collections import defaultdict

# Written by GPT-4

def process_chat_logs(folder_path, output_folder):
    """
    Process chat logs in a folder and separate messages by username.

    Args:
    - folder_path (str): The path to the folder containing the JSON chat logs.
    - output_folder (str): The path to the folder where the output JSON files will be saved.

    Returns:
    - List of paths to the generated JSON files for each unique username.
    """
    # Initialize a dictionary to store messages by username
    aggregated_messages_by_username = defaultdict(list)

    # Create the output directory if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    # Loop through each JSON file in the folder
    for filename in os.listdir(folder_path):
        if filename.endswith('.json'):
            file_path = os.path.join(folder_path, filename)
            # Load the JSON data from the file
            with open(file_path, 'r') as f:
                data = json.load(f)

            # Aggregate messages by username
            for message in data:
                username = message['username']
                aggregated_messages_by_username[username].append(message)

    # Generate a new JSON file for each unique username
    output_files = []
    for username, messages in aggregated_messages_by_username.items():
        output_file_path = os.path.join(output_folder, f'{username}.json')
        with open(output_file_path, 'w') as f:
            json.dump(messages, f)
        output_files.append(output_file_path)

    return output_files

# Example usage
if __name__ == "__main__":
    folder_path = "cleaned_data"
    output_folder = "user_transcripts"

    # Remove any existing JSON files in the output folder
    [os.remove(f) for f in glob.glob(os.path.join(output_folder, "*.json"))]

    generated_files = process_chat_logs(folder_path, output_folder)
