import streamlit as st
import tensorflow.keras
from PIL import Image, ImageOps
import numpy as np
import time
from send_img import send_img
from img_classifier import our_image_classifier

st.beta_set_page_config(
page_title="Title of the webpage",
layout="centered",
initial_sidebar_state="collapsed",
)

# Just making sure we are not bothered by File Encoding warnings
st.set_option('deprecation.showfileUploaderEncoding', False)


def main():
    menu = ['Home', 'Contact']
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Home":
        # Let's set the title of our awesome web app
        st.title('Title of your Awesome App')
        # Now setting up a header text
        st.subheader("By Your Cool Dev Name")
        # Option to upload an image file with jpg,jpeg or png extensions
        uploaded_file = st.file_uploader("Choose an image...", type=["jpg","png","jpeg"])
        # When the user clicks the predict button
        if st.button("Predict"):
        # If the user uploads an image
            if uploaded_file is not None:
                # Opening our image
                image = Image.open(uploaded_file)
                # Let's see what we got
                st.image(image,use_column_width=True)
                st.write("")
                try:
                    with st.spinner("The magic of our AI has started...."):
                        label = our_image_classifier(image)
                        time.sleep(8)
                    st.success("We predict this image to be: "+label)
                    rating = st.slider("Do you mind rating our service?",1,10)
                except:
                    st.error("We apologize something went wrong 🙇🏽‍♂️")
            else:
                st.error("Can you please upload an image 🙇🏽‍♂️")
    elif choice == "Contact":
        # Let's set the title of our Contact Page
        st.title('Get in touch')
        def display_team(name,path,affiliation="",email=""):
            '''
            Function to display picture,name,affiliation and name of creators
            '''
            team_img = Image.open(path)
            st.image(team_img, width=350, use_column_width=False)
            st.markdown(f"## {name}")
            st.markdown(f"#### {affiliation}")
            st.markdown(f"###### Email {email}")
            st.write("------")
        display_team("Your Awesome Name", "./assets/profile_pic.png","Your Awesome Affliation","hello@youareawesome.com")
if __name__ == "__main__":
    main()
