# Video Script Generator

🎬 **Video Script Generator** is a Streamlit-based application designed to help users generate engaging video scripts. Users simply need to input a topic, video duration, and creativity level, and the system will utilize the OpenAI API to automatically generate a video title and script.

Home Page:   
![FireShot Capture 228 - main_2 · Streamlit - localhost](https://github.com/user-attachments/assets/6d4da540-c23d-4387-b0f8-8194b83a2ab1)

Result:
![FireShot Capture 230 - main_1 · Streamlit - localhost](https://github.com/user-attachments/assets/4da58538-cb50-4387-ac0b-cd59c2d4e33a)

## Features

- Users can input video topics, durations, and creativity levels.
- Generates video titles and scripts in a friendly and easy-to-understand format.
- Provides relevant Wikipedia search results as references.

## Tech Stack

- **Frontend**: Streamlit
- **Backend**: LangChain, OpenAI API, Wikipedia API
- **Programming Language**: Python

## Installation and Running

### Prerequisites

Please ensure you have the following software installed:

- Python 3.7+
- pip

### Steps

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/video-script-generator.git
   cd video-script-generator
   ```

2. Install the required Python libraries:
   ```bash
   pip install -r requirements.txt
   ```

3. Open PyCharm and run the utils_2.py 

4. Start the application:
   ```bash
   streamlit run main_2.py
   ```

5. Open the application in your browser, usually at `http://localhost:8501`.

## Usage

1. Enter your OpenAI API key in the sidebar.
2. Input the video topic.
3. Set the video duration (in minutes) and creativity level.
4. Click the "Generate Script" button to view the generated video title and script.

## Example

Input example:
- Topic: "Sora Model"
- Video Duration: 1 minute
- Creativity Level: 0.7

Output example:
- Generated Title
- Generated Video Script
- Related Wikipedia Search Results
