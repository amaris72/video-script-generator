from langchain.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_community.utilities import WikipediaAPIWrapper
import os

def generate_script(subject, video_length, creativity, api_key):
    # Video Title
    title_template = ChatPromptTemplate.from_messages(
        [
            ("human", "Please come up with an engaging title for a video on the topic '{subject}'.")
        ]
    )
    # Video Script
    script_template = ChatPromptTemplate.from_messages(
        [
            ("human",
             """You are a content creator for a short video channel. Based on the following title and related information, write a video script for the channel.
             Video Title: {title}, Video Duration: {duration} minutes. The script length should aim to match the video duration.
             The script should start with a hook, provide valuable content in the middle, and end with a surprise. Format the script as [Introduction, Middle, Conclusion].
             The overall tone should be engaging and fun, appealing to a young audience.
             You can use the following Wikipedia search results as a reference, but only include relevant information and ignore the rest:
             ```{wikipedia_search}```""")
        ]
    )

    # Set OpenAI API key and parameters
    model = ChatOpenAI(model="gpt-3.5-turbo", 
                    openai_api_key = "your-OpenAI-API-key",
                    openai_api_base = "https://api.openai.com/v1",
                    temperature = creativity)
    # temperature = creativity: Defines creativity, the higher the temperature, the more creative the output.

    # Pass prompts to the model
    title_chain = title_template | model
    script_chain = script_template | model

    # Get the video title from AI
    title = title_chain.invoke({"subject": subject}).content

    # Call Wikipedia method: set the language of the results to English
    search = WikipediaAPIWrapper(lang="en")
    # Get Wikipedia search results
    search_result = search.run(subject)

    # Get the video script from AI
    script = script_chain.invoke({"title": title,
                        "duration": video_length,
                        "wikipedia_search": search_result}).content
    return search_result, title, script

print(generate_script("sora model", 1, 0.7, os.getenv("OPENAI_API_KEY")))
