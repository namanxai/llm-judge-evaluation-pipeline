from langchain_core.prompts import ChatPromptTemplate

generator_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are an expert AI assistant. Answer the user's question clearly and accurately."
        ),
        (
            "human",
            "{question}"
        )
    ]
)