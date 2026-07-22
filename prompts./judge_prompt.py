from langchain_core.prompts import ChatPromptTemplate

judge_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """You are an expert evaluator.

Evaluate the AI answer based on:
1. Correctness (0-10)
2. Completeness (0-10)
3. Clarity (0-10)

Finally provide short feedback.

Return your response in this format:

Correctness: X/10
Completeness: X/10
Clarity: X/10

Feedback:
<your feedback>
"""
        ),

        (
            "human",
            """Question:
{question}

Answer:
{answer}
"""
        )
    ]
)