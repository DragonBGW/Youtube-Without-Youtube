# 🎬 YouTube Transcript ➜ Detailed Notes Converter

This is a Streamlit web app that extracts the transcript from any public YouTube video and summarizes it into concise, bullet-point notes using **gemini-1.5-flash** (free-tier compatible).

---
## ✨ Features

- ✅ Accepts both long (`youtube.com/watch?v=...`) and short (`youtu.be/...`) YouTube URLs
- ✅ Handles URLs with extra parameters (`?si=...`, `&t=...`)
- ✅ Uses Google Gemini Pro or Gemini Flash API (Free Tier)
- ✅ Streamlit UI with live video thumbnail and notes rendering
- ✅ One-click local or cloud deployment

---

## 🧠 Example Use Case

Paste a YouTube link like:
https://youtu.be/xAt1xcC6qfM


and get a structured summary of the full transcript in seconds.

## 🚀 Local Setup Instructions

### 1. Clone the Repo

bash
git clone https://github.com/your-username/youtube-summary-app.git
cd youtube-summary-app

2. Set Up Virtual Environment
python -m venv venv
source venv/bin/activate         # On Windows: venv\Scripts\activate

3. Install Dependencies
pip install -r requirements.txt

4. Configure Your Gemini API Key
touch .env
GOOGLE_API_KEY=your_gemini_api_key_here

5. Run the App
streamlit run app.py

When the webpage is loaded, the website will look like following ->
<img width="785" alt="image" src="https://github.com/user-attachments/assets/93111d5a-d6a7-40bd-ac3f-7a10b265c513" />

The extracted textual data might look like ->
<img width="805" alt="image" src="https://github.com/user-attachments/assets/668ce039-ead5-479d-91f3-38fb7db14f12" />

