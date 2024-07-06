from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
import warnings
from dotenv import load_dotenv

warnings.filterwarnings('ignore')
_ = load_dotenv()

chain = (
        {"doc": lambda x: x.page_content}
        | ChatPromptTemplate.from_template("Summarize the following document:\n\n{doc}")
        | ChatOpenAI(model="gpt-4o",
                     max_retries=0)
        | StrOutputParser()
)


def summarise_text(text):
    return chain.invoke(text)
