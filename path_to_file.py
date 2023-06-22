import os
def find_path_to_file(name_file):
    path = __file__
    path = path.split('\\')
    del path[-1]
    del path[-1]
    path = "\\".join(path)
    path = os.path.join(path, name_file)
    return path