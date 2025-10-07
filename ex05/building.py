import sys
import string
import re


def build_result(stats: tuple) -> str:
	"""
	Builds the final formatted output string from character stats.

	Args:
		stats (tuple): A tuple of integers in the order:
			(total, upper, lower, punctuation, spaces, digits)

	Returns:
		str: A human-readable multiline summary of the character counts.
	"""
	assert len(stats) == 6, "An error occurred"

	result = f"The text contains {stats[0]} characters:\n"
	result += f"{stats[1]} upper letters\n"
	result += f"{stats[2]} lower letters\n"
	result += f"{stats[3]} punctuation marks\n"
	result += f"{stats[4]} spaces\n"
	result += f"{stats[5]} digits"

	return result


def parse_text(text: str) -> tuple:
	"""
	Parses a given text and returns counts of various character types.

	Args:
		text (str): Input string to be analyzed.

	Returns:
		tuple: Counts of (total, upper, lower, punctuation, spaces, digits)
	"""
	characters = len(text)
	uppercase = len(re.findall(r"[A-Z]", text))
	lowercase = len(re.findall(r"[a-z]", text))
	punctuation = len(re.findall(rf"[{re.escape(string.punctuation)}]", text))
	spaces = len(re.findall(r"\s", text))
	digits = len(re.findall(r"\d", text))

	return characters, uppercase, lowercase, punctuation, spaces, digits


def main(argv: list[str]) -> None:
	"""
	Main program logic: handle input and print character statistics.

	Args:
		argv (list[str]): Command-line arguments (from sys.argv)
	"""
	try:
		if len(argv) == 1:
			text = input("What is the text to count?\n")
		else:
			assert len(argv) == 2, (
				"more than one argument is provided"
			)
			text = argv[1]

		stats = parse_text(text)
		print(build_result(stats))

	except AssertionError as err:
		print(f"AssertionError: {err}")
		sys.exit(1)

	except (EOFError, KeyboardInterrupt):
		print("No data provided to input function")
		sys.exit(1)


if __name__ == "__main__":
	main(sys.argv)
