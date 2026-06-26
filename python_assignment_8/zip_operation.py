#zip file shutil.make_archive() use create and extract zip
#create zip 

import zipfile
with zipfile.ZipFile('new_zip.zip','w') as zip_file:
    zip_file.write('example.txt')
   

#extract zip 

with zipfile.ZipFile('new_zip.Zip','r') as zip_file:
    zip_file.extractall('extracted_files')