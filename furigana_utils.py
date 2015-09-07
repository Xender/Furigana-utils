#!/usr/bin/env python3

import sys
# import unicodedata

import tokenizer


# def _unicode_name(char):
# 	# Python 3.4 derps on this:
# 	#
# 	# In [1]: import unicodedata
# 	# In [2]: unicodedata.name('\n')
# 	# ---------------------------------------------------------------------------
# 	# ValueError                                Traceback (most recent call last)
# 	# <ipython-input-2-98e022c9c3ed> in <module>()
# 	# ----> 1 unicodedata.name('\n')
# 	# ValueError: no such name

# 	try:
# 		return unicodedata.name(char)
# 	except ValueError:
# 		return ''


def main():
	# while True:
	# 	char = sys.stdin.read(1)

	# 	if not char:
	# 		break

	# 	print(repr(char), _unicode_name(char))
	# 	# print(repr(char), end=' ')
	# 	# print(unicodedata.name(char))

	for line in sys.stdin:
		print(list(tokenizer.tokenize(line)))


if __name__ == '__main__':
	main()
