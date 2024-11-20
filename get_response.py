import os
from dotenv import load_dotenv

import google.generativeai as genai

# Loading all environment variables
load_dotenv()

# Fetching the API KEY
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

system_instruction = f"""
You are a macro and micro nutrient counter. Analyze the image, figure out the food items in the image and find out the number of calories,
macros and micro nutrients.
Response should be detailed and should follow the following structure:
Total Calories
Carbohydrates
Proteins
Fats
Fibre
Micronutrient profile
If the user has any additional questions about the food answer them.
                        """
# Setting model to be used
model = genai.GenerativeModel("gemini-1.5-flash",
                             system_instruction=system_instruction)

# starting chat_session
chat_session = model.start_chat()

# Function to convert natural language to SQL
def get_response(input, chat=chat_session):
    response = chat.send_message(input, stream=True)
    for chunk in response:
        yield chunk.text 