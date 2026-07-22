from utils.load_json import load_test_suite
from chains.generator_chain import generator_chain
from chains.judge_chain import judge_chain

questions = load_test_suite()

for item in questions:

    response = generator_chain.invoke(
        {
            "question": item["input"]
        }
    )

    print("=" * 60)
    print("Question:")
    print(item["input"])

    print("\nGemini Answer:")
if isinstance(response.content, list):
    answer = ""

    for block in response.content:
        if isinstance(block, dict):
            answer += block.get("text", "")

else:
    answer = response.content

print(answer)

judge_response = judge_chain.invoke(
    {
        "question": item["input"],
        "answer": answer,
    }
)

print("\nJudge Evaluation:\n")
if isinstance(judge_response.content, list):
    judge_answer = ""

    for block in judge_response.content:
        if isinstance(block, dict):
            judge_answer += block.get("text", "")

    print(judge_answer)

else:
    print(judge_response.content)