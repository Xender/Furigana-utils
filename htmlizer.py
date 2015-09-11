#!/usr/bin/env python3

import sys

from markup_processor import process
from formatters.html import HtmlFormat


def main():
	process(HtmlFormat, sys.stdin, sys.stdout)


if __name__ == '__main__':
	main()
