import sys

file1, file2 = sys.argv[1], sys.argv[2]

with open( file1 ) as f:
	file1 = f.readlines()

with open( file2 ) as f:
	file2 = f.readlines()

removed = [ line for line in file1 if not line in file2 ]

added = [ line for line in file2 if not line in file1 ]

for line in added:
	print( f'+ { line.strip() }' )

for line in removed:
	print( f'- { line.strip() }' )
