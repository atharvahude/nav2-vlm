from PIL import Image
import matplotlib.pyplot as plt

# Load the provided SLAM-generated map
image_path = "/mnt/data/apartment.png"
img = Image.open(image_path)

# Display the image to analyze the structure
plt.figure(figsize=(5,5))
plt.imshow(img, cmap='gray')
plt.title("SLAM-Generated Map")
plt.axis("on")
plt.show()
