
import base64
from io import BytesIO
from PIL import Image

def base64_to_image(base64_string):
    try:
        # Remove the header from the base64 string if it exists
        if ',' in base64_string:
            base64_string = base64_string.split(',')[1]
        
        # Decode the base64 string
        image_data = base64.b64decode(base64_string)
        
        # Create a BytesIO object
        image_buffer = BytesIO(image_data)
        
        # Open the image using PIL
        image = Image.open(image_buffer)
        
        # Convert to RGB if the image is in RGBA mode
        if image.mode == 'RGBA':
            image = image.convert('RGB')
        image.save("output-test.jpg", "JPEG")
        
        # return image
    
    except Exception as e:
        print(f"Error converting base64 to image: {str(e)}")
        return None