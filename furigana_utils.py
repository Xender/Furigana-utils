#!/usr/bin/env python3

import sys

import tokenizer


def main():
	for line in sys.stdin:
		# print(list(tokenizer.tokenize(line)))
		# continue

		for word, type_ in tokenizer.tokenize(line):
			if type_ == 'KANJI':
				kanjis = [kanji for kanji in word]

				kanji_part = '.'.join(kanjis)
				furi_part  = '.' * len(kanjis)

				print('[', kanji_part, '|', furi_part, ']', sep='', end='')

			else:
				print(word, end='')


if __name__ == '__main__':
	main()
