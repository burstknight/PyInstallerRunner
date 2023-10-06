from test.PyInstallerRunner_Fixture import test_strDefaultArgs, test_strCompleteArgs, test_strPartArgs
from pytest import mark
from PyInstallerRunner.myPyInstallerRunner import myPyInstallerRunner

@mark.test
def test_PyInstallerRunner_ParseDefaultArgs(test_strDefaultArgs):
    oRunner = myPyInstallerRunner()
    strArgs = oRunner._myPyInstallerRunner__parseSettings()

    assert strArgs == test_strDefaultArgs
# End of test_PyInstallerRunner_ParseDefaultArgs

@mark.test
def test_PyInstallerRunner_ParseCompleteArgs(test_strCompleteArgs):
    oRunner = myPyInstallerRunner()
    oRunner.loadSetting("./test/configs/complete_config.yaml")
    strArgs = oRunner._myPyInstallerRunner__parseSettings()

    assert strArgs == test_strCompleteArgs
# End of test_PyInstallerRunner_ParseCompleteArgs

@mark.test
def test_PyInstallerRunner_ParsePartArgs(test_strPartArgs):
    oRunner = myPyInstallerRunner()
    oRunner.loadSetting("./test/configs/part_config.yaml")
    strArgs = oRunner._myPyInstallerRunner__parseSettings()

    assert strArgs == test_strPartArgs
# End of test_PyInstallerRunner_ParsePartArgs

