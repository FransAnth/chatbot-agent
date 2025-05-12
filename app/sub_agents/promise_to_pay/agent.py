import os

from agents import Agent
from agents.extensions.models.litellm_model import LitellmModel
from dotenv import load_dotenv

from . import prompt
from .tools.calculator_tool import calculate_total_amount_due
from .tools.data_retrieval_tool import retrieve_user_data

load_dotenv()

model_name = os.getenv("MODEL_NAME", "gpt-4o-mini")
model_choice = os.getenv("MODEL_CHOICE", "openai")

if model_choice == "openai":
    model = model_name
else:
    model = LitellmModel(
        model=f"{model_choice}/{model_name}", api_key=os.getenv("GEMINI_API_KEY")
    )

promise_to_pay_agent = Agent(
    name="PTP Agent",
    instructions=prompt.ptp_agent_instr,
    model=model,
    tools=[calculate_total_amount_due, retrieve_user_data],
    handoff_description="Agent specialized for handling conversations when the user wants to make a promise to pay",
)
