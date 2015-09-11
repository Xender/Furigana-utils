import re


class MarkupSyntaxError(Exception):
	pass


furigana_re = re.compile(r'\[(.*?)\|(.*?)\]')  # Match "[kanji|kana]" format, non-greedily.


def furigana_re_replacer(match, formatter):
	kanji, kana = map(
		lambda s: s.split('.'),
		match.groups()
	)

	if len(kanji) != len(kana):
		raise MarkupSyntaxError("Number of base text parts not equal to number of ruby parts: " + match.group(0))

	return formatter(kanji, kana)


def furiganize(text, formatter):
	replacer = lambda match: furigana_re_replacer(match, formatter)

	return furigana_re.sub(replacer, text)


# ---

from helpers import stripped_and_empty_lines_collapsed


def process(out_format, in_file, out_file):
	print(out_format.header, file=out_file)

	for line in stripped_and_empty_lines_collapsed(in_file):
		if line == '':
			print(out_format.new_paragraph, file=out_file)
		elif line == '~':
			print(out_format.page_separator, file=out_file)
		else:
			print(furiganize(line, out_format.ruby_formatter), end=out_format.new_line, file=out_file)

	print(out_format.footer, file=out_file)
