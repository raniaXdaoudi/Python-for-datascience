import numpy as np
import matplotlib.pyplot as plt

def ft_invert(array: np.ndarray) -> np.ndarray:
	"""Inverts the color of the image received."""
	inverted = 255 - array
	plt.imshow(inverted)
	plt.title("Figure VIII.2: Invert")
	plt.axis("off")
	plt.show()
	return inverted

def ft_red(array: np.ndarray) -> np.ndarray:
	"""Keeps only the red channel of the image."""
	red = array.copy()
	red[:, :, 1] *= 0
	red[:, :, 2] *= 0
	plt.imshow(red)
	plt.title("Figure VIII.3: Red")
	plt.axis("off")
	plt.show()
	return red

def ft_green(array: np.ndarray) -> np.ndarray:
	"""Keeps only the green channel of the image."""
	green = array.copy()
	green[:, :, 0] -= green[:, :, 0]
	green[:, :, 2] -= green[:, :, 2]
	plt.imshow(green)
	plt.title("Figure VIII.4: Green")
	plt.axis("off")
	plt.show()
	return green

def ft_blue(array: np.ndarray) -> np.ndarray:
	"""Keeps only the blue channel of the image."""
	blue = array.copy()
	blue[:, :, 0] = 0
	blue[:, :, 1] = 0
	plt.imshow(blue)
	plt.title("Figure VIII.5: Blue")
	plt.axis("off")
	plt.show()
	return blue

def ft_grey(array: np.ndarray) -> np.ndarray:
	"""Converts the image to grayscale."""
	grey = array.copy()
	avg = (grey[:, :, 0] / 3 + grey[:, :, 1] / 3 + grey[:, :, 2] / 3)
	plt.imshow(avg, cmap='gray')
	plt.title("Figure VIII.6: Grey")
	plt.axis("off")
	plt.show()
	return avg
