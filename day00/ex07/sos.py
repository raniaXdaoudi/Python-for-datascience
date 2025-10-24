import  sys

NESTED_MORSE = {
	" ": "/", "A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".",
	"F": "..-.", "G": "--.", "H": "....", "I": "..", "J": ".---", "K": "-.-",
	"L": ".-..", "M": "--", "N": "-.", "O": "---", "P": ".--.", "Q": "--.-",
	"R": ".-.", "S": "...", "T": "-", "U": "..-", "V": "...-", "W": ".--",
	"X": "-..-", "Y": "-.--", "Z": "--..", "1": ".----", "2": "..---",
	"3": "...--", "4": "....-", "5": ".....", "6": "-....", "7": "--...",
	"8": "---..", "9": "----.", "0": "-----"
}


def encrypt(message: str) -> str:
	morse_code = []
	for char in message:
		key = char.upper()
		if key in NESTED_MORSE:
			morse_code.append(NESTED_MORSE[key])
	return ' '.join(morse_code)


def main(argv):
	try:
		assert len(argv) == 2, "the arguments are bad"
		assert all(ch.isalnum() or ch == ' ' for ch in argv[1]), "the arguments are bad"
		print(encrypt(argv[1]))
	except AssertionError as msg:
		print(f'AssertionError: {msg}')
		sys.exit(1)


if __name__ == "__main__":
	main(sys.argv)
