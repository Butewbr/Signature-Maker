from PIL import Image, ImageDraw, ImageFont

text = input("Write your name: ")

# If you have another font
font_path = "./Calligraphr.ttf"
font_size = 68

# Create a temporary image with a large size
temp_image = Image.new("RGBA", (1000, 1000), "#ffffff00")
draw = ImageDraw.Draw(temp_image)
font = ImageFont.truetype(font_path, font_size)

# Get the size of the rendered text
text_width = int(draw.textlength(text, font=font))

# Create an image with dimensions adjusted to fit the text
image = Image.new("RGBA", (text_width + 20, int(font_size*1.5)), "#ffffff00")
draw = ImageDraw.Draw(image)

# Draw the text on the image
draw.text((10, 10), text, font=font, fill="#000000")

# Save the image
image.save("./rubrica.png")
