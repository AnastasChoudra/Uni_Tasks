import os
from PIL import Image, ImageDraw

# Conversion factor from cm to pixels (96 dpi)
cm_to_px = 37.795275591

# Dimensions in cm
ppt_width_cm = 33.76
ppt_height_cm = 27.61

image_width_cm = 6.09
image_height_cm = 8.33

dist_bw_arrays_width_cm = 6.19
dist_bw_arrays_height_cm = 6.46

dist_to_perpendicular_line_cm = 3.1
dist_to_horizontal_line_cm = 3.12

edge_to_array1_3_cm = 7.74
edge_to_array2_4_cm = 7.58

# Convert dimensions to pixels
ppt_width_px = int(ppt_width_cm * cm_to_px)
ppt_height_px = int(ppt_height_cm * cm_to_px)

image_width_px = int(image_width_cm * cm_to_px)
image_height_px = int(image_height_cm * cm_to_px)

dist_bw_arrays_width_px = int(dist_bw_arrays_width_cm * cm_to_px)
dist_bw_arrays_height_px = int(dist_bw_arrays_height_cm * cm_to_px)

dist_to_perpendicular_line_px = int(dist_to_perpendicular_line_cm * cm_to_px)
dist_to_horizontal_line_px = int(dist_to_horizontal_line_cm * cm_to_px)

edge_to_array1_3_px = int(edge_to_array1_3_cm * cm_to_px)
edge_to_array2_4_px = int(edge_to_array2_4_cm * cm_to_px)

# Calculate positions of arrays
positions = {
    'array1': (edge_to_array1_3_px, dist_to_horizontal_line_px),
    'array2': (ppt_width_px - edge_to_array2_4_px - image_width_px, dist_to_horizontal_line_px),
    'array3': (edge_to_array1_3_px, ppt_height_px - dist_to_horizontal_line_px - image_height_px),
    'array4': (ppt_width_px - edge_to_array2_4_px - image_width_px, ppt_height_px - dist_to_horizontal_line_px - image_height_px),
}

# File paths
celebrity_images_path = r'C:\Users\Tasos\Desktop\MSc\Placement; PYM0PL2\Maddie Stimuli creation\stimuli\resize_images'
foil_images_path = r'C:\Users\Tasos\Desktop\MSc\Placement; PYM0PL2\Maddie Stimuli creation\stimuli\resize_foils'
output_folder_path = r'C:\Users\Tasos\Desktop\MSc\Placement; PYM0PL2\Maddie Stimuli creation\stimuli'

def main():
    # Prompt user for the initial number (1, 2, or 3)
    initial_number = input("Enter the initial number (1, 2, or 3): ")

    # Prompt user for image names
    celebrity_images = {
        'array1': input("Enter the name of the image for array1 (e.g., germanotta_9.jpg): "),
        'array2': input("Enter the name of the foil image for array2 (e.g., real_00112.jpg): "),
        'array3': input("Enter the name of the image for array3 (e.g., germanotta_7.jpg): "),
        'array4': input("Enter the name of the image for array4 (e.g., germanotta_5.jpg): ")
    }

    # Extract the celebrity name from the image filename
    def extract_celebrity_name(image_name):
        return image_name.split('_')[0]

    celebrity_name = extract_celebrity_name(celebrity_images['array1'])

    # Load images
    loaded_images = {key: Image.open(os.path.join(celebrity_images_path if key != 'array2' 
        else foil_images_path, img)).resize((image_width_px, image_height_px)) for key, img in celebrity_images.items()}

    # Create a blank template
    template = Image.new('RGB', (ppt_width_px, ppt_height_px), (255, 255, 255))
    draw = ImageDraw.Draw(template)

    # Draw the horizontal and perpendicular lines
    draw.line([(ppt_width_px // 2, 0), (ppt_width_px // 2, ppt_height_px)], fill=(0, 0, 0), width=3)  # Perpendicular line
    draw.line([(0, ppt_height_px // 2), (ppt_width_px, ppt_height_px // 2)], fill=(0, 0, 0), width=3)  # Horizontal line

    # Function to rotate images positions clockwise following the foil logic
    def rotate_positions_clockwise(positions, keys_order):
        new_positions = {}
        for i, key in enumerate(keys_order):
            new_positions[key] = positions[keys_order[i - 1]]
        return new_positions

    # Define the order of rotation
    keys_order = ['array2', 'array4', 'array3', 'array1']

    # Function to create an image with current positions
    def create_image_with_positions(template, positions):
        image = template.copy()

        # Overlay images
        for pos, (x, y) in positions.items():
            img = loaded_images[pos]
            centered_x = x + (image_width_px // 2) - (img.width // 2)
            centered_y = y + (image_height_px // 2) - (img.height // 2)
            image.paste(img, (centered_x, centered_y))

        return image

    # Define the mapping for oddball positions
    oddball_mapping = {
        'array1': 'oddball_4',
        'array2': 'oddball_2',
        'array3': 'oddball_3',
        'array4': 'oddball_1'
    }

    # Create images with rotated positions and save them with custom names
    current_positions = positions.copy()
    for i in range(4):
        result_image = create_image_with_positions(template, current_positions)
        output_name = f"{initial_number}_{celebrity_name}_{oddball_mapping[keys_order[i]]}.jpg"
        result_image.save(os.path.join(output_folder_path, output_name))
        current_positions = rotate_positions_clockwise(current_positions, keys_order)

    print("Images saved successfully.")

# Main loop to run the process multiple times
while True:
    main()
    again = input("Do you want to run the process again? (yes/no): ")
    if again.lower() != 'yes':
        break

print("Process completed.")
