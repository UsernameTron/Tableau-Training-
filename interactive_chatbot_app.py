import streamlit as st
import requests

# Chatbot function
def chatbot_response(user_message):
    # API Details
    api_url = "https://api.x.ai/v1/chat/completions"
    api_key = "xai-Xu7l97WPSOFphMCZ9qtWmwN3JmsdsTC0kgJAlAqyd5HR7c4zinkrEHNIiV6gYhCGTnUWQbdv8bLCNNDb"  
    # Headers for the API request
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }

    # Data payload
    data = {
        "messages": [
            {
                "role": "system",
                "content": "You are a Tableau training assistant. Your role is to provide detailed, step-by-step explanations on how to use Tableau for data visualization, dashboard creation, and data analysis. Keep responses concise and user-friendly."
            },
            {"role": "user", "content": user_message}
        ],
        "model": "grok-beta",
        "temperature": 0.8
    }

    try:
        # Make the API request
        response = requests.post(api_url, headers=headers, json=data)
        response.raise_for_status()  # Check for HTTP errors
        # Extract the chatbot's response
        chatbot_response = response.json()["choices"][0]["message"]["content"]
        return chatbot_response
    except requests.exceptions.RequestException as e:
        return f"API request failed: {e}"

# Streamlit interface
st.title("Interactive Tableau Training App")
st.write("""Welcome to the Interactive Tableau Training App!  
Here, you'll learn Tableau basics, explore dashboards, and gain the skills needed to create your own visualizations.
""")

# Input field for user message
user_message = st.text_input("Ask your Tableau question here:")

# Call the chatbot function when the user provides a message
if user_message:
    response = chatbot_response(user_message)  # Call the chatbot_response function
    st.write(f"Chatbot Response: {response}")
