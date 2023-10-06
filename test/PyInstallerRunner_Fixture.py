from typing import Dict
import pytest

@pytest.fixture()
def test_dctDefaultSettings() -> Dict:
    dctSettings = {}
    dctSettings["BuildPath"] = {"DistPath": "./bin/release", "SpecPath": "./bin", "WorkPath": "./bin/build", "IconPath": ""}
    dctSettings["CompileConfig"] = {"IsFile": True, "NeedShowConsole": True, "AppName": "Application"}

    return dctSettings
# End of test_dctDefaultSettings

@pytest.fixture()
def test_dctCompleteSettings() -> Dict:
    dctSettings = {}
    dctSettings["BuildPath"] = {"DistPath": "./build/release", "SpecPath": "./build", "WorkPath": "./build/tmp", "IconPath": "./resources/image.icon"}
    dctSettings["CompileConfig"] = {"IsFile": False, "NeedShowConsole": True, "AppName": "MyApp"}

    return dctSettings
# End of test_dctCompleteSettings

@pytest.fixture()
def test_dctPartSettings():
    dctSettings = {}
    dctSettings["BuildPath"] = {"DistPath": "./bin/release", "SpecPath": "./bin", "WorkPath": "./build/tmp", "IconPath": "./resources/image.icon"}
    dctSettings["CompileConfig"] = {"IsFile": True, "NeedShowConsole": False, "AppName": "Application"}

    return dctSettings
# End of test_dctPartSettings

@pytest.fixture()
def test_strDefaultArgs() -> str:
    return "-F -n \"Application\" --distpath \"./bin/release\" --specpath \"./bin\" --workpath \"./bin/build\" "
# End of test_strDefaultArgs

@pytest.fixture()
def test_strCompleteArgs() -> str:
    return "-D -n \"MyApp\" --distpath \"./build/release\" --specpath \"./build\" --workpath \"./build/tmp\" -i \"./resources/image.icon\" "
# End of test_strCompleteArgs

@pytest.fixture()
def test_strPartArgs() -> str:
    return "-F -w -n \"Application\" --distpath \"./bin/release\" --specpath \"./bin\" --workpath \"./build/tmp\" -i \"./resources/image.icon\" "
# End of test_strPartArgs

