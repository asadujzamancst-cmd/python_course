#os.mkdir(),os.listdir(),directory rename, os.rmdir()
#create directory

import os
os.mkdir('new_directory')

#list directory

print( os.listdir('python_assignment_8'))

#directory rename

os.rename("new_directory","old2_directory")
#remove directory
os.rmdir('old_directory')
