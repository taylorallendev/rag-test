from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
import env

model = ChatOpenAI(model="gpt-4")
parser = StrOutputParser()

# Prompt Templating
system_template = "Translate the following into {language}:"
prompt_template = ChatPromptTemplate.from_messages(
    [("system", system_template), ("user", "{text}")]
)
chain = prompt_template | model | parser
print(chain.invoke({"language": "italian", "text": "hi"}))

