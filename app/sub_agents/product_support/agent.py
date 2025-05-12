import os

from agents import Agent
from agents.extensions.models.litellm_model import LitellmModel
from dotenv import load_dotenv

from . import prompts
from .tools.doc_retrieval_tool import retrieve_relevant_doc

load_dotenv()


model_name = os.getenv("MODEL_NAME", "gpt-4o-mini")
model_choice = os.getenv("MODEL_CHOICE", "openai")

if model_choice == "openai":
    model = model_name
else:
    model = LitellmModel(
        model=f"{model_choice}/{model_name}", api_key=os.getenv("GEMINI_API_KEY")
    )

product_support_agent = Agent(
    name="Product Support Agent",
    instructions=prompts.product_support_agent_instr,
    model=model,
    tools=[retrieve_relevant_doc],
    handoff_description="Agent the will answer all of the questions that the user will ask about the product.",
)
