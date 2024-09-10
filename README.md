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

1. **Download the Code Repository**:
   - Open a browser and visit the [Video Script Generator GitHub repository](https://github.com/amaris72/video-script-generator).
   - Click the `Code` button, then select `Download ZIP`, or use the following command to clone the repository:
     ```bash
     git clone https://github.com/amaris72/video-script-generator.git
     ```

2. **Extract and Enter the Project Directory**:
   - If you downloaded the ZIP file, extract it and enter the extracted folder.
   - Use the terminal to navigate to the project directory:
     ```bash
     cd video-script-generator
     ```

3. **Create and Activate a Virtual Environment**:
   - Create a virtual environment:
     ```bash
     python -m venv venv
     ```
   - Activate the virtual environment:
     - On Windows:
       ```bash
       venv\Scripts\activate
       ```
     - On macOS or Linux:
       ```bash
       source venv/bin/activate
       ```

4. **Install Required Python Libraries**:
   - Ensure you are in the virtual environment and run the following command to install the dependencies:
     ```bash
     pip install -r requirements.txt
     ```

5. **Set OpenAI API Key**:
   - Make sure you have a valid OpenAI API key.
   - Set the environment variable in the terminal:
     - On Linux or macOS:
       ```bash
       export OPENAI_API_KEY='your-api-key'
       ```
     - On Windows:
       ```bash
       set OPENAI_API_KEY='your-api-key'
       ```

6. **Start the Application**:
   - Run the following command in the terminal to start the Streamlit app:
     ```bash
     streamlit run main_2.py
     ```

7. **Open the Application in Your Browser**:
   - Open your browser and go to the following address:
     ```
     http://localhost:8501
     ```

## Notes:
- Ensure that step 4 has the `requirements.txt` file present and includes the necessary libraries.
- If you encounter any errors during the running process, check the output in the terminal for debugging hints.

Following these steps, you should be able to successfully set up and run the Video Script Generator application.

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
