import streamlit as st
import requests
import pandas as pd
import matplotlib.pyplot as plt

# Chatbot function
def chatbot_response(user_message):
    # API Details
    api_url = "https://api.x.ai/v1/chat/completions"
    api_key = "xai-Xu7l97WPSOFphMCZ9qtWmwN3JmsdsTC0kgJAlAqyd5HR7c4zinkrEHNIiV6gYhCGTnUWQbdv8bLCNNDb"  # Replace with your API key

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }
    data = {
        "messages": [
            {"role": "system", "content": "You are a helpful assistant focused on Tableau training and data visualization."},
            {"role": "user", "content": user_message}
        ],
        "model": "grok-beta",
        "temperature": 0.8
    }
    try:
        response = requests.post(api_url, headers=headers, json=data)
        response.raise_for_status()
        return response.json()["choices"][0]["message"]["content"]
    except requests.exceptions.RequestException as e:
        return f"API request failed: {e}"

# Streamlit interface
st.title("Interactive Tableau Training App")
st.write("""
Welcome to the Interactive Tableau Training App!  
Here, you'll learn Tableau basics, explore dashboards, and gain the skills needed to create your own visualizations.
""")

# User message input
user_message = st.text_input("Enter your question about Tableau:")
if user_message:
    response = chatbot_response(user_message)
    st.write(f"Chatbot Response: {response}")

# Add file upload for datasets
st.subheader("Upload Your Dataset")
uploaded_file = st.file_uploader("Upload a dataset (.csv)", type="csv")
if uploaded_file is not None:
    try:
        data = pd.read_csv(uploaded_file)
        st.write("Here's a preview of your uploaded data:")
        st.dataframe(data)
    except Exception as e:
        st.error(f"Error loading file: {e}")

# Provide a sample dataset
st.subheader("Sample Dataset")
st.write("If you don't have a dataset, you can explore this sample dataset:")
sample_data = pd.DataFrame({
    "Category": ["Furniture", "Office Supplies", "Technology"],
    "Sales": [20000, 15000, 30000],
    "Profit": [4000, 3000, 8000],
    "Region": ["East", "West", "Central"]
})
st.dataframe(sample_data)

# Add FAQs for Tableau
st.subheader("Frequently Asked Questions")
faq = st.selectbox(
    "Select a question:",
    [
        "How do I create a calculated field in Tableau?",
        "How do I connect Tableau to Excel?",
        "What is the difference between dimensions and measures?"
    ]
)
if faq:
    st.write(f"You selected: {faq}")
    if faq == "How do I create a calculated field in Tableau?":
        st.write("In Tableau, right-click in the data pane and select 'Create Calculated Field'.")
    elif faq == "How do I connect Tableau to Excel?":
        st.write("In Tableau, click 'Connect', then choose 'Microsoft Excel'. Navigate to your file and open it.")
    elif faq == "What is the difference between dimensions and measures?":
        st.write("Dimensions are qualitative data (e.g., categories), while measures are quantitative data (e.g., numbers).")

# Add Tableau dashboard embed
st.subheader("Explore a Tableau Dashboard")
tableau_dashboard_url = "https://public.tableau.com/views/RegionalSampleWorkbook/Storms?%3Aembed=y&%3AshowShareOptions=false&%3Atoolbar=no&%3Adisplay_count=no&%3AshowVizHome=no#1"  # Corrected Tableau Public URL
st.markdown(
    f'<iframe src="{tableau_dashboard_url}" width="800" height="600"></iframe>',
    unsafe_allow_html=True
)

# Placeholder Tableau Experience
st.subheader("Sample Sales Analysis")
st.write("Here's a quick look at a sample dataset:")

# Display the sample data
sample_data = pd.DataFrame({
    "Category": ["Furniture", "Office Supplies", "Technology"],
    "Sales": [20000, 15000, 30000],
    "Profit": [4000, 3000, 8000],
    "Region": ["East", "West", "Central"]
})
st.dataframe(sample_data)

# Generate a simple bar chart
st.write("Visualizing Sales by Category:")
fig, ax = plt.subplots()
sample_data.plot(kind='bar', x='Category', y='Sales', legend=False, ax=ax)
ax.set_title("Sales by Category")
ax.set_xlabel("Category")
ax.set_ylabel("Sales ($)")
st.pyplot(fig)
