import streamlit as st
import speech_recognition as sr
from googletrans import Translator
from gtts import gTTS
import tempfile

# Initialize session state for history
if 'history' not in st.session_state:
    st.session_state.history = []

# App Title and Description
st.title("🌍 Ultimate Speech & Text Translator")
st.write("Translate spoken or written text from any language to any language!")

# Initialize recognizer and translator
recognizer = sr.Recognizer()
translator = Translator()

# Language options
lang_map = {
    "Auto Detect": "auto",
    "English": "en",
    "Hindi": "hi",
    "Spanish": "es",
    "French": "fr",
    "Telugu": "te",
    "Tamil": "ta",
    "German": "de",
    "Chinese (Simplified)": "zh-cn",
    "Arabic": "ar",
    "Russian": "ru",
    "Japanese": "ja",
    "Korean": "ko"
}

# Language selection
source_lang_name = st.selectbox("🗣️ Select source language:", list(lang_map.keys()))
target_lang_name = st.selectbox("🎯 Select target language:", list(lang_map.keys())[1:])  # Exclude "Auto Detect" from target

source_lang = lang_map[source_lang_name]
target_lang = lang_map[target_lang_name]

st.markdown("### 📌 Choose Input Method")

input_method = st.radio("How would you like to input text?", ("🎙️ Speak", "⌨️ Type"))

# 🔒 Always define input_text to prevent NameError
input_text = ""

# Handle input
if input_method == "🎙️ Speak":
    if st.button("Start Recording"):
        with sr.Microphone() as source:
            st.info("🎤 Listening... Speak now!")
            try:
                audio = recognizer.listen(source, timeout=5)
                st.write("🔠 Converting speech to text...")
                input_text = recognizer.recognize_google(audio, language=source_lang if source_lang != "auto" else "en")
                st.success(f"🗣️ You said: {input_text}")
            except sr.WaitTimeoutError:
                st.error("⏱️ Listening timed out. Please try again.")
            except sr.UnknownValueError:
                st.error("❌ Could not understand your voice. Try again.")
            except sr.RequestError:
                st.error("❌ Network error. Please check your connection.")
            except Exception as e:
                st.error(f"Unexpected error: {e}")
else:
    input_text = st.text_area("✍️ Type something to translate:")

# Translate and Output
if input_text.strip():
    st.write("🌐 Translating...")

    try:
        translated = translator.translate(input_text, src=source_lang, dest=target_lang)
        st.success(f"📝 Translation ({target_lang_name}): {translated.text}")

        # Save to history
        st.session_state.history.append({
            "from": source_lang_name,
            "to": target_lang_name,
            "input": input_text,
            "output": translated.text
        })

        # Text-to-speech
        tts = gTTS(translated.text, lang=target_lang)
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as fp:
            tts.save(fp.name)
            st.audio(fp.name, format='audio/mp3')

    except Exception as e:
        st.error(f"Translation error: {e}")

# Show translation history
if st.session_state.history:
    st.markdown("---")
    st.markdown("## 📜 Translation History (Last 5)")
    for idx, entry in enumerate(reversed(st.session_state.history[-5:]), 1):
        st.markdown(f"**{idx}.** {entry['from']} → {entry['to']}<br>"
                    f"🗣️ *{entry['input']}*<br>"
                    f"📝 **{entry['output']}**", unsafe_allow_html=True)
