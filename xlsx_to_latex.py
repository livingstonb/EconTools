import sys
import os
import pandas as pd

def drop_line(text, lineno):
	lines = text.splitlines()
	del lines[lineno]
	return '\n'.join(lines)

def xlsx_to_latex(filepath):
	df = pd.read_excel(filepath, index_col=0, header=1)
	tex = df.to_latex(float_format="%.1f")

	# print(drop_line(tex, 3))

	# outpath = filepath.replace('.xlsx', '.tex')
	# with open(outpath, 'w') as fobj:
	# 	fobj.write(tex)

if __name__ == '__main__':
	xlsx_to_latex(sys.argv[1])