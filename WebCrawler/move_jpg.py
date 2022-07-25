import re
import os
import shutil

class FileMove():

    SOURCE_FOLDER = ""
    TARGET_FOLDER = ""

    def __init__(self):
        pass
    def _check_parent(self, path):
        """
        This function is to check if parent folder exists,
        if it does, continue, otherwise, it will raise error
        """
        path = self.TARGET_FOLDER
        if not os.path.exists(path):
            print(f'There\'s no folder for {path}')
            return False
        else:
            print(f'Starting to process jpg files in {path}')
            return True

    def _check_target(self, path):
        """
        This function is to create check if target folder is there,
        if it is, clean it and re-post, otherwise, create folder and post
        """
        path = self.TARGET_FOLDER
        if not os.path.exists(path):
            print(f'Creating folder {path}')
            os.makedirs(path)
            return True
        else:
            print(f'Removing files in {path}')
            for root,dirs,files in os.walk(path):
                for name in files:
                    os.remove(os.path.join(root,name))
            return True

    def _processing_files(self):
        """
        This function is to processing files
        """
        self._check_target(self.TARGET_FOLDER)
        if self._check_parent(self.SOURCE_FOLDER):
            for root,ds,fs in os.walk(self.SOURCE_FOLDER):
                for f in fs:
                    if f.endswith(".jpg"):
                        shutil.move(os.path.join(root,f),os.path.join(self.TARGET_FOLDER))
                        print("Moving is done.")


if __name__ == '__main__':

   test_obj = FileMove()
   test_obj.SOURCE_FOLDER = "D:/迅雷下载/pythontest"
   test_obj.TARGET_FOLDER = "D:/迅雷下载/pythontest/target"
   test_obj._processing_files()
