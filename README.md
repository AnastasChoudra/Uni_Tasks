# Oddball Paradigm Stimuli Generator

## Overview
This Python script automates the creation of stimuli for a standard oddball paradigm used in psychology experiments. It arranges images in a 2x2 grid, rotates their positions clockwise, and saves the resulting composite images with descriptive filenames.

## Features
- **Automated Rotation**: Images are rotated clockwise in a 2x2 grid.
- **Customizable Input**: Requires only the image filenames and directory paths.
- **Batch Processing**: Runs multiple times in a loop until manually stopped.
- **Descriptive Filenames**: Outputs images with filenames indicating their position and content.

## Requirements
- Python 3.x
- PIL (Pillow) library for image processing

## How to Use
1. **Install Pillow**: If not already installed, run `pip install pillow`.
2. **Prepare Images**: Ensure your images are in the specified directories.
3. **Run the Script**: Execute `stimuli_creation_code.py`.
4. **Follow Prompts**: Enter the initial number (1, 2, or 3) and the names of the images for each array position.

## Directory Structure
- **Celebrities**: Place celebrity images in `celebrity_images_path`.
- **Foils**: Place foil images in `foil_images_path`.
- **Output**: Generated images are saved in `output_folder_path`.

## Example
```plaintext
Enter the initial number (1, 2, or 3): 1
Enter the name of the image for array1 (e.g., germanotta_9.jpg): germanotta_9.jpg
Enter the name of the foil image for array2 (e.g., real_00112.jpg): real_00112.jpg
Enter the name of the image for array3 (e.g., germanotta_7.jpg): germanotta_7.jpg
Enter the name of the image for array4 (e.g., germanotta_5.jpg): germanotta_5.jpg
