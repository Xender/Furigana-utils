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
