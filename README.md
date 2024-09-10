# Video Script Generator

🎬 **Video Script Generator** is a tool designed to create engaging video scripts using AI. Leveraging OpenAI's GPT-3.5-turbo model and Wikipedia's vast knowledge base, this tool generates video titles and scripts based on user inputs. Ideal for content creators looking for a quick way to generate video content ideas and scripts.

![FireShot Capture 228 - main_2 · Streamlit - localhost](https://github.com/user-attachments/assets/6d4da540-c23d-4387-b0f8-8194b83a2ab1)


## Features

- **Generate Engaging Titles**: Get creative and captivating video titles based on your topic.
- **Create Detailed Video Scripts**: Automatically generate scripts with an engaging introduction, informative middle section, and a surprising conclusion.
- **Utilize Wikipedia Data**: Incorporate relevant information from Wikipedia to enhance the script content.
- **Adjust Creativity**: Control the level of creativity in the generated script with a simple slider.

## How It Works

1. **Input**: Provide the video topic, desired duration, and creativity level.
2. **Generate Title**: The tool uses OpenAI to generate a compelling title for the video.
3. **Fetch Wikipedia Data**: Retrieves relevant information from Wikipedia.
4. **Create Script**: Uses the title and Wikipedia data to craft a detailed video script.

## Installation

1. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Set Up API Key**: You need an OpenAI API key to use this tool. You can get one from [OpenAI API Keys](https://platform.openai.com/account/api-keys).

2. **Run the App**:
   ```bash
   streamlit run main_2.py
   ```

3. **Use the App**:
   - Enter your OpenAI API key in the sidebar.
   - Input the video topic, duration, and creativity level.
   - Click "Generate Script" to create your video title and script.

## Code Overview

### `utils_2.py`

Contains the core functionality of the Video Script Generator:
- **`generate_script` Function**: Generates video titles and scripts using OpenAI and Wikipedia.

### `main_2.py`

Provides a Streamlit interface for user interaction:
- **Title and Sidebar**: For user input and API key configuration.
- **Input Fields**: To specify video topic, duration, and creativity.
- **Alerts**: For missing input or API key.
- **Display**: Shows the generated title, script, and Wikipedia search results.
