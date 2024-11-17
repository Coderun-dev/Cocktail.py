import openai
import streamlit as st
import os

# Set your OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

st.title("AI-Powered Cocktail Recommendation")

# Collect user preferences
spirit = st.selectbox(
    "Do You Have a Preferred Spirit?", 
    ["Vodka", "Gin", "Rum", "Tequila", "Whiskey", "Something Else"]
)

sweetness = st.selectbox(
    "Do You Prefer Sweet, Sour, Bitter, or Balanced Drinks?",
    ["Sweet", "Sour", "Bitter", "Balanced"]
)

flavor_profile = st.selectbox(
    "Do You Enjoy Fruity Flavors or More Herbal and Earthy Notes?",
    ["Fruity", "Herbal/Earthy"]
)

strength = st.selectbox(
    "Are You in the Mood for Something Strong or Lighter?",
    ["Strong", "Lighter"]
)

# Generate a recommendation using OpenAI's GPT
if st.button("Get Cocktail Recommendation"):
    # Construct the prompt for OpenAI
    prompt = (
        f"Suggest a cocktail based on these preferences:\n"
        f"Spirit: {spirit}\n"
        f"Sweetness: {sweetness}\n"
        f"Flavor Profile: {flavor_profile}\n"
        f"Strength: {strength}\n\n"
        f"Provide the name of the cocktail, a brief description, and detailed preparation instructions."
    )

    try:
        # Call OpenAI API
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=200,
            temperature=0.7
        )

        # Extract and display the generated recipe
        recipe = response.choices[0].text.strip()
        st.subheader("Your Custom Cocktail Recommendation")
        st.write(recipe)

    except Exception as e:
        st.error(f"An error occurred: {e}")
