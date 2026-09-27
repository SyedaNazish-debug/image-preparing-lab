# Image Preparing Lab

A small experiment that started with a simple question:
"Why isn't my image being accepted?"

## What started the experiment

I initially thought the issue was file size (MB).
While experimenting, I realized the requirement was about
megapixels (MP), not megabytes.

That led me to explore:

- Image resolution vs file size
- Megapixel calculations
- Image upscaling
- Cropping and recalculating resolution
- LANCZOS resampling
- JPEG compression quality
- Automated testing
- Streamlit deployment

## What the project does

The application allows you to:

1. Upload an image
2. Inspect its dimensions and megapixels
3. Crop unwanted areas
4. Validate crop coordinates
5. Recalculate megapixels after cropping
6. Calculate the required scaling factor
7. Resize images below the target resolution
8. Export the result as a JPEG at quality 95
9. Download the prepared image

## Processing flow

Where will the user upload an image the system will flow the series of operation on img like Cropping it then Validating the Expected format and requirements like Calculate MP (megapixel ) and Resizing the ing to compress based on the intended original img metadata Compress ,
finally it will be ready to Download the img 

## The experiment

The original test image was:

2036 × 1184
≈ 2.41 MP

After cropping:

2036 × 815
≈ 1.66 MP

The cropped image was then scaled to approximately:

3535 × 1415
≈ 5.00 MP

I also compared different JPEG quality settings and found
JPEG quality 95 to be a reasonable balance for this experiment.

## Important lesson

Increasing the number of pixels does not recreate missing
camera detail.

Upscaling creates estimated pixels through interpolation.
It can satisfy a resolution requirement, but it should not be
confused with increasing the original image's genuine detail.

## Tech stack

- Python
- Pillow
- Streamlit
- Pytest
- Git & GitHub

## Project structure

image-preparing-lab/

├── app.py

├── image_processor.py

├── image_experiment.ipynb

├── tests/

│   └── test_app.py

├── requirements.txt

└── .gitignore

## Testing

The project currently has 8 automated tests covering:

- Megapixel calculation
- Scale calculation
- Image resizing
- Image cropping
- Crop-coordinate validation

All tests currently pass.

## Live Demo
<https://image-preparing-lab-74tikgn2nae9zxxg29jnwh.streamlit.app/>

## Status

This is a learning project and is currently deployed as a
working prototype. It is **not a production service**.

The project will continue to evolve as I learn more about
image processing, testing, and application development.

## Why I built it

This project wasn't planned as an application from the beginning.

It started with a simple question about an image upload.

The interesting part was following that question through
experimentation, mistakes, observations, coding, testing,
version control, and finally deployment.

Sometimes a small "why?" is enough to start a project.
