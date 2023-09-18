import os
import shutil

class helperClass:
    def __init__(self):
        pass

    def delete_file(self, path):
        for filename in os.listdir(path):
            file_path = os.path.join(path, filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except Exception as e:
                print('Failed to delete %s. Reason: %s' % (file_path, e))
    

    def delete_folder(self, path):
        if os.path.exists(path):
            shutil.rmtree(path)
        else:
            print("The file does not exist")

    def create_folder(self, path):
        if not os.path.exists(path):
            os.makedirs(path)
        else:
            print("Folder already exists")

    def create_file(self, path):
        if not os.path.exists(path):
            open(path, 'w')
        else:
            print("File already exists")