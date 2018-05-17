import os
import re
import sys
from pprint import pprint

def search_files(dir_path,file_name_pattern):
	child_dirs = []
	files = []

	root_path = dir_path

	target_file_path = (root_path.replace('\\','\\\\') + file_name_pattern)
	target_file_path_pattern = re.compile(r'%s' % target_file_path)

	for path in os.listdir(root_path):
		absolute_path = root_path + '\\' +path
		if os.path.isdir(absolute_path):
			child_dirs.append(absolute_path)
		else:
			if target_file_path_pattern.match(absolute_path):
				files.append(absolute_path)

	for child_dir in child_dirs:
		child_dir_files = search_files(child_dir.replace('\\\\','\\'),file_name_pattern)
		for file in child_dir_files:
			files.append(file)

	return files

def replace_new_line_code(file_name):
	pass

def main():
	try:
		file_name_pattern = sys.argv[1]
	except:
		print('Input File Name Pattern !!')
		return False
	
	root_path = os.getcwd()
	files = search_files(root_path,file_name_pattern)
	pprint(files)
	for file in files:
		replace_new_line_code(file)

if __name__ == '__main__':
	main()