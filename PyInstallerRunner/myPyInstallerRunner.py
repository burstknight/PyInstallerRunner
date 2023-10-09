from typing import Dict, List
from yaml import safe_load
from os.path import isfile, isdir, join, exists
from os import system
from shutil import copy, copytree, rmtree
from argparse import ArgumentParser, Namespace
import sys
from typing import List
import platform

__version__ = "0.1.0-dev0"

class myPyInstallerRunner(object):
    """
    Description:
    =======================================================
    This class can use `PyInstaller` to build python code.
    """
    def __init__(self) -> None:
        self.__m_dctSettings = {}
        self.__m_dctSettings["BuildPath"] = {"DistPath": "./bin/release", "SpecPath": "./bin", "WorkPath": "./bin/build", "IconPath": ""}
        self.__m_dctSettings["CompileConfig"] = {"IsFile": True, "NeedShowConsole": True, "AppName": "Application", "Resources": []}
    # End of constructor

    @property
    def m_dctSettings(self) -> Dict:
        return self.__m_dctSettings
    # End of myPyInstallerRunner::m_dctSettings

    def loadSetting(self, strPath:str):
        """
        Description:
        ===================================================
        Load the setting from the given file path.

        Args:
        ===================================================
        - strPath: Give the setting file path.
        """
        if False == isfile(strPath):
            raise FileNotFoundError("Not found file: %s" %(strPath))
        # End of if-condition

        with open(strPath, "r", encoding="utf-8") as oReader:
            dctYamlSetting = safe_load(oReader)
        # End of with-block

        if dctYamlSetting is None:
            return
        # End of if-condition

        self.__setSettingTree(dctYamlSetting, self.m_dctSettings)
    # End of myPyInstallerRunner::loadConfig

    def __setSettingTree(self, dctYamlTree: Dict, dctSettingTree: Dict):
        """
        Description:
        ===================================================
        Use tree travel to set the setting from the yaml file.

        Args:
        ===================================================
        - dctYamlTree: Give the context for the yaml file.
        - dctSettingTree: Give the setting.
        """
        if False == isinstance(dctYamlTree, dict):
            raise TypeError("The type of the parameter `dctYamlTree` must be `dict` in the method `__setSettingNode()` of the class `myPyInstallerRunner`!")
        # End of if-condition

        if False == isinstance(dctSettingTree, dict):
            raise TypeError("The type of the parameter `dctSettingTree` must be `dict` in the method `__setSettingNode()` of the class `myPyInstallerRunner`!")
        # End of if-condition

        for strKey in dctYamlTree.keys():
            self.__setSettingNode(strKey= strKey, dctYamlNode=dctYamlTree, dctSettingNode=dctSettingTree)
        # End of for-loop
    # End of myPyInstallerRunner::setSettingNode

    def __setSettingNode(self, strKey: str , dctYamlNode: Dict, dctSettingNode: Dict):
        """
        Description:
        ===================================================
        Use recursive to set the settings.

        Args:
        ===================================================
        - strKey: Give the key word to set the value for the setting.
        - dctYamlNode: Give the node from the yaml file.
        - dctSettingNode: Give the setting node to set.
        """
        if False == isinstance(dctYamlNode[strKey], dict):
            dctSettingNode[strKey] = dctYamlNode[strKey]
            return
        else:
            for strSonKey in dctYamlNode[strKey].keys():
                if strSonKey not in dctSettingNode[strKey].keys():
                    raise KeyError("The key `%s` in `*.yaml` file is undefined in the method `__setSettingNode()` of the class `myPyInstallerRunner`!" %(strKey))
                # End of if-condition

                self.__setSettingNode(strSonKey, dctYamlNode[strKey], dctSettingNode[strKey])
            # End of for-loop
        # End of if-condition
    # End of myPyInstallerRunner::setSettingNode

    def __parseSettings(self) -> str:
        """
        Description:
        ===================================================
        Parse the field `__m_dctSettings` to generate a
        list of the arguments for `PyInstaller`.
        """
        strArgs = ""
        
        for strKey in self.m_dctSettings["CompileConfig"].keys():
            if "IsFile" == strKey:
                if True == self.m_dctSettings["CompileConfig"][strKey]:
                    strArgs += "-F "
                else:
                    strArgs += "-D "
                # End of if-condition
            elif "NeedShowConsole" == strKey:
                if False == self.m_dctSettings["CompileConfig"][strKey]:
                    strArgs += "-w "
                # End of if-condition
            elif "AppName" == strKey:
                strArgs += "-n \"%s\" " %(self.m_dctSettings["CompileConfig"][strKey])
            # End of if-condition
        # End of for-loop

        dctBuildPathArgs = {}
        dctBuildPathArgs["DistPath"] = "--distpath"
        dctBuildPathArgs["SpecPath"] = "--specpath"
        dctBuildPathArgs["WorkPath"] = "--workpath"
        dctBuildPathArgs["IconPath"] = "-i"
        for strKey in self.m_dctSettings["BuildPath"].keys():
            if "IconPath" != strKey:
                strArgs += "%s \"%s\" "  %(dctBuildPathArgs[strKey], self.m_dctSettings["BuildPath"][strKey])
            else:
                if len(self.m_dctSettings["BuildPath"][strKey]) > 0:
                    strArgs += "%s \"%s\" " %(dctBuildPathArgs[strKey], self.m_dctSettings["BuildPath"][strKey])
                # End of if-condition
            # End of if-condition
        # End of for-loop

        return strArgs
    # End of myPyInstallerRunner::__parseSettings

    def __copyResourceFiles(self, strBuildDir: str, vdctResources: List[Dict[str, str]]):
        """
        Description:
        ===================================================
        Copy all resource files into the build directory if 
        we need.

        Args:
        ===================================================
        - strBuildDir: All resource files will copy into this directory.
        - vdctResources: Give the list of the resource.
        """
        if len(vdctResources) <= 0:
            return
        # End of if-condition

        for dctResource in vdctResources:
            if "." == dctResource["Target"]:
                strTargetPath = strBuildDir
            else:
                strTargetPath = join(strBuildDir, dctResource["Target"])
            # End of if-condition

            strSourcePath = dctResource["Source"]
            if True == isfile(strSourcePath):
                copy(strSourcePath, strTargetPath)
            elif True == isdir(strSourcePath):
                if True == exists(strTargetPath):
                    rmtree(strTargetPath)
                # End of if-condition

                copytree(strSourcePath, strTargetPath)
            else:
                print("Warning: Not found file or directory: %s" %(strSourcePath))
            # End of if-condition
        # End of for-loop
    # End of myPyInstallerRunner::__copyResourceFiles

    def buildCode(self, strSource: str):
        """
        Description:
        ===================================================
        Build python code as an executable file.

        Args:
        ===================================================
        - strSource: Give the python code file path.
        """
        if False == isfile(strSource):
            raise FileNotFoundError("Not found python code file: %s" %(strSource))
        # End of if-condition

        strArgs = self.__parseSettings()
        if "Windows" == platform.system():
            strPythonCommand = "python"
        else:
            strPythonCommand = "python3"
        # End of if-condition

        strCommand = "%s -m PyInstaller %s -y %s" %(strPythonCommand, strArgs, strSource)

        iReturnCode = system(strCommand)

        if 0 != iReturnCode:
            raise RuntimeError("Failed to build the python code file as an executable file!")
        # End of if-condition

        if True == self.m_dctSettings["CompileConfig"]["IsFile"]:
            strBuildDir = self.m_dctSettings["BuildPath"]["DistPath"]
        else:
            strBuildDir = join(self.m_dctSettings["BuildPath"]["DistPath"], self.m_dctSettings["CompileConfig"]["AppName"])
        # End of if-condition

        self.__copyResourceFiles(strBuildDir, self.m_dctSettings["CompileConfig"]["Resources"])
    # End of myPyInstallerRunner::buildCode
# End of class myPyInstallerRunner


def parseArgs(vstrArgs: List[str]) -> Namespace:
    """
    Descripiton:
    =======================================================
    Parse the arguments from user.

    Returns:
    =======================================================
    - rtype: Namespace, Return the parsed arguments.
    """
    oArgParser = ArgumentParser(description="This is a tool that can use `*.yaml` file as the configuration file and `PyInstaller` to build python code file as an executable file.")
    oArgParser.add_argument("source_path", help="Give the python source code file path.", type=str)
    oArgParser.add_argument("-c", "--config", help="Give `*.yaml` file path to load configuration.", default="", dest="config_path", type=str)
    oArgParser.add_argument("-v", "--version", action="version", version="Version: %s" %(__version__))

    return oArgParser.parse_args(vstrArgs)
# End of parseArgs

def main():
    oArgs = parseArgs(sys.argv[1:])

    oBuildRunner = myPyInstallerRunner()
    if len(oArgs.config_path) > 0:
        oBuildRunner.loadSetting(oArgs.config_path)
    # End of if-condition

    oBuildRunner.buildCode(oArgs.source_path)
# End of main

if "__main__" == __name__:
    main()
# End of if-condition
