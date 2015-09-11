#!/usr/bin/env python3

import re
import sys


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


furigana_re = re.compile(r'\[(.*?)\|(.*?)\]')  # Match "[kanji|kana]" format.

def furigana_re_replacer(match):
	kanjis, kanas = map(
		lambda s: s.split('.'),
		match.groups()
	)

	assert len(kanjis) == len(kanas)

	ret = ''

	for kanji, kana in zip(kanjis, kanas):
		ret += r'\ruby{' + kanji + '}{' + kana + '}'

	return ret

def furiganize(s):
	return furigana_re.sub(furigana_re_replacer, s)


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
			print(furiganize(line), end='\\newline\n')

	print(tex_footer)


if __name__ == '__main__':
	main()
