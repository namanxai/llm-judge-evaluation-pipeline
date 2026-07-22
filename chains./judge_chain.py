from langchain_google_genai import ChatGoogleGenerativeAI

from config.settings import (
    GOOGLE_API_KEY,
    MODEL_NAME,
)

from prompts.judge_prompt import judge_prompt


judge_llm = ChatGoogleGenerativeAI(
    model=MODEL_NAME,
    google_api_key=GOOGLE_API_KEY,
)

judge_chain = judge_prompt | judge_llm