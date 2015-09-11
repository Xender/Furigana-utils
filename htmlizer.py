#!/usr/bin/env python3

import sys


header = '''\
<!doctype html>
<meta charset="utf-8">

'''

def main():
	print(header)

	for line in sys.stdin:
		html_line = (line
			.replace('[', '<ruby><rb>')
			.replace('|', '</rb><rt>')
			.replace(']', '</rt></ruby>')
		)

		print(html_line, end='<br>')


if __name__ == '__main__':
	main()
