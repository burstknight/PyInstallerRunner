from PyInstallerRunner.myPyInstallerRunner import myPyInstallerRunner
from pytest import mark, raises
from unittest.mock import patch
from test.PyInstallerRunner_Fixture import test_dctApp01Cofig_dir, test_dctApp01Cofig_file, test_dctApp02Cofig_dir, test_dctApp02Cofig_file
from os import system, getcwd, chdir

def runApp(strExeDir: str, strAppName: str) -> int:
    """
    Description:
    =======================================================
    Try to run the given application to test if can work.

    Args:
    =======================================================
    - strExeDir: Give the directory path that contains the application.
    - strAppName: Give the application name.

    Retuns:
    =======================================================
    - rtype: int, Return `0` if succeed to run the application, otherwiser retun non-zero integer.
    """
    strCurrPath = getcwd()
    chdir(strExeDir)
    strCommand = "./%s" %(strAppName)
    iReturnCode = system(strCommand)
    chdir(strCurrPath)

    return iReturnCode
# End of runApp

@mark.Build
def test_PyInstallerRunner_Build_NotFoundFile():
    with raises(FileNotFoundError):
        oRunner = myPyInstallerRunner()
        oRunner.buildCode("test.py")
    # End of with-block
# End of test_PyInstallerRunner_Build_NotFoundFile

@mark.Build
def test_PyInstallerRunner_Build_SucceedFile(test_dctApp01Cofig_file):
    oRunner = myPyInstallerRunner()
    oRunner.loadSetting(test_dctApp01Cofig_file["config"])
    oRunner.buildCode(test_dctApp01Cofig_file["source"])

    assert 0 == runApp(test_dctApp01Cofig_file["bin"], test_dctApp01Cofig_file["app"])
# End of test_PyInstallerRunner_Build_SucceedFile

@mark.Build
def test_PyInstallerRunner_Build_SucceedDir(test_dctApp01Cofig_dir):
    oRunner = myPyInstallerRunner()
    oRunner.loadSetting(test_dctApp01Cofig_dir["config"])
    oRunner.buildCode(test_dctApp01Cofig_dir["source"])

    assert 0 == runApp(test_dctApp01Cofig_dir["bin"], test_dctApp01Cofig_dir["app"])
# End of test_PyInstallerRunner_Build_SucceedDir

@mark.Build
def test_PyInstallerRunner_Build_Failed(test_dctApp01Cofig_dir):
    with patch("PyInstallerRunner.myPyInstallerRunner.system") as oMocker:
        oMocker.return_value = 1
        with raises(RuntimeError):
            oRunner = myPyInstallerRunner()
            oRunner.loadSetting(test_dctApp01Cofig_dir["config"])
            oRunner.buildCode(test_dctApp01Cofig_dir["source"])
        # End of with-block
    # End of with-block
# End of test_PyInstallerRunner_Build_Failed

@mark.Build
def test_PyInstallerRunner_Build_SucceedDir_WithResources(test_dctApp02Cofig_dir):
    oRunner = myPyInstallerRunner()
    oRunner.loadSetting(test_dctApp02Cofig_dir["config"])
    oRunner.buildCode(test_dctApp02Cofig_dir["source"])

    assert 0 == runApp(test_dctApp02Cofig_dir["bin"], test_dctApp02Cofig_dir["app"])
# End of test_PyInstallerRunner_Build_SucceedDir_WithResources

@mark.Build
def test_PyInstallerRunner_Build_SucceedFile_WithResources(test_dctApp02Cofig_file):
    oRunner = myPyInstallerRunner()
    oRunner.loadSetting(test_dctApp02Cofig_file["config"])
    oRunner.buildCode(test_dctApp02Cofig_file["source"])

    assert 0 == runApp(test_dctApp02Cofig_file["bin"], test_dctApp02Cofig_file["app"])
# End of test_PyInstallerRunner_Build_SucceedDir_WithResources
