import io

import streamlit as st
from PIL import Image

from image_processor import (
    calculate_megapixels,
    crop_image,
    resize_to_target,
)

TARGET_MP = 5.0
JPEG_QUALITY = 95

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


        st.subheader("Crop image")

    st.write(
        "Adjust the crop coordinates to remove unwanted borders "
        "or overlays before resizing."
    )

    crop_col1, crop_col2 = st.columns(2)

    with crop_col1:
        left = st.number_input(
            "Left",
            min_value=0,
            max_value=width - 1,
            value=0,
            step=1,
        )

        top = st.number_input(
            "Top",
            min_value=0,
            max_value=height - 1,
            value=0,
            step=1,
        )

    with crop_col2:
        right = st.number_input(
            "Right",
            min_value=1,
            max_value=width,
            value=width,
            step=1,
        )

        bottom = st.number_input(
            "Bottom",
            min_value=1,
            max_value=height,
            value=height,
            step=1,
        )

    if left >= right or top >= bottom:

        st.error(
            "Invalid crop area. Make sure Left < Right "
            "and Top < Bottom."
        )

    else:

        cropped = crop_image(
            image,
            left,
            top,
            right,
            bottom,
        )

        cropped_width, cropped_height = cropped.size

        cropped_mp = calculate_megapixels(
            cropped_width,
            cropped_height,
        )

        st.subheader("Cropped image")

        st.image(
            cropped,
            use_container_width=True,
        )

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric(
                "Width",
                f"{cropped_width}px",
            )

        with col2:
            st.metric(
                "Height",
                f"{cropped_height}px",
            )

        with col3:
            st.metric(
                "Megapixels",
                f"{cropped_mp:.2f} MP",
            )


        if cropped_mp < TARGET_MP:

            resized, scale = resize_to_target(
                cropped,
                TARGET_MP,
            )

            new_width, new_height = resized.size

            st.info(
                f"The cropped image is below {TARGET_MP:.0f} MP. "
                f"Required scale: {scale:.3f}×"
            )

            st.subheader("Prepared image")

            st.image(
                resized,
                use_container_width=True,
            )

            final_mp = calculate_megapixels(
                new_width,
                new_height,
            )

            col1, col2, col3 = st.columns(3)

            with col1:
                st.metric(
                    "Width",
                    f"{new_width}px",
                )

            with col2:
                st.metric(
                    "Height",
                    f"{new_height}px",
                )

            with col3:
                st.metric(
                    "Megapixels",
                    f"{final_mp:.2f} MP",
                )

            output = io.BytesIO()

            if resized.mode in ("RGBA", "P"):
                resized = resized.convert("RGB")

            resized.save(
                output,
                format="JPEG",
                quality=JPEG_QUALITY,
            )

            file_size_mb = len(output.getvalue()) / (
                1024 * 1024
            )

            st.metric(
                "JPEG file size",
                f"{file_size_mb:.2f} MB",
            )

            st.download_button(
                label="Download prepared JPEG",
                data=output.getvalue(),
                file_name="prepared_image.jpg",
                mime="image/jpeg",
            )

        else:

            st.success(
                f"The cropped image is already "
                f"{cropped_mp:.2f} MP, which is above "
                f"the {TARGET_MP:.0f} MP target."
            )