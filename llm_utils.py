import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()


api_key = os.getenv("GOOGLE_API_KEY")


genai.configure(api_key=api_key)


model = genai.GenerativeModel(model_name="gemini-1.5-pro")


def query_gemini(prompt):
    response = model.generate_content(prompt)
    return response.text
