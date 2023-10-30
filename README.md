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

This model is being trained and tested with [Axlotl](https://github.com/OpenAccess-AI-Collective/axolotl).

[Runpod Docker Template](https://runpod.io/gsc?template=v2ickqhz9s&ref=6i7fkpdz)

Start the container

Download your dataset and config file inside the container.

Start the fine-tune: `accelerate launch -m axolotl.cli.train qLora.yml`

Login to HuggingFace: `huggingface-cli login`

Push model to HuggingFace: `python merge_peft.py --base_model=mistralai/Mistral-7B-v0.1 --peft_model=./qlora-out --hub_id=Zetaphor/Neolandtest`

## Quantizing/GGUF

```sh
git clone https://github.com/ggerganov/llama.cpp.git
pip install -r llama.cpp/requirements.txt
cd llama.cpp
make CUBLAS=1 # Build llama.cpp binaries
mv Neolandtest llama.cpp/models # Move the merged models into the llama.cpp models folder
# python llama.cpp/convert.py Neolandtest --outfile Neolandtest.gguf --outtype q8_0 # Optional 8-bit quantization
python3 convert.py ./models/Neolandtest/ # F32 quantization and convert to GGUF
./quantize models/Neolandtest.gguf models/quantized_q5_K_M.gguf q5_K_M # 5-bit quantization
# Modify hf_upload and run again for new file
```

## Disclaimer

This probably violates the Discord TOS. Use this responsibly and make sure you have the consent of both the admins and the community that you intend to scrape data and train from.

This is a fun project that was done with the consent of the people involved, and is intended to only be used within that private server. Don't be a dick and use this on a large public server where it's practically impossible to get consent.