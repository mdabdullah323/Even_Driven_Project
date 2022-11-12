import glob
from logging import exception
from pydoc import describe
import shutil
import os
import runpy

text_source_path = '../source/*.txt'
py_source_path = '../source/*.py'
destination_path = '../destination/'
temp = '../source/temp/'
postfix = [1, 2, 3]

while True:

    text_source_object = glob.glob(text_source_path)
    py_source_object = glob.glob(py_source_path)
    if len(text_source_object) > 0:
        # reading source file
        with open('../source/file.txt', 'r') as file:
            lines = file.readlines()
            file.close()

        #write and spliting
        for file_path in text_source_object:
            object_name = file_path.split('/')[-1].split('.')
            prefix = object_name[0]
            postfix = object_name[1]

            for item in range(1, 4):
                with open(f'../destination/temp/{prefix}_{item}.txt', 'w') as file:
                    file.writelines(lines[:10*item])
                    file.close()
        shutil.make_archive(base_name=f'../source/file',
                            format='zip', root_dir='../destination/temp/')
        shutil.move(src='../source/file.zip', dst='../destination/file.zip')
        shutil.unpack_archive(filename='../destination/file.zip',
                              extract_dir='../destination/')

    if len(py_source_object) > 0:
        for p_file in py_source_object:
            try:
                runpy.run_path(p_file)
            except BaseException as error:
                print(f"wait found an Error{error}")
