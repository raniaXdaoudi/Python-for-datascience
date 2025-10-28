import numpy as np
import matplotlib.pyplot as plt
from load_image import ft_load

def extract_center(image: np.ndarray, size: int = 400) -> np.ndarray:
	height, width, _ = image.shape
	center_y = height // 2
	center_x = width // 2
	half = size // 2
	zoom = image[
		center_y - half:center_y + half,
		center_x - half:center_x + half
	]
	grayscale = zoom[:, :, 0:1]
	print(f"The shape of image is: {grayscale.shape}")
	print(grayscale)
	return grayscale

def manual_transpose(array: np.ndarray) -> np.ndarray:
	h, w, _ = array.shape
	result = np.zeros((w, h), dtype=int)
	for i in range(h):
		for j in range(w):
			result[j][i] = array[i][j][0]
	print(f"New shape after Transpose: {result.shape}")
	print(result)
	return result

def display_image(array: np.ndarray, title: str = "Transposed Image") -> None:
	plt.imshow(array, cmap='gray')
	plt.title(title)
	plt.xlabel("")
	plt.ylabel("")
	plt.xticks(np.arange(0, array.shape[1], 50))
	plt.yticks(np.arange(0, array.shape[0], 50))
	plt.grid(False)
	plt.show()

def main():
	image = ft_load("animal.jpeg")
	if image is None:
		return
	zoomed = extract_center(image)
	transposed = manual_transpose(zoomed)
	display_image(transposed)

if __name__ == "__main__":
	main()
