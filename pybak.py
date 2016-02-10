import os
import shutil
import datetime

# source1 : destination1, source2 : destination2
backupfolders = {"C:/pybak/src" : "C:/pybak/dst"}
    
def copy_folder(src, dst):
    srcfoldername = os.path.basename(os.path.normpath(src))
    bakupfoldername = datetime.datetime.now().strftime("%Y%m%d%H%M%S") + "_" + srcfoldername
    shutil.copytree(src, dst + "/" + bakupfoldername);

if __name__ == "__main__":
    print("pybak version 0.Init")
    for src, dst in backupfolders.items():
        copy_folder(src, dst);
    print("complete")
