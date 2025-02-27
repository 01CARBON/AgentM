from src.preprocessing.prompt import PROMPT

from google import genai
import pathlib
import PIL.Image
import os

class GeminiAgent:
    """A class to interact with the Gemini API for image content generation."""

    def __init__(self, images: list, api_key_env_var="GEMINI_API_KEY"):
        """
        Initializes the GeminiAgent with the image path and API key.

        Args:
            image_path (str): The path to the image file to be processed.
            api_key_env_var (str): The environment variable name for the API key.
        """
        # Load images
        self.pil_images = images
        self.api_key = os.getenv(api_key_env_var)
        self.client = genai.Client(api_key=self.api_key)

    def generate_image_content(self, model="gemini-2.0-flash-thinking-exp-01-21"):
        """
        Generates content for the image using the Gemini API.

        Returns:
            str: The text response from the Gemini API describing the image.
        """
        
        response = self.client.models.generate_content(
            model=model,
            contents=[PROMPT] + self.pil_images
        )
        return response.text

if __name__ == "__main__":
    # Example usage
    image_paths = ["Sample Images/Screenshot 2025-02-07 102305.png", "Sample Images/Screenshot 2025-02-07 102945.png"]
    agent = GeminiAgent(image_paths)
    response_text = agent.generate_image_content()
    print(response_text)
