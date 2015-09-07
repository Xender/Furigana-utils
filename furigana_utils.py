#!/usr/bin/env python3

import sys

import tokenizer


def main():
	for line in sys.stdin:
		print(list(tokenizer.tokenize(line)))


if __name__ == '__main__':
	main()
