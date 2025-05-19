import streamlit as st
import wikipedia
import pyjokes
import datetime
import speedtest
from youtube_search_python import VideosSearch
import requests

st.set_page_config(page_title="AI Voice Assistant", layout="centered")

st.title("🤖 AI Voice Assistant (Text-Based Demo)")
st.write("Type a command below:")

command = st.text_input("Your Command:")

if command:
    command = command.lower()

    if 'wikipedia' in command:
        topic = command.replace('wikipedia', '').strip()
        result = wikipedia.summary(topic, sentences=2)
        st.success(f"Wikipedia says:\n{result}")

    elif 'joke' in command:
        joke = pyjokes.get_joke()
        st.success(f"Here's a joke:\n{joke}")

    elif 'time' in command:
        now = datetime.datetime.now().strftime("%H:%M:%S")
        st.success(f"Current time is {now}")

    elif 'youtube' in command:
        query = command.replace('youtube', '').strip()
        results = VideosSearch(query, limit=1).result()
        link = results['result'][0]['link']
        st.markdown(f"[🎬 Watch on YouTube]({link})")

    elif 'internet speed' in command:
        st.info("Testing internet speed...")
        st_spinner = st.spinner("Running speed test...")
        with st_spinner:
            s = speedtest.Speedtest()
            download = round(s.download() / (10**6), 2)
            upload = round(s.upload() / (10**6), 2)
        st.success(f"Download: {download} Mbps | Upload: {upload} Mbps")

    else:
        st.warning("Sorry, I didn’t understand that command.")
