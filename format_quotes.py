import json
import re

# Written by GPT-4
# Reformats the data from the quotes channel to use the completion format for axlotl
# ex: {"text": "quoted_username: \"Quoted text\""}

def reformat_quote(quote):
    """
    Reformat the quote according to the given rules.
    If the quote doesn't meet the criteria, return None.
    """
    if re.search(r'http[s]?://', quote):
        return None

    match = re.match(r'^(.*?)(?:\s*-\s*|\s*-\s*@)([a-zA-Z0-9_]+)(?:\s+to\s+@\w+)?$', quote)
    if not match:
        return None

    quote_text, username = match.groups()
    return f"{username}: {quote_text.strip()}"

def main():
    # Load the JSON data from the file
    input_file_path = 'cleaned_data/quotes.json'
    output_file_path = 'final_data/quotes.jsonl'

    with open(input_file_path, 'r') as f:
        quotes_data = json.load(f)

    reformatted_quotes = []

    for quote_entry in quotes_data:
        content = quote_entry['content']
        reformatted = reformat_quote(content)
        if reformatted:
            reformatted_quotes.append({"text": reformatted})

    # Save the reformatted quotes to a JSONL file
    with open(output_file_path, 'w') as f:
        for item in reformatted_quotes:
            f.write(json.dumps(item) + '\n')

if __name__ == "__main__":
    main()
