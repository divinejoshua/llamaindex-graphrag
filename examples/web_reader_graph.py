import os
from llama_index.core import StorageContext, load_index_from_storage
from llama_index.core.indices import PropertyGraphIndex
from llama_index.readers.web import SimpleWebPageReader
from decouple import config

# Configurations
os.environ['OPENAI_API_KEY'] = config('OPENAI_API_KEY')


storage_dir = "../graph_store"

# Load documents and build index
documents = SimpleWebPageReader(html_to_text=True).load_data(
    ["https://en.wikipedia.org/wiki/The_World%27s_Billionaires"]
)
# create and Store the date in the Graph store 
index = PropertyGraphIndex.from_documents(documents)
index.storage_context.persist(storage_dir)

# Load the data from the vector store
storage_context = StorageContext.from_defaults(persist_dir=storage_dir)
index = load_index_from_storage(storage_context)

# Chat with the data
query_engine = index.as_query_engine()
response = query_engine.query("Who's name appear on the list the most?")
print(response)