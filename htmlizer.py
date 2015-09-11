#!/usr/bin/env python3

import sys

from markup_processor import furiganize
from helpers import stripped_and_empty_lines_collapsed


class HtmlFormat:
	header = '''\
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

	footer = ''

	new_paragraph  = '<p>'
	new_line       = '<br>\n'
	page_separator = '<div class="page-break">~</div>'

	@staticmethod
	def ruby_formatter(kanji, kana):
		return ''.join((
			'<ruby>',
			'<rb>'.join(kanji),
			'<rt>',
			'<rt>'.join(kana),
			'</ruby>'
		))


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
