
import json
import re
import os

def get_substitute_username(username, username_mapping, substitute_iter):
    """Get a substitute username for a given username, keeping the substitution consistent."""
    if username in username_mapping:
        return username_mapping[username]

    # Get the next available substitute username
    substitute = next(substitute_iter)
    username_mapping[username] = substitute
    return substitute

def process_chatlog(chatlog, allowed_usernames, username_mapping, substitute_iter):
    """Process a single chatlog JSON."""
    for message in chatlog:
        original_username = message['username']
        if original_username not in allowed_usernames:
            message['username'] = get_substitute_username(original_username, username_mapping, substitute_iter)

        mentions = re.findall(r"@([\w.-]+)", message['content'])
        for mention in mentions:
            if mention not in allowed_usernames:
                substitute = get_substitute_username(mention, username_mapping, substitute_iter)
                message['content'] = message['content'].replace(f"@{mention}", f"@{substitute}")

def main(input_folder, output_folder):
    # Read allowed usernames
    with open('allowed_usernames.txt', 'r') as f:
        allowed_usernames = set(f.read().splitlines())

    # Read substitute usernames
    with open('substitute_usernames.txt', 'r') as f:
        substitute_usernames = f.read().splitlines()

    # Initialize a dictionary to keep track of username substitutions
    username_mapping = {}

    # Initialize an iterator for substitute usernames
    substitute_iter = iter(substitute_usernames)

    # Create output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.endswith('.json'):
            with open(os.path.join(input_folder, filename), 'r') as f:
                chatlog = json.load(f)

            process_chatlog(chatlog, allowed_usernames, username_mapping, substitute_iter)

            with open(os.path.join(output_folder, filename), 'w') as f:
                json.dump(chatlog, f, indent=4)

# Uncomment the line below to run the script
main('formatted_data', 'cleaned_data')
