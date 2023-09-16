from typing import Dict, Union

class myPyInstallerRunner(object):
    """
    Description:
    =======================================================
    This class can use `PyInstaller` to build python code.
    """
    def __init__(self) -> None:
        self.__m_dctSettings = {}
        self.__m_dctSettings["BuildPath"] = {"DistPath": "./bin/release", "SpecPath": "./bin", "WorkPath": "./bin/build", "IconPath": ""}
        self.__m_dctSettings["Args"] = {"IsFile": True, "NeedShowConsole": True}
    # End of constructor

    @property
    def m_dctSettings(self) -> Dict[str, Union[str, bool]]:
        return self.__m_dctSettings
    # End of myPyInstallerRunner::m_dctSettings
# End of class myPyInstallerRunner
