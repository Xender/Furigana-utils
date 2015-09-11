#!/usr/bin/env python3

import sys

from markup_processor import furiganize
from helpers import stripped_and_empty_lines_collapsed
from formatters.html import HtmlFormat


out_format = HtmlFormat


def main():
	print(out_format.header)

	for line in stripped_and_empty_lines_collapsed(sys.stdin):
		if line == '':
			print(out_format.new_paragraph)
		elif line == '~':
			print(out_format.page_separator)
		else:
			print(furiganize(line, out_format.ruby_formatter), end=out_format.new_line)

	print(out_format.footer)


if __name__ == '__main__':
	main()
