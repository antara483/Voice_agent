
# import asyncio
# from utils.stt import transcribe_audio
# from utils.llm import generate_reply
# from utils.tts import offline_synthesize_audio
# from metrics_logger import log_metrics_to_excel
# from datetime import datetime

# def process_audio(audio_path):
#     # Step 1: STT
#     # text = transcribe_audio(audio_path)
#     # text = asyncio.run(transcribe_audio(audio_file))
#     text = asyncio.run(transcribe_audio(audio_path))


#     print(f"Transcript: {text}")

#     # Step 2: LLM
#     reply = generate_reply(text)
#     print(f"LLM Response: {reply}")

#     # Step 3: TTS
#     # synthesize_audio(reply, "response.wav")  # Save to response.wav
#     # try:
#     #     synthesize_audio(reply, "response.wav")
#     # except Exception as e:
#     #     print("ElevenLabs TTS failed, falling back to offline TTS:", e)
#     #     offline_synthesize_audio(reply, "response.wav")
#     offline_synthesize_audio(reply, "response.wav")
#     # Step 4: Logging
#     metrics = {
#         "timestamp": datetime.now().isoformat(),
#         "transcript": text,
#         "response": reply
#     }
#     log_metrics_to_excel(metrics)
#     print("Metrics logged to: call_logs.xlsx")

#     return "response.wav"


import speech_recognition as sr
from utils.llm import generate_reply
from utils.tts import offline_synthesize_audio
from metrics_logger import log_metrics_to_excel
from datetime import datetime
import pyttsx3

def run_voice_agent():
    recognizer = sr.Recognizer()
    mic = sr.Microphone()
    tts_engine = pyttsx3.init()

    print("🎤 Voice Agent is live. Say something! (Say 'exit' to quit)\n")

    while True:
        try:
            with mic as source:
                print("🔊 Listening...")
                recognizer.adjust_for_ambient_noise(source, duration=0.3)
                audio = recognizer.listen(source)

            # Step 1: STT
            text = recognizer.recognize_google(audio)
            print(f"📝 You said: {text}")

            if text.lower() in ["exit", "quit", "stop"]:
                print("👋 Exiting voice agent.")
                break

            # Step 2: LLM
            reply = generate_reply(text)
            print(f"🤖 Agent: {reply}")

            # Step 3: TTS (offline)
            tts_engine.say(reply)
            tts_engine.runAndWait()

            # Optional: Save response if needed
            # offline_synthesize_audio(reply, "response.wav")

            # Step 4: Logging
            metrics = {
                "timestamp": datetime.now().isoformat(),
                "transcript": text,
                "response": reply
            }
            log_metrics_to_excel(metrics)
            print("📊 Metrics logged to: call_logs.xlsx\n")

        except sr.UnknownValueError:
            print("⚠️ Sorry, I didn't catch that. Please try again.")
        except sr.RequestError as e:
            print(f"⚠️ Could not request results from Google STT; {e}")
        except KeyboardInterrupt:
            print("🛑 Interrupted by user.")
            break
