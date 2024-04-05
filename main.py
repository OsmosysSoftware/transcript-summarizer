import openai
import os
import datetime
from dotenv import load_dotenv

# Load .env file
load_dotenv()

# Initialize OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

###-------------Functions declared here-------------###

### Function to chunk file so that it is within token limit of gpt-3.5
def chunk_file(input_folder_path, filename, chunk_size):
    print(f'\n-----------------------\nUsing data from {filename}\n-----------------------\n')
    input_file = os.path.join(input_folder_path, filename)
    with open(input_file, 'r') as file:
        lines = file.readlines()
        total_lines = len(lines)
        num_chunks = total_lines // chunk_size
        if total_lines % chunk_size != 0:
            num_chunks += 1

        for i in range(num_chunks):
            start_index = i * chunk_size
            end_index = min((i + 1) * chunk_size, total_lines)
            chunk = lines[start_index:end_index]
            yield chunk

### function to remove extensions from filename
def remove_extension(filename):
    # Split the filename into its base name and extension
    base_name, extension = os.path.splitext(filename)
    # Return only the base name
    return base_name

### Function to create output file
def create_output_file(output_folder, filename, response):
    # Create the directory if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Get the current date and time & format as a string
    current_time = datetime.datetime.now()
    formatted_time = current_time.strftime("%H%M%S")

    # Create output file
    outputFileName = f"{formatted_time}_{filename}.txt"
    file_path = os.path.join(output_folder, outputFileName)

    # write data in new file
    with open(file_path, "w") as outputFile:
        outputFile.writelines(response)
        print(f"=======================\nResponse saved in {file_path}\n=======================\n")

### Function that generates minutes of meeting using transcript snippets
def summarize_meeting_using_chatbot(context):
    # Get the current date and time
    current_time = datetime.datetime.now()

    # Format the current time as a string
    formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")

    message_template =f"""
      Act as a meeting note taker. I have a transcript of a teams meeting as follows: {context}

      I want a summary of the transcript in the following format:

      # Meeting Minutes
      Give appropriate discussion heading
      Created on: {formatted_time}
      Duration: Set as last recorded response end time and format it as hh:mm:ss

      # Participants
      Display list of participants involved

      # Agenda
      Brief summary what the meeting was about in max 3 points

      # Discussion
      Give the main disucssion points and the speaker names. Give answer in points. Be as descriptive as possible.

      # Action items
      Give what was the outcome, tasks assigned, end result if any of the discussion in points
    """

    chat = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "user",
                "content": message_template
            }
        ]
    )
    reply = chat.choices[0].message.content
    print(f"ChatGPT:\n{reply}")
    return reply

###-------------Main starts here-------------###

def main():
    # Initialize input and output folders
    input_folder_path = os.getenv("INPUT_PATH")
    output_folder_path = os.getenv("OUTPUT_PATH")

    # Get Filename set input folder to create meeting minutes of
    filename = 'sample-site-creation.txt'
    no_ext_filename = remove_extension(filename)

    # Get the current date and time & format as a string
    current_time = datetime.datetime.now()
    formatted_time = current_time.strftime("%Y%m%d")

    # Variables for assigning chunk data
    chunk_size = 930
    output_chunk_folder_path = os.path.join(output_folder_path, f"{formatted_time}_{no_ext_filename}_output")
    output_files_prefix = "_output_chunk_"

    # Call the bot for a response by giving chunks of input of and store it in an output file
    for i, chunk in enumerate(chunk_file(input_folder_path, filename, chunk_size)):
        print(f"------------- Evaluating chunk {i + 1} -------------")
        output_file_name = f"{no_ext_filename}{output_files_prefix}{i+1}"
        chatgpt_reply = summarize_meeting_using_chatbot(chunk)
        create_output_file(output_chunk_folder_path, output_file_name, chatgpt_reply)

if __name__ == "__main__":
    main()