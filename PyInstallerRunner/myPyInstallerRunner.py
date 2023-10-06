from typing import Dict
from yaml import safe_load
from os.path import isfile

class myPyInstallerRunner(object):
    """
    Description:
    =======================================================
    This class can use `PyInstaller` to build python code.
    """
    def __init__(self) -> None:
        self.__m_dctSettings = {}
        self.__m_dctSettings["BuildPath"] = {"DistPath": "./bin/release", "SpecPath": "./bin", "WorkPath": "./bin/build", "IconPath": ""}
        self.__m_dctSettings["CompileConfig"] = {"IsFile": True, "NeedShowConsole": True, "AppName": "Application"}
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
# End of class myPyInstallerRunner
