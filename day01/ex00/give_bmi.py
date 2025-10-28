def give_bmi(height: list[int | float], weight: list[int | float]) -> list[float]:
	"""
	Calculate BMI for each person in the lists.
	Returns a list of BMI values = weight / height²
	"""
	if not isinstance(height, list) or not isinstance(weight, list):
		raise TypeError("Both arguments must be lists.")
	elif len(height) != len(weight):
		raise ValueError("Both lists must be of the same length.")

	bmi_list = []
	for h, w in zip(height, weight):
		if not isinstance(h, (int, float)) or not isinstance(w, (int, float)):
			raise TypeError("All elements must be int or float.")
		if h == 0:
			raise ValueError("Height cannot be zero.")
		bmi = w / (h ** 2)
		bmi_list.append(bmi)

	return bmi_list

def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
	"""
	Return a list of booleans: True if bmi[i] > limit, else False
	"""
	if not isinstance(limit, int):
		raise TypeError("Limit must be an integer.")
	elif not isinstance(bmi, list):
		raise TypeError("BMI must be a list.")

	result = []
	for val in bmi:
		if not isinstance(val, (int, float)):
			raise TypeError("All BMI values must be int or float.")
		result.append(val > limit)
	return result

