import math

from PIL import Image


def calculate_megapixels(width, height):
    return (width * height) / 1_000_000


def calculate_scale(width, height, target_mp):
    pixels = width * height

    return math.sqrt(
        (target_mp * 1_000_000) / pixels
    )


def resize_to_target(image, target_mp):
    width, height = image.size

    scale = calculate_scale(
        width,
        height,
        target_mp,
    )

    new_width = math.ceil(width * scale)
    new_height = math.ceil(height * scale)

    resized = image.resize(
        (new_width, new_height),
        Image.Resampling.LANCZOS,
    )

    return resized, scale


def crop_image(image, left, top, right, bottom):
    return image.crop((left, top, right, bottom))