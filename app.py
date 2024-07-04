import warnings

from langchain_community.vectorstores import Chroma
from generic_html_parser import extract_table_rows, extract_other_elements
from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings

warnings.filterwarnings('ignore')
_ = load_dotenv()

# filename = "./docs/sales.html"
filename = "./docs/nvidia_financial_results_q1_fiscal_2025.html"

""" extract the table rows and other elements from the html file"""

table_rows = extract_table_rows(filename)

other_elements = extract_other_elements(filename)


""" add the table rows and other elements to the documents list"""
documents = table_rows + other_elements

embeddings = OpenAIEmbeddings()

vectorstore = Chroma.from_documents(documents, embeddings)

# query = "$26,044"
query = "quarterly cash dividend"

retriever = vectorstore.as_retriever()

result = retriever.invoke(query, k=4)

print(result)
