import openai
import streamlit as st

# Access the API key from Streamlit secrets
api_key = st.secrets["api_key"]

# OpenAI API Key
openai.api_key = api_key

st.title("Cocktail Recommendation")

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
        # Call OpenAI API using the updated method
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a helpful assistant that suggests cocktail recipes."},
                {"role": "user", "content": prompt}
            ]
        )

        # Access the message content correctly
        recipe = response.choices[0].message.content.strip()
        st.subheader("Your Custom Cocktail Recommendation")
        st.write(recipe)

    except Exception as e:
        st.error(f"An error occurred: {e}")
