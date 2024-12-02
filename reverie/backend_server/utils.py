import os

proxy = ""
os.environ["http_proxy"] = proxy
os.environ["https_proxy"] = proxy

# Copy and paste your OpenAI API Key
# use Grok API
openai_api_key = "xai-dHOWkj742Q85Zp5gexXOHRu32WkqzaFssq9U9R0iypqN3kVdEcSZ4jC7s48ioIostmUcGo5nDbVLkIIx"
# Put your name
key_owner = "" 

# OpenAI API Key for embedding
embedding_openai_api_key = "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"

maze_assets_loc = "../../environment/frontend_server/static_dirs/assets"
env_matrix = f"{maze_assets_loc}/the_ville/matrix"
env_visuals = f"{maze_assets_loc}/the_ville/visuals"

fs_storage = "../../environment/frontend_server/storage"
fs_temp_storage = "../../environment/frontend_server/temp_storage"

collision_block_id = "32125"

# Verbose 
debug = True