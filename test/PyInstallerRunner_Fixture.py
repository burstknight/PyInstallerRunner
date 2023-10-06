from typing import Dict
import pytest

@pytest.fixture()
def test_dctDefaultSettings() -> Dict:
    dctSettings = {}
    dctSettings["BuildPath"] = {"DistPath": "./bin/release", "SpecPath": "./bin", "WorkPath": "./bin/build", "IconPath": ""}
    dctSettings["Args"] = {"IsFile": True, "NeedShowConsole": True}

    return dctSettings
# End of test_dctDefaultSettings

@pytest.fixture()
def test_dctCompleteSettings() -> Dict:
    dctSettings = {}
    dctSettings["BuildPath"] = {"DistPath": "./build/release", "SpecPath": "./build", "WorkPath": "./build/tmp", "IconPath": "./resources/image.icon"}
    dctSettings["Args"] = {"IsFile": False, "NeedShowConsole": True}

    return dctSettings
# End of test_dctCompleteSettings

@pytest.fixture()
def test_dctPartSettings():
    dctSettings = {}
    dctSettings["BuildPath"] = {"DistPath": "./bin/release", "SpecPath": "./bin", "WorkPath": "./build/tmp", "IconPath": "./resources/image.icon"}
    dctSettings["Args"] = {"IsFile": True, "NeedShowConsole": False}

    return dctSettings
# End of test_dctPartSettings

@pytest.fixture()
def test_strDefaultArgs() -> str:
    return "-F --distpath \"./bin/release\" --specpath \"./bin\" --workpath \"./bin/build\" "
# End of test_strDefaultArgs

@pytest.fixture()
def test_strCompleteArgs() -> str:
    return "-D --distpath \"./build/release\" --specpath \"./build\" --workpath \"./build/tmp\" -i \"./resources/image.icon\" "
# End of test_strCompleteArgs

@pytest.fixture()
def test_strPartArgs() -> str:
    return "-F -w --distpath \"./bin/release\" --specpath \"./bin\" --workpath \"./build/tmp\" -i \"./resources/image.icon\" "
# End of test_strPartArgs

