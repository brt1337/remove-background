from io import BytesIO
import streamlit as st
from PIL import Image
from rembg import remove

st.set_page_config(layout="wide", page_title="Remover Fundo")

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 

st.write("## Remova o fundo da sua imagem")
st.write(
    ":dog: Tente fazer upload de uma imagem para ver o plano de fundo removido magicamente. Imagens de qualidade total podem ser baixadas na barra lateral. Este código é open source e está disponível aqui no GitHub. Agradecimentos especiais à biblioteca [rembg library](<https://github.com/danielgatis/rembg>) :grin:"
)
st.sidebar.write("## Upload e download :gear:")

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
    col1.write("Imagem Original :camera:")
    col1.image(image)

    fixed = remove(image)
    col2.write("Fundo removido :wrench:")
    col2.image(fixed)
    st.sidebar.markdown("\n")
    st.sidebar.download_button(
        "Download image", convert_image(fixed), "fixed.png", "image/png"
    )

# Create the file uploader
my_upload = st.sidebar.file_uploader("Upload Imagem", 
                                     type=["png", "jpg", "jpeg"],
                                     accept_multiple_files=False,
                                     )

# Fix the image!
if my_upload is not None:
    fix_image(upload=my_upload)
else:
    fix_image("./mbappe-psg.jpg")


