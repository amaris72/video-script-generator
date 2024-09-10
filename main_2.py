import streamlit as st
from utils_2 import generate_script

# Title
st.title("🎬 Video Script Generator")

# Sidebar
with st.sidebar:
    openai_api_key = st.text_input("Enter your OpenAI API key:", type="password")
    # Set hyperlink
    st.markdown("[Get OpenAI API Key](https://platform.openai.com/account/api-keys)")

# Input field: for users to enter the video topic
subject = st.text_input("💡 Enter the video topic")

# Input field hint text
video_length = st.number_input("⏱ Enter the approximate video duration (in minutes)",
                               min_value=0.1, step=0.1)
# min_value: sets the minimum value allowed, step=0.1: sets the step increment for adjusting the duration

# Set the temperature value for LLM
creativity = st.slider("✨ Enter the creativity level for the video script (a lower number means more precise, a higher number means more diverse)",
                       min_value=0.0, max_value=1.0,
                       value=0.2, step=0.1)

# Add submit button
submit = st.button("Generate Script")

# Alert 1: User clicked the "Generate Script" button but did not provide the API key
if submit and not openai_api_key:
    # Set text alert for "user clicked 'Generate Script' button but did not provide API key"
    st.info("Please enter your OpenAI API key")
    st.stop()

# Alert 2: User clicked the "Generate Script" button but did not enter a video topic
if submit and not subject:
    st.info("Please enter the video topic")
    st.stop()

# Alert 3: User clicked the "Generate Script" button but did not set video length greater than 0.1 minutes
if submit and not video_length >= 0.1:
    st.info("Video length needs to be greater than or equal to 0.1 minutes")
    st.stop()

# Actions after all conditions are met
if submit:
    with st.spinner("Generating content, please wait..."): # Loading message after clicking the submit button
        search_result, title, script = generate_script(subject, video_length, creativity, openai_api_key)
    st.success("Video script has been generated!")
    st.subheader("🔥 Title:")
    st.write(title) # title is the AI-generated title
    st.subheader("📝 Video Script:")
    st.write(script)  # script is the AI-generated script
    with st.expander("Wikipedia Search Results 🔍"): # Collapsible component for Wikipedia content
        st.info(search_result)