import os

files = os.scandir('/home/ukulelezombie')

for file in files:
	if file.is_file():
		print('Filename:',file.name)
		print('Filesize:',file.stat().st_size)
