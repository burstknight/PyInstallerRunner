import pytest
from PyInstallerRunner.myPyInstallerRunner import myPyInstallerRunner
from test.PyInstallerRunner_Fixture import test_dctDefaultSettings, test_dctCompleteSettings, test_dctPartSettings

def test_PyInstallerRunner_SucceedDefault(test_dctDefaultSettings):
    oRunner = myPyInstallerRunner()
    assert oRunner.m_dctSettings == test_dctDefaultSettings
# End of test_PyInstallerRunner_succeed_default

def test_PyInstallerRunner_SucceedComplete(test_dctCompleteSettings):
    oRunner = myPyInstallerRunner()
    oRunner.loadSetting("./test/configs/complete_config.yaml")

    assert oRunner.m_dctSettings == test_dctCompleteSettings
# End of test_PyInstallerRunner_succeed_complete

def test_PyInstallerRunner_SucceedPart(test_dctPartSettings):
    oRunner = myPyInstallerRunner()
    oRunner.loadSetting("./test/configs/part_config.yaml")

    assert oRunner.m_dctSettings == test_dctPartSettings
# End of test_PyInstallerRunner_succeed_part

def test_PyInstallerRunner_KeyNoExists():
    with pytest.raises(KeyError):
        oRunner = myPyInstallerRunner()
        oRunner.loadSetting("./test/configs/no_key_config.yaml")
    # End of with-block
# End of test_PyInstallerRunner_KeyNoExists

def test_PyInstallerRunner_setSettingTree_dctYamlTree_error():
    with pytest.raises(TypeError):
        oRunner = myPyInstallerRunner()
        oRunner._myPyInstallerRunner__setSettingTree(1, {})
    # End of with-block
# End of test_PyInstallerRunner_setSettingTree_dctYamlTree_error

def test_PyInstallerRunner_setSettingTree_dctSettingTree_error():
    with pytest.raises(TypeError):
        oRunner = myPyInstallerRunner()
        oRunner._myPyInstallerRunner__setSettingTree({}, 1)
    # End of with-block
# End of test_PyInstallerRunner_setSettingTree_dctYamlTree_error

def test_PyInstallerRunner_EmptyConfig(test_dctDefaultSettings):
    oRunner = myPyInstallerRunner()
    oRunner.loadSetting("./test/configs/empty_config.yaml")

    assert oRunner.m_dctSettings == test_dctDefaultSettings
# End of test_PyInstallerRunner_EmptyConfig

def test_PyInstallerRunner_NotFoundFile():
    with pytest.raises(FileNotFoundError):
        oRunner = myPyInstallerRunner()
        oRunner.loadSetting("test")
    # End of with-block
# End of test_PyInstallerRunner_NotFoundFile

