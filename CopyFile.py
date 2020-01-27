import shutil

a = r'source_path\file.extn' #r is added to make the docstring a raw string
b = r'destination_path\file.extn'

shutil.copyfile(a, b)
