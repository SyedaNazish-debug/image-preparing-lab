from PIL import Image

from image_processor import (
    calculate_megapixels,
    calculate_scale,
    crop_image,
    resize_to_target,
    validate_crop_coordinates,
)

def test_calculate_megapixels():
    assert round(calculate_megapixels(2036, 1184), 2) == 2.41


def test_calculate_scale():
    scale = calculate_scale(2036, 1184, 5.0)

    assert round(scale, 3) == 1.440


def test_resize_to_target():
    image = Image.new("RGB", (2036, 1184))

    resized, scale = resize_to_target(image, 5.0)

    width, height = resized.size

    assert width == 2933
    assert height == 1706
    assert round(scale, 3) == 1.440

    final_mp = (width * height) / 1_000_000

    assert final_mp >= 5.0
def test_crop_image():
    image = Image.new("RGB", (2036, 1184))

    cropped = crop_image(
        image,
        0,
        185,
        2036,
        1000,
    )

    assert cropped.size == (2036, 815)
    
def test_validate_crop_coordinates_valid():
    assert validate_crop_coordinates(
        0,
        185,
        2036,
        1000,
        2036,
        1184,
    )

def test_validate_crop_coordinates_invalid_order():
    assert not validate_crop_coordinates(
        1000,
        185,
        500,
        1000,
        2036,
        1184,
    )

def test_validate_crop_coordinates_outside_image():
    assert not validate_crop_coordinates(
        0,
        0,
        2500,
        1000,
        2036,
        1184,
    )

def test_validate_crop_coordinates_negative():
    assert not validate_crop_coordinates(
        -10,
        0,
        1000,
        1000,
        2036,
        1184,
    )