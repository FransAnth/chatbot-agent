import asyncio
from dataclasses import dataclass

import cv2
from agents import GuardrailFunctionOutput, RunContextWrapper, input_guardrail


@input_guardrail
def image_quality_guardrail(wrapper, agent, user_input):
    if wrapper and wrapper.context:
        image_path = wrapper.context.image_path
        if image_path != None:
            is_blurry, message = is_image_blurry(image_path)
        else:
            # No image to check, continue the conversation
            is_blurry = False
            message = ""

        return GuardrailFunctionOutput(
            output_info=message, tripwire_triggered=is_blurry
        )


def is_image_blurry(image_path):
    """Checks if the image is blurry."""
    threshold = 400.0
    try:
        img = cv2.imread(image_path)
        if img is None:
            return True, "Error: Could not open or find the image at '{image_path}'"

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        laplacian = cv2.Laplacian(gray, cv2.CV_64F)
        variance = laplacian.var()

        if variance < threshold:
            return True, "Image is blurry"
        else:
            return False, "Image is not blurry"

    except Exception as e:
        return False, f"An error occured: {e}"
