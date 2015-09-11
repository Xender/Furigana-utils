#!/usr/bin/env python3

import sys

from markup_processor import furiganize
from helpers import stripped_and_empty_lines_collapsed


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


def html_ruby_formatter(kanji, kana):
	return ''.join((
		'<ruby>',
		'<rb>'.join(kanji),
		'<rt>',
		'<rt>'.join(kana),
		'</ruby>'
	))


def main():
	print(html_header)

	for line in stripped_and_empty_lines_collapsed(sys.stdin):
		if line == '':
			print('<p>')
		elif line == '~':
			print('<div class="page-break">~</div>')
		else:
			print(furiganize(line, html_ruby_formatter), end='<br>\n')


if __name__ == '__main__':
	main()
