import os, sys


FILE_TYPES = [
	'.ino',			# Arduino
	'.asm',			# Assembly
	'.ahk',			# Auto Hot Key
	'.bat',			# Batch
	'.c',			# C
	'.h',			# C
	'.cpp',			# C++
	'.hpp',			# C++
	'.cbl',			# Cobol
	'.cobol',		# Cobol
	'.jcl',			# Cobol
	'.css',			# CSS
	'.yml',			# Docker
	'.yaml',		# Docker
	'Dockerfile',	# Docker
	'.html',		# html
	'.java',		# Java
	'.js',			# JavaScript
	'.jsx',			# JavaScript
	'.kv',			# Kivy
	'.ld',			# Linker
	'Makefile',		# Make
	'.glsl',		# OpenGL
	'.frag',		# OpenGL
	'.vert',		# OpenGL
	'.prisma',		# Prisma
	'.py',			# Python
	'.pyw',			# Python
	'.rpy',			# Ren'py
	'.sass',		# SASS
	'.scss',		# SASS
	'.sh',			# Shell
	'.sql',			# SQL
	'BUILD',		# Starlark
	'.tpl',			# Template
	'.tf',			# Terraform
	'.tfvars',		# Terraform
	'.tex',			# Tex
	'.ts',			# TypeScript
	'.tsx',			# TypeScript
	'.v',			# Verilog
	'.ys',			# Y86 Assembly
]


EXTRA_TYPES = [
	'.cnf',						# Conf
	'.env',						# Environment
	'.gitignore',				# Git
	'.gitattributes',			# Git
	'.md',						# Markdown
	'nest-cli.json',			# NestJS
	'package-lock.json',		# NodeJs
	'tsconfig.json',			# NodeJs
	'.postman_collection.json',	# Postman
	'.prettierrc',				# Prettier
	'.test',					# Test
	'.toml',					# Toml
	'.eslintrc.js',				# Typescript
	'tsconfig.build.json',		# Typescript
]



def find(folder):
	files = []
	for file in os.listdir(folder):
		path = os.path.join(folder, file)
		if os.path.isdir(path):
			files += find(path)
		else:
			files.append(path)
	return (files)


def filter_extentions(files):
	new_files = []
	for file in files:
		for ext in FILE_TYPES:
			if file.endswith(ext):
				new_files.append(file)
				break
	return new_files


def count_lines(file):
	lines = []
	try:
		with open(file, encoding='utf-8', mode='r') as f:
			lines = f.readlines()
	except UnicodeDecodeError as err:
		print(file, err)
	return len(lines) + 1, len(''.join(lines))



def main():
	if len(sys.argv) > 1 and sys.argv[1] == "-e":
		global FILE_TYPES
		FILE_TYPES += EXTRA_TYPES
	files = find("..")
	files = filter_extentions(files)
	count, characters = 0, 0
	for file in files:
		res = count_lines(file)
		count += res[0]
		characters += res[1]
	print(f"Total Files: {len(files)}")
	print(f"Total Lines: {count}")
	print(f"Total Characters: {characters}")


if __name__ == '__main__':
	main()
