from yaml import safe_load
from os import listdir
from os.path import join

def main():
    with open("version.txt", "r", encoding="utf-8") as oReader:
        strVersern = oReader.readline().strip()
    # End of with-block

    print("Verison: %s\n" %(strVersern))

    strDataDir = "./data"
    for strFile in listdir(strDataDir):
        strPath = join(strDataDir, strFile)
        print("="*20 + " %s " %(strPath) + "="*20)
        
        with open(strPath, "r", encoding="utf-8") as oReader:
            dctYaml = safe_load(oReader)
        # End of with-block

        print(dctYaml)
        print()
    # End of for-loop
# End of main

if "__main__" == __name__:
    main()
# End of if-condition
