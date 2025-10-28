def slice_me(family: list, start: int, end: int) -> list:
	"""Displays the initial and final shape of a 2D array after slicing."""
	if not isinstance(family, list) or not all(isinstance(row, list) for row in family):
		raise TypeError("family must be a list of lists.")
	if len(family) == 0:
		raise ValueError("family cannot be empty.")
	row_length = len(family[0])
	if any(len(row) != row_length for row in family):
		raise ValueError("Inconsistent row sizes.")
	if not isinstance(start, int) or not isinstance(end, int):
		raise TypeError("start and end must be integers.")

	print(f"My shape is : ({len(family)}, {row_length})")
	sliced = family[start:end]
	print(f"My new shape is : ({len(sliced)}, {row_length})")

	return sliced
