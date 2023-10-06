from os import WTERMSIG
from PyInstallerRunner.myPyInstallerRunner import myPyInstallerRunner
from pytest import mark, raises
from unittest.mock import patch
from test.PyInstallerRunner_Fixture import test_strApp01_config_dir, test_strApp01_config_file, test_strApp01_src

@mark.Build
def test_PyInstallerRunner_Build_NotFoundFile():
    with raises(FileNotFoundError):
        oRunner = myPyInstallerRunner()
        oRunner.buildCode("test.py")
    # End of with-block
# End of test_PyInstallerRunner_Build_NotFoundFile

@mark.Build
def test_PyInstallerRunner_Build_SucceedFile(test_strApp01_src, test_strApp01_config_file):
    oRunner = myPyInstallerRunner()
    oRunner.loadSetting(test_strApp01_config_file)
    oRunner.buildCode(test_strApp01_src)
# End of test_PyInstallerRunner_Build_SucceedFile

@mark.Build
def test_PyInstallerRunner_Build_SucceedDir(test_strApp01_src, test_strApp01_config_dir):
    oRunner = myPyInstallerRunner()
    oRunner.loadSetting(test_strApp01_config_dir)
    oRunner.buildCode(test_strApp01_src)
# End of test_PyInstallerRunner_Build_SucceedDir

@mark.Build
def test_PyInstallerRunner_Build_Failed(test_strApp01_src, test_strApp01_config_file):
    with patch("PyInstallerRunner.myPyInstallerRunner.system") as oMocker:
        oMocker.return_value = 1
        with raises(RuntimeError):
            oRunner = myPyInstallerRunner()
            oRunner.loadSetting(test_strApp01_config_file)
            oRunner.buildCode(test_strApp01_src)
        # End of with-block
    # End of with-block
# End of test_PyInstallerRunner_Build_Failed

