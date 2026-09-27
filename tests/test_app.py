from PIL import Image

from image_processor import (
    calculate_megapixels,
    calculate_scale,
    resize_to_target,
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
    