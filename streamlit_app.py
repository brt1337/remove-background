import streamlit as st
from io import BytesIO
import ssl
ssl._create_default_https_context = ssl._create_stdlib_context
from streamlit_option_menu import option_menu
from pages.youtube_video import Convert_video
from pages.youtube_audio import Convert_audio
from PIL import Image
from rembg import remove
from streamlit_option_menu import option_menu


st.set_page_config(page_title="Home", page_icon="😁", layout="wide",initial_sidebar_state="collapsed")
no_sidebar_style="""
            <style>
                div[data-testid="stSidebarNav"] {display: none;}
                div[data-testid="collapsedControl"] {display: none;}
            </style>
            """
st.markdown(no_sidebar_style,unsafe_allow_html=True)

hide_streamlit_style = """
            <style>
                #MainMenu {visibility: hidden;}
                footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 

with st.sidebar:
    st.button('GitHub')

selected = option_menu(None,["Home","Remove Background Image","Convert Audio Youtube","Convert Video Youtube"],
                       icons=['house','cloud-upload'],
                       menu_icon="cast", default_index=0, orientation="horizontal")

def Home():
    st.title("On this page you can magically download video from youtube, download audio from youtube and remove background from image.")
    st.header("Completely free and open source project. ")


def remove_background():
    st.write("## Remove background from your image")
    st.write(":dog: Upload image to see the background magically removed. :grin:")
    st.write(":camera: The high quality image can be downloaded from the sidebar.")

    # Create the columns
    col1, col2 = st.columns(2)


    # Download the fixed image
    def convert_image(img):
        buf = BytesIO()
        img.save(buf, format="PNG")
        byte_im = buf.getvalue()
        return byte_im

    # Package the transform into a function
    def fix_image(upload):
        image = Image.open(upload)
        col1.write("Original Image :camera:")
        col1.image(image)

        fixed = remove(image)
        col2.write("Background removed :wrench:")
        col2.image(fixed)
        st.markdown("\n")
        st.download_button(
            "Download image", convert_image(fixed), "fixed.png", "image/png"
        )
    st.write("## Upload e download :gear:")
    # Create the file uploader
    my_upload = st.file_uploader("Upload Imagem", 
                                        type=["png", "jpg", "jpeg"],
                                        accept_multiple_files=False,
                                        )

    # Fix the image!
    if my_upload is not None:
        fix_image(upload=my_upload)
    else:
        fix_image("./Dani-Alves.jpg")

if selected  == 'Home':
    Home()

if selected  == 'Remove Background Image':
    remove_background()

if selected  == 'Convert Audio Youtube':
    Convert_audio()

if selected  == 'Convert Video Youtube':
    Convert_video()
