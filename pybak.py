import os
import shutil
import datetime

# source1 : destination1, source2 : destination2
backupfolders = {"C:/pybak/src" : "C:/pybak/dst"}
    
def copy_folder(source, dst):
    resfolder = os.path.basename(os.path.normpath(source))
    bakupfoldername = datetime.datetime.now().strftime("%Y%m%d%H%M%S") + "_" + resfolder
    shutil.copytree(source, dst + "/" + bakupfoldername);

if __name__ == "__main__":
    print("pybak version 0.Init")
    for src, dst in backupfolders.items():
        copy_folder(src, dst);
    print("complete")
