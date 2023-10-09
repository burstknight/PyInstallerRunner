from test.PyInstallerRunner_Fixture import test_dctCommandArgs_Default, test_dctCommandArgs_Config
from pytest import mark
from PyInstallerRunner.myPyInstallerRunner import parseArgs

@mark.Command
def test_parseArgs_Default(test_dctCommandArgs_Default):
    oArgs = parseArgs(test_dctCommandArgs_Default["command"])

    assert oArgs == test_dctCommandArgs_Default["args"]
# End of test_parseArgs

@mark.Command
def test_parseArgs_Config(test_dctCommandArgs_Config):
    oArgs = parseArgs(test_dctCommandArgs_Config["command"])

    assert oArgs == test_dctCommandArgs_Config["args"]
# End of test_strDefaultArgs_Config
