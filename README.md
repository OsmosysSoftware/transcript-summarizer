# transcript-summarizer

TranscriptSummarizer is a CLI tool that quickly turns call transcripts into concise meeting minutes, highlighting key points and actions. Ideal for saving time and capturing essential details from any text-based transcript.

## Prerequisites

To run this project, you need to have Python version 3.6 or above installed on your system.
- [Download Python](https://www.python.org/downloads/)
- [Download Visual Studio Code](https://code.visualstudio.com/)
- [OpenAI Account](https://platform.openai.com/api-keys) for API key
- Transcript from teams meeting

## Setup

1. Use pip to install requirements.txt
    ```shell
    pip install -r requirements.txt
    ```

2. Create a new file `.env`. Copy all data from the [env example](./env-example) and paste it in `.env`.

3. Add your API key to `.env`
    ```shell
    OPENAI_KEY=sk-your-openai-api-key
    ```

## Run

1. Paste the transcript file for which you want meeting minutes in [input folder](./input). Set the name as `your-file-name.txt` .

2. In [main function](./main.py), replace the variable `filename` with the name of your transcript file (set in input folder).

3. Run the program by pressing the run button in VS Code. Alternatively, execute the following command in root directory:

    ```shell
    python -u "./main.py"
    ```
