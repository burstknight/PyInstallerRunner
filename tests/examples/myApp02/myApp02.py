from yaml import safe_load
from os import listdir
from os.path import join, isfile

def main():
    with open("version.txt", "r", encoding="utf-8") as oReader:
        strVersern = oReader.readline().strip()
    # End of with-block

    print("Verison: %s\n" %(strVersern))

    strDataDir = "./data"
    isShow = False
    for strFile in listdir(strDataDir):
        strPath = join(strDataDir, strFile)
        if False == isfile(strPath):
            continue
        # End of if-condition

        print("="*20 + " %s " %(strPath) + "="*20)
        
        with open(strPath, "r", encoding="utf-8") as oReader:
            dctYaml = safe_load(oReader)
        # End of with-block

        print(dctYaml)
        print()
        isShow = True
    # End of for-loop

    if False == isShow:
        raise FileNotFoundError("Failed to load *yaml files!")
    # End of if-condition
# End of main

if "__main__" == __name__:
    main()
# End of if-condition
