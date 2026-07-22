from langchain_google_genai import ChatGoogleGenerativeAI

from config.settings import (
    GOOGLE_API_KEY,
    MODEL_NAME,
    TEMPERATURE,
)

from prompts.generator_prompt import generator_prompt

llm = ChatGoogleGenerativeAI(
    model=MODEL_NAME,
    google_api_key=GOOGLE_API_KEY,
    temperature=TEMPERATURE,
)

generator_chain = generator_prompt | llm