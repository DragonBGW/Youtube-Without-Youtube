import streamlit as st
from dotenv import load_dotenv
import google.generativeai as genai
from youtube_transcript_api import YouTubeTranscriptApi

# ─────────────────────────────── CONFIG ───────────────────────────────
load_dotenv()  # Loads .env file containing GOOGLE_API_KEY
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

MODEL_NAME = "gemini-1.5-flash"  # 🔁 Change to "gemini-1.5-flash", "gemini-1.5-pro", etc.

PROMPT = (
    "You are a YouTube-video summarizer. Summarize the transcript below in clear, "
    "concise bullet points (max 250 words).\n\nTranscript:\n"
)

# ───────────────────────────── HELPERS ────────────────────────────────
def get_video_id(url: str) -> str | None:
    """
    Extract the video ID from either:
    • https://youtu.be/VIDEO_ID?...
    • https://www.youtube.com/watch?v=VIDEO_ID&...
    """
    parsed = urlparse(url)
    if "youtu.be" in parsed.netloc:
        return parsed.path.lstrip("/") or None
    if "youtube.com" in parsed.netloc:
        return parse_qs(parsed.query).get("v", [None])[0]
    return None


def extract_transcript(video_id: str) -> str:
    """Fetch YouTube transcript and combine into single string."""
    segments = YouTubeTranscriptApi.get_transcript(video_id)
    return " ".join(seg["text"] for seg in segments)


def generate_summary(transcript: str) -> str:
    """Use Gemini to summarize transcript."""
    model = genai.GenerativeModel(MODEL_NAME)
    response = model.generate_content(PROMPT + transcript)
    return getattr(response, "text", response.candidates[0].content.parts[0].text)

# ────────────────────────────── UI ────────────────────────────────────
st.set_page_config(layout="wide")
st.title("🎬 YouTube Transcript ➜ Detailed Notes")

yt_url = st.text_input("Paste a YouTube link:")

# Display video thumbnail if valid
video_id = get_video_id(yt_url) if yt_url else None
if video_id:
    st.image(f"https://img.youtube.com/vi/{video_id}/0.jpg", use_container_width=True)

# Button: Get Notes
if st.button("Get Detailed Notes") and video_id:
    with st.spinner("Fetching transcript and generating notes…"):
        try:
            transcript_text = extract_transcript(video_id)
            summary = generate_summary(transcript_text)
            st.subheader("📝 Detailed Notes")
            st.write(summary)
        except Exception as err:
            st.error(f"❌ Failed: {err}")
elif yt_url and not video_id:
    st.warning("⚠️ Invalid YouTube link format.")

