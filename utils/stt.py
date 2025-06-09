
import asyncio
from deepgram import Deepgram
import os
from dotenv import load_dotenv

load_dotenv()
# Load your Deepgram API key from environment variable or set it here
DEEPGRAM_API_KEY = os.getenv("DEEPGRAM_API_KEY")
if not DEEPGRAM_API_KEY:
    raise ValueError("DEEPGRAM_API_KEY is not set.")
# Initialize the Deepgram SDK
dg_client = Deepgram(DEEPGRAM_API_KEY)

async def transcribe_audio(file_path):
    # Open the audio file
    with open(file_path, 'rb') as audio:
        source = {'buffer': audio, 'mimetype': 'audio/wav'}

        try:
            # Send the audio to Deepgram for transcription
            response = await dg_client.transcription.prerecorded(
                source,
                {'punctuate': True, 'language': 'en'}
            )

            # Extract the transcript text
            transcript = response['results']['channels'][0]['alternatives'][0]['transcript']
            return transcript

        except Exception as e:
            print("Transcription error:", e)
            return "Sorry, I couldn't transcribe the audio."
