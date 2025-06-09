

import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables
load_dotenv()

# Configure the API key
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Correctly specify the model (Gemini 1.5 models are in "models/" path)
model = genai.GenerativeModel(model_name="models/gemini-1.5-flash")

def generate_reply(prompt):
    """Generates a text reply using Gemini 1.5 Flash."""
    response = model.generate_content(prompt)
    return response.text


