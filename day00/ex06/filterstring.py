import sys
from ft_filter import ft_filter


def main(argv):
	try:
		assert len(argv) == 3, "the arguments are bad"
		s = argv[1]
		try:
			n = int(argv[2])
		except ValueError:
			raise AssertionError("the arguments are bad")
		words = s.split()
		result = list(ft_filter(lambda w: len(w) > n, words))
		print(result)
	except AssertionError as e:
		print(f"AssertionError: {e}")
		sys.exit(1)

if __name__ == "__main__":
	main(sys.argv)
