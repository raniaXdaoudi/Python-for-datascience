import sys
import time


def ft_tqdm(lst: range) -> None:
	"""
	Custom implementation of tqdm using yield.
	Displays a progress bar as the iterable is consumed.
	"""
	total = len(lst)
	start_time = time.time()
	bar_length = 50

	for i, item in enumerate(lst):
		percent = (i + 1) / total
		filled = int(bar_length * percent)
		bar = "=" * filled + ">" + " " * (bar_length - filled - 1)
		elapsed = time.time() - start_time
		speed = (i + 1) / elapsed if elapsed > 0 else 0

		sys.stdout.write(
			f"\r{int(percent * 100):3d}%|[{bar}]| {i + 1}/{total} "
			f"[{elapsed:05.2f}s<{(total - (i + 1)) / speed if speed > 0 else 0:05.2f}s, "
			f"{speed:05.2f}it/s]"
		)
		sys.stdout.flush()
		yield item

	print()
