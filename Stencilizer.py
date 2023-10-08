from PIL import Image, ImageFilter
import os


def create_stencil(image_path, output_path, threshold=128):
    """
    Create a stencil from an image.

    Parameters:
        - image_path: str, path to the input image.
        - output_path: str, path to save the stencil image.
        - threshold: int, value to differentiate between dark and light regions. Default is 128.
    """
    # Open image
    image = Image.open(image_path)

    # Convert to grayscale
    gray_image = image.convert('L')

    # Apply threshold
    stencil_image = gray_image.point(lambda p: 255 if p > threshold else 0)

    # Optionally, apply a median filter to reduce small noise
    stencil_image = stencil_image.filter(ImageFilter.MedianFilter())

    # If the output_path is a directory, append a default filename
    if os.path.isdir(output_path):
        output_path = os.path.join(output_path, "stencil_output.png")

    # Save the stencil
    stencil_image.save(output_path)
    print(f'Stencil saved to {output_path}')


if __name__ == "__main__":
    input_path = input("Enter the path of the image: ").strip()
    output_path = input("Enter the path to save the stencil (e.g. stencil.png): ").strip()

    # Strip any double quotes from the paths
    input_path = input_path.strip('"')
    output_path = output_path.strip('"')

    create_stencil(input_path, output_path)
