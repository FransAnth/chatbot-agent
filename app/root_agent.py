import asyncio
import os
from dataclasses import dataclass

from agents import Agent, InputGuardrail, InputGuardrailTripwireTriggered, Runner
from agents.extensions.models.litellm_model import LitellmModel
from dotenv import load_dotenv

from app.sub_agents.image_processing.agent import image_processing_agent
from app.sub_agents.product_support.agent import product_support_agent
from app.sub_agents.promise_to_pay.agent import promise_to_pay_agent

from .guardrails.image_quality_checker import image_quality_guardrail
from .prompts import root_agent_instruction

load_dotenv()

model_name = os.getenv("MODEL_NAME", "gpt-4o-mini")
model_choice = os.getenv("MODEL_CHOICE", "openai")

if model_choice == "openai":
    model = model_name
else:
    model = LitellmModel(
        model=f"{model_choice}/{model_name}", api_key=os.getenv("GEMINI_API_KEY")
    )


@dataclass
class ChatbotContext:
    image_path: str


class ChatbotAgent:
    def __init__(self, image_path):
        self.router_agent = Agent(
            name="Router Agent",
            instructions=root_agent_instruction,
            model=model,
            handoffs=[
                image_processing_agent,
                product_support_agent,
                promise_to_pay_agent,
            ],
            input_guardrails=[image_quality_guardrail],
        )
        self.image_path = image_path

    async def invoke_async(self, query):
        chatbot_context = ChatbotContext(image_path=self.image_path)

        try:
            result = await Runner.run(
                starting_agent=self.router_agent, input=query, context=chatbot_context
            )
            return result.final_output

        except InputGuardrailTripwireTriggered:
            return "It looks like the image you uploaded is a bit blurry. Could you please re-upload a clearer version?"

    def invoke(self, query):
        return asyncio.run(self.invoke_async(query))
