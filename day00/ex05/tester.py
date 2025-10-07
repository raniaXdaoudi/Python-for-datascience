import subprocess

def run_test(args, expected_contains):
    print(f"▶ Test: python building.py {args}")
    try:
        result = subprocess.run(
            ["python3", "building.py"] + args,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        output = result.stdout.strip()
        if any(expected in output for expected in expected_contains):
            print("Passed\n")
        else:
            print("Failed")
            print("Output:")
            print(output)
            print("Expected contains:")
            print(expected_contains)
            print()
    except Exception as e:
        print(f"Exception occurred: {e}")


# TEST
run_test([], ["What is the text to count?"])
run_test(["Hello World!"], ["The text contains", "upper", "lower"])
run_test(["123"], ["digits"])
run_test(["!@# ?"], ["punctuation", "spaces"])
run_test(["AaBbCc"], ["6 characters", "3 upper", "3 lower"])
run_test([""], ["0 characters"])
run_test(["Hello", "World"], ["AssertionError"])

run_test(["Hi!", "Extra"], ["AssertionError: more than one argument"])
