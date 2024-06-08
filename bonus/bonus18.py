import streamlit as webcam

from PIL import Image

with webcam.expander("Start Camera"):
    # Starting the camera
    camera_image = webcam.camera_input("Camera")


if camera_image:
    # Create image instance from PIL
    img = Image.open(camera_image)

    # Conversion to grayscale
    gray_img = img.convert("L")

    # Displaying grayscale image
    webcam.image(gray_img)

