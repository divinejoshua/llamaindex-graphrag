import os

from llama_index.core import SummaryIndex
from llama_index.readers.web import SimpleWebPageReader
from decouple import config

# Configurations
os.environ['OPENAI_API_KEY'] = config('OPENAI_API_KEY')


storage_dir = "../graph_store"

# Load documents and build index
documents = SimpleWebPageReader(html_to_text=True).load_data(
    ["https://en.wikipedia.org/wiki/The_World%27s_Billionaires"]
)

index = SummaryIndex.from_documents(documents)

# Chat with the data
query_engine = index.as_query_engine()
response = query_engine.query("Who's name appear on the list the most?")
print(response)