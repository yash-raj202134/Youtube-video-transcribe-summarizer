# YouTube Video Transcribe Summarizer

This application utilizes the Google Gemini Pro large language model (LLM) to generate detailed summaries and notes from YouTube video transcripts. The app is designed to process YouTube videos, extract the transcript, and provide a concise summary of the video with important key points.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [License](#license)
- [Contributing](#contributing)
- [Contact](#contact)

## Overview

The YouTube Video Transcribe Summarizer takes a YouTube video URL as input, extracts the transcript, and provides a summary of the video using Google Gemini Pro's LLM. This tool is helpful for users who want to quickly understand the key points of a YouTube video without watching the entire content.

## Features

- **Video Summary**: Generate detailed summaries of YouTube videos based on their transcripts.
- **Key Points Extraction**: Identify and summarize key points from the video.
- **User-Friendly Interface**: Easily input YouTube video URLs and retrieve summaries.

## Prerequisites

- **Python 3.x**: Ensure you have Python 3.x installed.
- **Libraries**: The project requires the following Python libraries:
    - `youtube_transcript_api`: For extracting YouTube video transcripts.
    - `streamlit`: For creating a user-friendly interface.
    - `google-generativeai`: For using Google Gemini Pro's LLM.
    - `python-dotenv`: For managing environment variables.
    - `pathlib`: For handling file paths.

## Installation

1. **Clone the repository**:

    ```bash
    git clone <repository-url>
    ```

2. **Navigate to the project directory**:

    ```bash
    cd youtube-video-transcribe-summarizer
    ```

3. **Install required dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

4. **Configure Google Gemini Pro**: Set up your API access to Google Gemini Pro's LLM.

## Usage

1. **Run the application**:

    ```bash
    streamlit run app.py
    ```

2. **Enter YouTube video URL**: Input the URL of the YouTube video you want to summarize.
3. **Get detailed notes**: Click the "Get Detailed Notes" button to retrieve a summary of the video.
4. **View the summary**: Review the summary and key points provided by the application.

## License

This project is licensed under the Apache-2.0 License.

## Contributing

Contributions are welcome! Please fork this repository and submit pull requests for any features, improvements, or bug fixes.

## Contact

For any inquiries or support, please [contact us](mailto:yashraj3376@gmail.com).

Happy summarizing!
