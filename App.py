import os
import time
from pathlib import Path
import tempfile

import streamlit as st
from dotenv import load_dotenv

from phi.agent import Agent
from phi.model.google import Gemini
from phi.tools.duckduckgo import DuckDuckGo
from google.generativeai import upload_file, get_file
import google.generativeai as genai

# Load local .env for development
load_dotenv()

# 🔑 Get API key (first from Streamlit Secrets, then from local .env)
if "GOOGLE_API_KEY" in st.secrets:
    API_KEY = st.secrets["GOOGLE_API_KEY"]
else:
    API_KEY = os.getenv("GOOGLE_API_KEY")

if not API_KEY:
    st.error("⚠️ GOOGLE_API_KEY is missing! Please add it to Streamlit Secrets.")
else:
    genai.configure(api_key=API_KEY)

# Page config
st.set_page_config(
    page_title="Multimodal AI Agent-Video Summarizer",
    page_icon="🚀",
    layout="wide",
)

st.title("Phidata Video AI Summarizer🎥🕵️")
st.header("Powered by Gemini-2.5-flash")


@st.cache_resource
def initialize_agent():
    return Agent(
        name="Video AI Summarizer",
        model=Gemini(id="gemini-2.5-flash"),
        tools=[DuckDuckGo()],
        markdown=True,
    )


# Initialize the agent
multimodal_Agent = initialize_agent()

# File uploader
video_file = st.file_uploader(
    "Upload a video file", type=['mp4', 'mov', 'avi'], help="Upload a video for AI Analysis"
)

if video_file:
    with tempfile.NamedTemporaryFile(delete=False, suffix='.mp4') as temp_video:
        temp_video.write(video_file.read())
        video_path = temp_video.name

    st.video(video_path, format="video/mp4", start_time=0)

    user_query = st.text_area(
        "What insights are you seeking from this video?",
        placeholder="Ask anything about the video content. The AI Agent will analyze the content and give additional information to you",
        help="Provide specific questions or insights you want from the video"
    )

    if st.button("🔍 Analyze video", key="analyze_video_button"):
        if not user_query:
            st.warning("Please enter a question or insights to analyze the video.")
        else:
            try:
                with st.spinner("Processing video and gathering insights..."):
                    # Upload and process a video file
                    processed_video = upload_file(video_path)
                    while processed_video.state.name == "PROCESSING":
                        time.sleep(1)
                        processed_video = get_file(processed_video.name)

                    # Prompt generation for analysis
                    analysis_prompt = f"""
                        Analyze the uploaded video for content and context.
                        Respond to the following query using video insights and supplementary web research:
                        {user_query}

                        Provide a detailed, user-friendly, and actionable response.
                    """

                    # AI agent processing
                    response = multimodal_Agent.run(analysis_prompt, videos=[processed_video])

                # Display result
                st.subheader("Analysis Result")
                st.markdown(response.content)

            except Exception as error:
                st.error(f"An error occurred during analysis: {error}")
            finally:
                # Clean up temporary video file
                Path(video_path).unlink(missing_ok=True)
else:
    st.info("Upload a video file for analysis")

# Customize text area height
st.markdown(
    """
    <style>
    .stTextArea TextArea {
        height: 100px;
    }
    </style>
    """,
    unsafe_allow_html=True
)
