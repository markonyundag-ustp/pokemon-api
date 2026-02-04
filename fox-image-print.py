import requests
from PIL import Image
import io

# 1. Get the JSON data first
api_url = "http://randomfox.ca/floof"
response = requests.get(api_url)

if response.status_code == 200:
    # Convert the response text into a Python dictionary
    data = response.json()
    actual_image_url = data['image']  # Extract the real image URL

    print(f"Downloading image from: {actual_image_url}")

    # 2. Now download the actual image bytes
    img_response = requests.get(actual_image_url)

    try:
        image_data = io.BytesIO(img_response.content)
        img = Image.open(image_data)
        img.show()  # This will open the fox image!
    except IOError:
        print("Error: The data retrieved is not a valid image.")
else:
    print(f"Error: Failed to reach API. Status code: {response.status_code}")