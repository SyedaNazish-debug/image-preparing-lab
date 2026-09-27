import io
import math

import streamlit as st
from PIL import Image


TARGET_MP = 5.0
JPEG_QUALITY = 95


def calculate_megapixels(width, height):
    return (width * height) / 1_000_000


def calculate_scale(width, height, target_mp):
    pixels = width * height
    return math.sqrt((target_mp * 1_000_000) / pixels)


def resize_to_target(image, target_mp):
    width, height = image.size

    scale = calculate_scale(width, height, target_mp)

    new_width = math.ceil(width * scale)
    new_height = math.ceil(height * scale)

    resized = image.resize(
        (new_width, new_height),
        Image.Resampling.LANCZOS,
    )

    return resized, scale


st.set_page_config(
    page_title="Image Preparing Lab",
    page_icon="🖼️",
    layout="centered",
)

st.title("Image Preparing Lab")

st.write(
    "A small experiment-based tool for preparing images "
    "by checking resolution, scaling, and JPEG compression."
)


uploaded_file = st.file_uploader(
    "Upload an image",
    type=["jpg", "jpeg", "png"],
)


if uploaded_file is not None:

    image = Image.open(uploaded_file)

    width, height = image.size
    megapixels = calculate_megapixels(width, height)

    st.subheader("Original image")

    st.image(image, use_container_width=True)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Width", f"{width}px")

    with col2:
        st.metric("Height", f"{height}px")

    with col3:
        st.metric("Megapixels", f"{megapixels:.2f} MP")


    if megapixels < TARGET_MP:

        resized, scale = resize_to_target(
            image,
            TARGET_MP,
        )

        new_width, new_height = resized.size

        st.info(
            f"The image is below {TARGET_MP:.0f} MP. "
            f"Required scale: {scale:.3f}×"
        )

        st.subheader("Prepared image")

        st.image(resized, use_container_width=True)

        final_mp = calculate_megapixels(
            new_width,
            new_height,
        )

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric("Width", f"{new_width}px")

        with col2:
            st.metric("Height", f"{new_height}px")

        with col3:
            st.metric("Megapixels", f"{final_mp:.2f} MP")


        output = io.BytesIO()

        if resized.mode in ("RGBA", "P"):
            resized = resized.convert("RGB")

        resized.save(
            output,
            format="JPEG",
            quality=JPEG_QUALITY,
        )


        st.download_button(
            label="Download prepared JPEG",
            data=output.getvalue(),
            file_name="prepared_image.jpg",
            mime="image/jpeg",
        )


    else:

        st.success(
            f"This image is already {megapixels:.2f} MP, "
            f"which is above the {TARGET_MP:.0f} MP target."
        )