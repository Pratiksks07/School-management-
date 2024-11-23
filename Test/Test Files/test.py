from PIL import Image, ImageOps

# Load the image
input_path = "C://Users//LENOVO//Desktop//questionbank.jpg"
output_path = "C://Users//LENOVO//Desktop//questionbank1.jpg"
image = Image.open(input_path)

# Change the background color to #8AA3F6
bg_color = "#8AA3F6"
image_with_bg = ImageOps.expand(image, border=0, fill=bg_color)

# Save the updated image
image_with_bg.save(output_path)
output_path