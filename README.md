# 🌍 Ultimate Speech & Text Translator

A powerful and easy-to-use Streamlit web app that translates **spoken or written input** into over 10 languages — with **real-time audio output**, translation history, and intuitive UI.

## ✨ Features

* 🎙️ Speech-to-text using your microphone
* ⌨️ Text input for manual typing
* 🌐 Translation between 10+ global languages
* 🔊 Audio output using gTTS (Google Text-to-Speech)
* 🕒 Session-based translation history
* ⚡ Fast, accurate, and user-friendly

## 🧠 Technologies Used

* Python
* Streamlit
* Google Translate (`googletrans`)
* Speech Recognition (`speech_recognition`)
* gTTS (Google Text-to-Speech)
* tempfile (for audio playback)

## 📦 Supported Languages

* English
* Hindi
* Spanish
* French
* Telugu
* Tamil
* German
* Chinese (Simplified)
* Arabic
* Russian
* Japanese
* Korean

## 📂 Folder Structure

```
MultilingualTranslator/
│
├── translator_app.py            # Main Streamlit app file
├── README.md                    # Documentation
└── requirements.txt             # List of dependencies
```

## 🚀 How to Run

1. Install dependencies:

   ```bash
   pip install streamlit speechrecognition googletrans==4.0.0-rc1 gTTS
   ```

2. Run the app:

   ```bash
   streamlit run translator_app.py
   ```

3. Give mic access in the browser when prompted.

## 🖥️ Usage

* **Select source & target languages** from dropdowns.
* **Choose input method**: 🎙️ speak or ⌨️ type.
* **Click "Start Recording"** (for speech) or type your sentence.
* **See translation output + hear audio**.
* **View your last 5 translations** under the history section.

## 🧪 Notes

* Make sure you have a working microphone for speech input.
* You need an active internet connection (for Google APIs).
* To avoid audio issues, use the latest Chrome/Edge browser.

## 👨‍💻 Author

**Shaik Sajith**
📧 [shaiksajith29@gmail.com](mailto:shaiksajith29@gmail.com)
🌐 [GitHub Profile](https://github.com/shaiksajith29)

## 📝 License

This project is open-source under the [MIT License](https://opensource.org/licenses/MIT).
