from PIL import Image
import numpy as np
import os

def ft_load(path: str) -> np.ndarray:
	"""Loads an image, prints its shape and pixel data. Returns the pixel array."""
	if not os.path.isfile(path):
		print("Error: File not found.")
		return None

	try:
		with Image.open(path) as img:
			if img.format not in ['JPEG', 'JPG']:
				print("Error: Unsupported image format.")
				return None
			rgb_image = img.convert('RGB')
			img_array = np.array(rgb_image)
			print(f"The shape of image is: {img_array.shape}")
			print(img_array)
			return img_array
	except Exception as e:
		print(f"Error loading image: {e}")
		return None
