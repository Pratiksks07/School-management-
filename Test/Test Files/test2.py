from PIL import Image, ImageOps

# Load the user's image
image_path = "C:/Users/LENOVO/Desktop/admin_icon.jpg"
image = Image.open(image_path)

# Invert the colors of the image
inverted_image = ImageOps.invert(image)

# Save the inverted image
output_path = "C:/Users/LENOVO/Desktop/admin_icon1.jpg"
inverted_image.save(output_path)
output_path
