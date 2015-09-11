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

	footer = '\n\\end{document}\n'

	new_paragraph  = '\n'
	new_line       = '\\newline\n'
	page_separator = '{\\raise.17ex\\hbox{$\\scriptstyle\\sim$}}\\pagebreak\n'

	@staticmethod
	def ruby_formatter(kanjis, kanas):
		ret = ''

		for kanji, kana in zip(kanjis, kanas):
			ret += '\\ruby{' + kanji + '}{' + kana + '}'

		return ret
