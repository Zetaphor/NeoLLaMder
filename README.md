# NeoLLaMder

Neo**LL**a**M**der is a project to fine-tune an LLM on the content of the Neolanders Discord server.

## Data Pipeline

Preparing the data for the LLM is a three step process:

1. Export the data with [Discrub](https://chrome.google.com/webstore/detail/discrub/plhdclenpaecffbcefjmpkkbdpkmhhbj) and place the JSON files in the `raw_data` directory
2. Run `1_format_data.py` which will remove the unneccesary data and create formatted JSON files in the `formatted_data` directory
3. Run `2_clean_data.py` which reformats the usernames according to the allowed usernames list, made up of users who have consented to having their username retained in the training data.
4. Run `3_extract_users.py` to separate the messages from individual users into separate JSON files

`allowed_usernames.txt` is the list of usernames to be retained in the training data. `substitute_usernames.txt` is a list of usernames generated with [Mockaroo](https://www.mockaroo.com/) that are used for pseudonymous users. Each pseudonymous user is assigned a username that remains consistent throughout the processing of the formatted discord data. These usernames are also substituted in messages from other users that mention the user.

`format_quotes.py` reformats the `quotes.json` from the `cleaned_data` folder to use the completion format for training. Below is an example of the output format.

```json
{"text": "quoted_username: \"Quoted text\""}
```

The data pipeline scripts were created in their entirety by prompting GPT-4.

## Training

More to follow as the project progresses.

## Disclaimer

This probably violates the Discord TOS. Use this responsibly and make sure you have the consent of both the admins and the community that you intend to scrape data and train from.

This is a fun project that was done with the consent of the people involved, and is intended to only be used within that private server. Don't be a dick and use this on a large public server where it's practically impossible to get consent.