import os

from agents import Agent, InputGuardrail
from agents.extensions.models.litellm_model import LitellmModel
from dotenv import load_dotenv

from . import prompts
from .tools.text_extraction_tool import extract_text

load_dotenv()

model_name = os.getenv("MODEL_NAME", "gpt-4o-mini")
model_choice = os.getenv("MODEL_CHOICE", "openai")

if model_choice == "openai":
    model = model_name
else:
    model = LitellmModel(
        model=f"{model_choice}/{model_name}", api_key=os.getenv("GEMINI_API_KEY")
    )

image_processing_agent = Agent(
    name="Image Processing Agent",
    instructions=prompts.image_processing_agent_instr,
    model=model,
    tools=[extract_text],
    handoff_description="Agent specialized for extracting key information from images attached by the user.",
)
