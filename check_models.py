from dotenv import load_dotenv
import os
from google import genai

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GOOGLE_API_KEY")
)

models = list(client.models.list())

for model in models:
    print("=" * 60)
    print("Name:", model.name)

    if hasattr(model, "supported_actions"):
        print("Supported Actions:", model.supported_actions)

    if hasattr(model, "display_name"):
        print("Display Name:", model.display_name)