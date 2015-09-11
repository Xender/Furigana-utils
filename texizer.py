#!/usr/bin/env python3

import sys

from markup_processor import process
from formatters.tex import TexFormat


def main():
	process(TexFormat, sys.stdin, sys.stdout)


if __name__ == '__main__':
	main()
