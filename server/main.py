import glob
import shutil
import runpy
import os
import time

text_source_path = '../source/*.txt'
py_source_path = '../source/*.py'
destination_path = '../destination/'
temp = '../source/temp/'
postfix = [1, 2, 3]

while True:
    
    os.mkdir('../source/temp')
    text_source_object = glob.glob(text_source_path)
    py_source_object = glob.glob(py_source_path)
    if len(text_source_object) > 0:
            
        # reading source file
        for file_path in text_source_object:
            with open(file_path,'r') as file:
                lines = file.readlines()
                file.close()

             #write and spliting
            
            object_name = file_path.split('\\')[-1].split('.')
            prefix = object_name[0]
            postfix = object_name[1]
            print(prefix)
            for item in range(1, 4):
                    with open(f'../source/temp/{prefix}_{item}.txt', 'w') as file:
                        file.writelines(lines[:10*item])
                        file.close()

            
        shutil.make_archive(base_name=f'../source/file',
                            format='zip', root_dir='../source/temp/')
        
        shutil.copy(src='../source/file.zip', dst='../destination/file.zip')
        
        shutil.unpack_archive(filename='../destination/file.zip',
                              extract_dir='../destination/')
        
       
        shutil.rmtree("../source/temp/")
        os.remove("../destination/file.zip")
        #os.remove('../source/temp')
        os.remove('../source/file.zip')
        time.sleep(0.30)
        
        
    
    if len(py_source_object) > 0:
        for p_file in py_source_object:
            try:
                runpy.run_path(p_file)
            except BaseException as error:
                print(f"wait found an Error{error}")
