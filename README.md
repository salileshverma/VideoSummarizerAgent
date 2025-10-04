<img width="2872" height="1456" alt="Screenshot 2025-08-12 at 1 24 23 AM" src="https://github.com/user-attachments/assets/a5c1e98a-7f12-4137-aa0e-b9694175f62a" />
<img width="2782" height="1452" alt="Screenshot 2025-08-12 at 1 43 16 AM" src="https://github.com/user-attachments/assets/50f57fb4-35ef-46c8-9b5d-73ccca843b53" />
<img width="2772" height="1420" alt="Screenshot 2025-08-12 at 1 43 39 AM" src="https://github.com/user-attachments/assets/cec82660-693d-40f9-a68f-cbab1b3c91e2" />

Phidata Video AI Summarizer 🎥🕵️

A Streamlit-based multimodal AI agent that analyzes video content and provides actionable insights. Powered by Gemini 1.5 Flash and web search (DuckDuckGo), this tool lets you upload a video and ask questions about its content.

Features

Upload video files (.mp4, .mov, .avi) for AI-based analysis.

Ask questions about video content and get detailed, user-friendly insights.

Integrates Google Generative AI for video processing.

Supports real-time video processing and web research to enhance responses.

Easy-to-use Streamlit interface with responsive design.

Demo

Installation

Clone the repository:

git clone (https://github.com/salileshverma/VideoSummarizerAgent.git)
cd video-summarizer


Create a virtual environment:

python -m venv .venv
source .venv/bin/activate  # Mac/Linux
.venv\Scripts\activate     # Windows


Install dependencies:

pip install -r requirements.txt


Create a .env file with your Google API key:

GOOGLE_API_KEY=your_google_api_key_here

Usage
streamlit run main.py


Open the Streamlit app in your browser.

Upload a video file (.mp4, .mov, .avi).

Enter a question about the video in the text area.

Click Analyze Video to get AI-generated insights.

Dependencies

Streamlit
 – for the frontend UI

phi-agent
 – AI agent integration

Google Generative AI
 – video analysis

DuckDuckGo search for supplemental web insights

Python 3.10+

Folder Structure
video-summarizer/
│
├─ main.py            # Streamlit app entry point
├─ requirements.txt   # Python dependencies
├─ .env               # API keys
└─ README.md
