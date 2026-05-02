from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.6,
    api_key=api_key
)

def generate_restaurant_name(cuisine):

    # Prompt 1: Restaurant name
    prompt1 = PromptTemplate.from_template(
        "I want to open a restaurant for {cuisine} food. Suggest a fancy name. Give only one name."
    )

    name_response = llm.invoke(prompt1.format(cuisine=cuisine))
    restaurant_name = name_response.content.strip()

    # Prompt 2: Menu items
    prompt2 = PromptTemplate.from_template(
        "Suggest only five menu items for {restaurant_name}. Return them separated by commas."
    )

    menu_response = llm.invoke(prompt2.format(restaurant_name=restaurant_name))
    menu_items = menu_response.content.strip().split(",")

    # Clean spaces
    menu_items = [item.strip() for item in menu_items]

    return {
        "restaurant_name": restaurant_name,
        "menu_items": menu_items
    }
