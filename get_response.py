import streamlit as st

import google.generativeai as genai

def start_chat_session():
    # Fetching the API KEY
    if "GOOGLE_API_KEY" in st.session_state:
        genai.configure(api_key=st.session_state["GOOGLE_API_KEY"])

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

    return chat_session

# Function to convert natural language to SQL
def get_response(input, chat):
    response = chat.send_message(input, stream=True)
    for chunk in response:
        yield chunk.text 