from dotenv import load_dotenv
from langchain.schema import HumanMessage, SystemMessage
from langchain_openai import ChatOpenAI

load_dotenv()

with open(
    r"app\sub_agents\product_support\utils\output-files\billease_faq.html",
    "r",
    encoding="utf-8",
) as f:
    html_text = f.read()

system_prompt = """You are a helpful assistant. The user is sending raw HTML content of a FAQ page.
Extract all relevant information, especially questions and answers.

Format the response as:
---
question: <the question>
answer: <the answer>
---

Be thorough and don't skip any content that looks like a FAQ."""

chat = ChatOpenAI(model="gpt-4o", temperature=0)

messages = [SystemMessage(content=system_prompt), HumanMessage(content=html_text)]

response = chat(messages)

with open("/utils/billease_faq.txt", "w", encoding="utf-8") as f:
    f.write(response.content)
