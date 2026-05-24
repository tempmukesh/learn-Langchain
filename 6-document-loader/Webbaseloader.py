# build on beautifulsoup + request 
# and not support heavy task 
from langchain_community.document_loaders import WebBaseLoader

loader = WebBaseLoader("https://www.flipkart.com/apple-macbook-air-m4-16-gb-256-gb-ssd-macos-sequoia-mc6t4hn-a/p/itm7c1831ce25509")


docs = loader.load()


print(len(docs))

print(docs[0].page_content)
print(docs[0].metadata)

# now asking question by useing of webBaseLoader
# webloadersolution.py 