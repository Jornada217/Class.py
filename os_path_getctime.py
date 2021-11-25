import os
import time
from pathlib import Path

# dir = 'C:\\Users\\joaopaulo\\PycharmProjects\\Learning_Projects\\Folder'
src = os.path.join('Folder')
dir = os.path.abspath(src)
print('Directory of files is:', dir)

file_upload = 'basketball_stats.txt'
file_src = os.path.join('folder', file_upload)
file_dir = os.path.abspath(file_src)
print('The basketball_stats absolute path is:', file_dir)
filemain = os.path.splitext(file_upload)[0]
print('Basketball stats file name (before "txt": ', filemain)

last_file = max([f for f in os.listdir(dir)], key=lambda xa: os.path.getctime(os.path.join(dir, xa)))
print('The last file name is: ', last_file)
print('The last file type is: ', type(last_file))
# print(os.path.abspath(os.path.join(os.path.dirname(file))))
# print(os.path.dirname(os.path.dirname(file)))


#rename
f_src = os.path.join('folder', last_file)
dir_last = os.path.abspath(f_src)
print('The root directory of last file is: ', dir_last)
print('Last file split name (without ".txt"): ')
lfn = os.path.splitext(last_file)[0]
print(lfn)
try:
    path = Path(dir_last)
    target = path.with_name(path.name.replace(lfn, filemain + '_converted'))
    path.rename(target)
except:
    print(FileNotFoundError)