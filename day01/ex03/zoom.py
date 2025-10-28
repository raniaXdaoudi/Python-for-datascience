import numpy as np
import matplotlib.pyplot as plt
from load_image import ft_load

def zoom_image(image: np.ndarray, zoom_size: int = 400) -> np.ndarray:
	height, width, _ = image.shape
	center_y = height // 2
	center_x = width // 2
	half_zoom = zoom_size // 2
	zoom_area = image[
		center_y - half_zoom:center_y + half_zoom,
		center_x - half_zoom:center_x + half_zoom
	]
	grayscale = zoom_area[:, :, 0:1]
	print(f"New shape after slicing: {grayscale.shape}")
	print(grayscale)
	return grayscale

def display_image(image: np.ndarray, title: str = "Zoomed Image") -> None:
	plt.imshow(image.squeeze(), cmap='gray')
	plt.title(title)
	plt.xlabel("")
	plt.ylabel("")
	plt.xticks(ticks=range(0, 351, 50))
	plt.yticks(ticks=range(0, 351, 50))
	plt.grid(False)
	plt.show()

def main():
	image = ft_load("animal.jpeg")
	if image is None:
		return
	print(image)
	zoomed = zoom_image(image)
	display_image(zoomed)

if __name__ == "__main__":
	main()
