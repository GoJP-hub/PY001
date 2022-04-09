import os
from glob import glob

# Comments

# Variable Declaration

# Functions
def search_files(flname, fld_pth):
    for fld in fld_pth:
        #print(fld_pth)
        #print(fld)
        #print(flname)
        srch_results = [y for x in os.walk(fld) for y in glob(os.path.join(x[0], flname))]
        for srch_result in srch_results:
            print(srch_result)
            os.startfile(srch_result)
            return;
# Script Process
