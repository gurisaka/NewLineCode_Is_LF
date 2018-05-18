import os
import re
import sys
from pprint import pprint

def search_files(dir_path,file_name_pattern,now_dir_depth,max_dir_depth):
	#Depth Check
	if now_dir_depth >= max_dir_depth:
		return []

	child_dirs = []
	files = []

	root_path = dir_path

	target_file_path = (root_path + file_name_pattern)
	target_file_path_pattern = re.compile(r'%s' % target_file_path)

	#Search Dir and Files
	for path in os.listdir(root_path):
		absolute_path = root_path + '/' +path
		if os.path.isdir(absolute_path):
			child_dirs.append(absolute_path)
		else:
			if target_file_path_pattern.match(absolute_path):
				files.append(absolute_path)

	for child_dir in child_dirs:
		child_dir_files = search_files(child_dir,file_name_pattern,now_dir_depth + 1,max_dir_depth)
		for file in child_dir_files:
			files.append(file)

	return files

def replace_new_line_code(file_name):
	pass

def main():
	try:
		file_name_pattern = sys.argv[1]
		try:
			max_dir_depth = int(sys.argv[2])
			if max_dir_depth >= 7:
				print("over 7 depth is invalid !!")
				max_dir_depth = 6
		except:
			max_dir_depth = 4
	except:
		print('Input File Name Pattern !!')
		return False
	
	root_path = os.getcwd()

	files = search_files(root_path,file_name_pattern,0,max_dir_depth)

	pprint(files)
	for file in files:
		replace_new_line_code(file)

if __name__ == '__main__':
	main()