def stripped_and_empty_lines_collapsed(it):
	last_line_empty = False

	for line in it:
		line = line.rstrip('\n')

		if line == '' and last_line_empty:
			continue

		last_line_empty = (line == '')

		yield line
