#!/usr/bin/env python3

import re
import sys


html_header = '''\
<!doctype html>
<meta charset="utf-8">

<style>
body {
	font-family: "Kozuka Mincho Pr6N R";
	line-height: 1.7em;
	page-break-inside: avoid;
}

rt {
	font-size: 0.7em;
}

.page-break {
	page-break-after: always;
}
</style>

<p>\
'''


furigana_re = re.compile(r'\[(.*?)\|(.*?)\]')  # Match "[kanji|kana]" format.

def furigana_re_replacer(match):
	kanji, kana = map(
		lambda s: s.split('.'),
		match.groups()
	)

	return ''.join((
		'<ruby>',
		'<rb>'.join(kanji),
		'<rt>',
		'<rt>'.join(kana),
		'</ruby>'
	))

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
	print(html_header)

	for line in stripped_and_empty_lines_collapsed(sys.stdin):
		if line == '':
			print('<p>')
		elif line == '~':
			print('<div class="page-break">~</div>')
		else:
			print(furiganize(line), end='<br>\n')


if __name__ == '__main__':
	main()
