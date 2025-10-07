import sys

def whatis(number: int) -> str:
	return "I'm Even." if number % 2 == 0 else "I'm Odd."

def main(argv):
	if len(argv) == 1:
		return

	try:
		assert len(argv) == 2, "more than one argument is provided"
		try:
			num = int(argv[1])
		except ValueError:
			raise AssertionError("argument is not an integer")
		print(whatis(num))

	except AssertionError as msg:
		print(f'AssertionError: {msg}')
		exit(1)

if __name__ == "__main__":
	main(sys.argv)
