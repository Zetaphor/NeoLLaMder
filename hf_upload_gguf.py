from huggingface_hub import HfApi
api = HfApi()

model_id = "Zetaphor/Neolandtest-gguf"
api.create_repo(model_id, exist_ok=True, repo_type="model")
api.upload_file(
    path_or_fileobj="neolandtest.gguf",
    path_in_repo="neolandtest.gguf",
    repo_id=model_id,
)