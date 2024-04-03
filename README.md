# transcript-summarizer
 TranscriptSummarizer is a CLI tool that quickly turns call transcripts into concise meeting minutes, highlighting key points and actions. Ideal for saving time and capturing essential details from any text-based transcript.

## Prerequisites

To run this project, you need to have Python version 3.6 or above installed on your system.
- [Download Python](https://www.python.org/downloads/)
- [Visual Studio Code](https://code.visualstudio.com/)
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

1. Paste your transcript as `your-file-name.txt` in [input folder](./input).

2. Replace the file for which you want meeting minutes in [main function](./main.py).

3. Run the program.
