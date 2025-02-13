from PIL import Image
import os

# Open the PGM file
pgm_path = "/home/atharvahude/maps/apartment.pgm"  # Replace with your actual file name
pgm_image = Image.open(pgm_path)

# Change extension to .png while keeping the same name
png_path = os.path.splitext(pgm_path)[0] + ".png"

# Save as PNG
pgm_image.save(png_path)

print(f"Converted {pgm_path} to {png_path}")
