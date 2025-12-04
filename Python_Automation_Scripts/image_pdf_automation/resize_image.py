from PIL import Image

def resize(path, output, width, height):
    img = Image.open(path)
    img = img.resize((width, height))
    img.save(output)
    print("Image resized successfully!")

# Example
resize("input.jpg", "resized.jpg", 400, 400)
