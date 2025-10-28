from PIL import Image
import numpy as np
import os

def ft_load(path: str) -> np.ndarray:
	"""Loads an image and returns the pixel array as RGB format."""
	if not os.path.isfile(path):
		print("Error: File not found.")
		return None
	try:
		with Image.open(path) as img:
			if img.format not in ['JPEG', 'JPG']:
				print("Error: Unsupported image format.")
				return None
			rgb_image = img.convert('RGB')
			return np.array(rgb_image)
	except Exception as e:
		print(f"Error loading image: {e}")
		return None
