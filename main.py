import streamlit as st 
from PIL import Image 
import cv2
import numpy

st.title("Image transformation")
st.subheader("Developed by M. Galchenkova")

st.write("This app is to convert your image to grayscale image and into a watercolor sketch.")


camera_image = st.camera_input("Camera")

if camera_image:
    img = Image.open(camera_image)
    gray_img = img.convert("L")
    st.image(gray_img)
    
    cv2_image = numpy.array(img)
    # Convert RGB to BGR
    cv2_image = cv2_image[:, :, ::-1].copy()
    
    original_img = cv2.cvtColor(cv2_image, cv2.COLOR_BGR2RGB)
    watercolour_image = cv2.stylization(original_img, sigma_s=100, sigma_r=0.25)
    st.image(watercolour_image)