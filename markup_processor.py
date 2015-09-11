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
