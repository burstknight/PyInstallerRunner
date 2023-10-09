from test.PyInstallerRunner_Fixture import test_dctCommandArgs_Default, test_dctCommandArgs_Config, test_dctCommandArgs_Build
from pytest import mark
from PyInstallerRunner.myPyInstallerRunner import main, parseArgs
from test.test_PyInstallerRunner_Build import runApp
from unittest.mock import patch

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

@mark.Command
def test_main_Build(test_dctCommandArgs_Build):
    with patch("PyInstallerRunner.myPyInstallerRunner.parseArgs") as oMocker:
        oMocker.return_value = test_dctCommandArgs_Build["args"]
        main()
        
        assert 0 == runApp(test_dctCommandArgs_Build["bin"], test_dctCommandArgs_Build["app"])
    # End of with-block
# End of test_main_Build
