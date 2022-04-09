import os
from glob import glob
# Comments
#特定の拡張子を持つファイルを検索するためのスクリプト

# Variable Declaration
fld_pth = ["C:\\APPL_DEV\\PY001\\scripts\\pyscripts"]
target_ext = "txt"

# Functions
def search_files(flname):
    for fld in fld_pth:
        srch_results = [y for x in os.walk(fld) for y in glob(os.path.join(x[0], flname))]
        for srch_result in srch_results:
            print(srch_result)
            os.startfile(srch_result)
            return;

# Script Process
while True:
    print("searching the file with ext: " + target_ext)
    flname = input("please enter the filename without extension here: ")
    flname = flname+"."+target_ext
    #print(flname)
    search_files(flname)