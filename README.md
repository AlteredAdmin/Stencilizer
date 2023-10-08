# Stencilizer
### Image Stencil Creator

This script allows users to create stencils from their images. It converts an image into black and white based on a given threshold. The areas that are lighter than the threshold turn white, and the darker areas turn black, thus creating a stencil effect. The script also uses a median filter to reduce small noise, resulting in a cleaner stencil output.

## Features

- Convert any image into a stencil.
- Save the stencil with a custom name or at a specified directory.
- Set a custom threshold for the stencil conversion.
- Uses a median filter to reduce noise.

## Prerequisites

Make sure you have the following Python libraries installed:

- `PIL` from the `Pillow` package.

You can install it using pip:

```
pip install Pillow
```

## How to use

1. Clone the repository or download the script.
2. Navigate to the script directory via terminal or command prompt.
3. Run the script using the command:

```
python <script_name>.py
```

4. You will be prompted to enter the path of the image you want to convert.
5. Next, specify the path (and optionally filename) where you'd like to save the stencil.
6. Wait for the script to process the image and create the stencil. The path to the saved stencil will be printed.

### Function Parameters:

- `image_path`: Path to the input image.
- `output_path`: Path to save the stencil image.
- `threshold`: An integer value to differentiate between dark and light regions. The default is 128.

For instance, when using the `create_stencil` function directly:

```python
create_stencil("path_to_input_image.jpg", "path_to_save_stencil.png", 150)
```

Happy stenciling! 🖼️🎨
