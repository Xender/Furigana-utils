#!/usr/bin/env python3

import sys

import tokenizer


def main():
	for line in sys.stdin:
		# print(list(tokenizer.tokenize(line)))
		# continue

		for token in tokenizer.tokenize(line):
			if token[1] == 'KANJI':
				print('[', token[0], '|]', sep='', end='')
			else:
				print(token[0], end='')


if __name__ == '__main__':
	main()
