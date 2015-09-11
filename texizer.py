#!/usr/bin/env python3

import sys

from markup_processor import furiganize


tex_header = '''\
\\documentclass{article}
\\usepackage{ruby}
\\usepackage{luatexja-fontspec}
\\usepackage{etoolbox}

\\renewcommand{\\rubysize}{0.5}
\\renewcommand{\\rubysep}{-0.2ex}

\\begin{document}
'''

tex_footer = '\n\\end{document}'


def tex_ruby_formatter(kanjis, kanas):
	ret = ''

	for kanji, kana in zip(kanjis, kanas):
		ret += r'\ruby{' + kanji + '}{' + kana + '}'

	return ret


def stripped_and_empty_lines_collapsed(it):
	last_line_empty = False

	for line in it:
		line = line.rstrip('\n')

		if line == '' and last_line_empty:
			continue

		last_line_empty = (line == '')

		yield line


def main():
	print(tex_header)

	for line in stripped_and_empty_lines_collapsed(sys.stdin):
		if line == '':
			print('\\\\')
		elif line == '~':
			print('{\\raise.17ex\\hbox{$\\scriptstyle\\sim$}}\\pagebreak')
		else:
			print(furiganize(line, tex_ruby_formatter), end='\\newline\n')

	print(tex_footer)


if __name__ == '__main__':
	main()
