import base64
import os

import google.generativeai as genai
from agents import RunContextWrapper, function_tool
from dotenv import load_dotenv

from app.sub_agents.image_processing.prompts import text_extraction_prompt

load_dotenv()

API_KEY = os.environ.get("GEMINI_API_KEY")


@function_tool
def extract_text(wrapper: RunContextWrapper):
    """Extracts text from the given image data"""

    image_path = wrapper.context.image_path
    if image_path == None:
        return "No image uploaded."

    with open(image_path, "rb") as image_file:
        image_data = image_file.read()

    contents = [
        {
            "mime_type": "image/png",
            "data": base64.b64encode(image_data).decode("utf-8"),
        },
        text_extraction_prompt,
    ]

    genai.configure(api_key=API_KEY)
    model = genai.GenerativeModel(model_name="gemini-2.0-flash")
    response = model.generate_content(contents)

    return response.text
