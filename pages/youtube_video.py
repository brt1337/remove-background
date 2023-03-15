import streamlit as st
from pytube import YouTube
from io import BytesIO
from pathlib import Path
import ssl
ssl._create_default_https_context = ssl._create_stdlib_context


st.set_page_config(page_title="Download Video", page_icon="💻", layout="centered")
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            #sidebar {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 

@st.cache_data(show_spinner=False)
def download_video_to_buffer(url):
    buffer = BytesIO()
    youtube_video = YouTube(url)
    video = youtube_video.streams.filter(progressive="True",file_extension="mp4").order_by('resolution').desc()
    video_720p=video[0]
    default_filename = video_720p.default_filename
    video_720p.stream_to_buffer(buffer)
    return default_filename, buffer

def Convert_video():
    st.title("Download video from Youtube")
    url = st.text_input("Insert Youtube URL:")
    if url:
        with st.spinner("Downloading video Stream from Youtube..."):
            default_filename, buffer = download_video_to_buffer(url)
        st.subheader("Title")
        st.write(default_filename)
        title_vid = Path(default_filename).with_suffix(".mp4").name
        st.subheader("Watch the video")
        st.video(buffer, format='video/mpeg')
        st.subheader("Download Video File")
        st.download_button(
            label="Download mp4",
            data=buffer,
            file_name=title_vid,
            mime="video/mpeg")

if __name__ == "__main__":
    Convert_video()
