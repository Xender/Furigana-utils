#!/usr/bin/env python3

import sys

from markup_processor import furiganize
from helpers import stripped_and_empty_lines_collapsed


class TexFormat:
	header = '''\
\\documentclass{article}
\\usepackage{ruby}
\\usepackage{luatexja-fontspec}
\\usepackage{etoolbox}

\\renewcommand{\\rubysize}{0.5}
\\renewcommand{\\rubysep}{-0.2ex}

\\begin{document}
'''

	footer = '\n\\end{document}'

	new_paragraph  = '\\\\'
	new_line       = '\\newline\n'
	page_separator = '{\\raise.17ex\\hbox{$\\scriptstyle\\sim$}}\\pagebreak'

	@staticmethod
	def ruby_formatter(kanjis, kanas):
		ret = ''

		for kanji, kana in zip(kanjis, kanas):
			ret += '\\ruby{' + kanji + '}{' + kana + '}'

		return ret


out_format = TexFormat


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
