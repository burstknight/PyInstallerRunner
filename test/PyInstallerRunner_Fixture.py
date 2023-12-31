from typing import Dict
import pytest
from argparse import Namespace

@pytest.fixture()
def test_dctDefaultSettings() -> Dict:
    dctSettings = {}
    dctSettings["BuildPath"] = {"DistPath": "./bin/release", "SpecPath": "./bin", "WorkPath": "./bin/build", "IconPath": ""}
    dctSettings["CompileConfig"] = {"IsFile": True, "NeedShowConsole": True, "AppName": "Application", "Resources": []}

    return dctSettings
# End of test_dctDefaultSettings

@pytest.fixture()
def test_dctCompleteSettings() -> Dict:
    dctSettings = {}
    dctSettings["BuildPath"] = {"DistPath": "./build/release", "SpecPath": "./build", "WorkPath": "./build/tmp", "IconPath": "./resources/image.icon"}
    dctSettings["CompileConfig"] = {"IsFile": False, "NeedShowConsole": True, "AppName": "MyApp", "Resources": [{"Source": "./resources/config.cfg", "Target": "resources/"}, {"Source": "./data/", "Target": "data"}, {"Source": "./version.txt", "Target": "."}]}

    return dctSettings
# End of test_dctCompleteSettings

@pytest.fixture()
def test_dctPartSettings():
    dctSettings = {}
    dctSettings["BuildPath"] = {"DistPath": "./bin/release", "SpecPath": "./bin", "WorkPath": "./build/tmp", "IconPath": "./resources/image.icon"}
    dctSettings["CompileConfig"] = {"IsFile": True, "NeedShowConsole": False, "AppName": "Application", "Resources": []}

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

@pytest.fixture()
def test_dctApp01Cofig_file() -> Dict[str, str]:
    dctConfig = {}
    dctConfig["source"] = "./test/examples/myApp01/myApp01.py"
    dctConfig["config"] = "./test/examples/myApp01/config_file.yaml"
    dctConfig["bin"] = "./test/examples/bin/release/myApp01_file"
    dctConfig["app"] = "myApp01_file"

    return dctConfig
# End of test_dctApp01Cofig_file

@pytest.fixture()
def test_dctApp01Cofig_dir() -> Dict[str, str]:
    dctConfig = {}
    dctConfig["source"] = "./test/examples/myApp01/myApp01.py"
    dctConfig["config"] = "./test/examples/myApp01/config_dir.yaml"
    dctConfig["bin"] = "./test/examples/bin/release/myApp01_dir"
    dctConfig["app"] = "myApp01_dir"
    
    return dctConfig
# End of test_dctApp01Cofig_dir

@pytest.fixture()
def test_dctApp02Cofig_file() -> Dict[str, str]:
    dctConfig = {}
    dctConfig["source"] = "./test/examples/myApp02/myApp02.py"
    dctConfig["config"] = "./test/examples/myApp02/config_file.yaml"
    dctConfig["bin"] = "./test/examples/bin/release/myApp02_file"
    dctConfig["app"] = "myApp02_file"

    return dctConfig
# End of test_dctApp02Cofig_file

@pytest.fixture()
def test_dctApp02Cofig_dir() -> Dict[str, str]:
    dctConfig = {}
    dctConfig["source"] = "./test/examples/myApp02/myApp02.py"
    dctConfig["config"] = "./test/examples/myApp02/config_dir.yaml"
    dctConfig["bin"] = "./test/examples/bin/release/myApp02_dir"
    dctConfig["app"] = "myApp02_dir"
    
    return dctConfig
# End of test_dctApp02Cofig_dir

@pytest.fixture()
def test_dctCopyResourcesFailed() -> Dict:
    dctResource = {}
    dctResource["BuildPath"] = "./test"
    dctResource["Resources"] = [{"Source": "bug_code.pyxxx", "Target": "."}]

    return dctResource
# End of test_dctCopyResourcesFailed

@pytest.fixture()
def test_dctCommandArgs_Default() -> Dict:
    dctCommandArgs = {}
    dctCommandArgs["command"] = ["myApp.py"]
    dctCommandArgs["args"] = Namespace(source_path="myApp.py", config_path="")

    return dctCommandArgs
# End of test_dctCommandArgs_Default

@pytest.fixture()
def test_dctCommandArgs_Config() -> Dict:
    dctCommandArgs = {}
    dctCommandArgs["command"] = ["myApp.py", "-c", "config.yaml"]
    dctCommandArgs["args"] = Namespace(source_path="myApp.py", config_path="config.yaml")

    return dctCommandArgs
# End of test_dctCommandArgs_Config

@pytest.fixture()
def test_dctCommandArgs_Build() -> Dict:
    dctCommandArgs = {}
    dctCommandArgs["args"] = Namespace(source_path="./test/examples/myApp01/myApp01.py", config_path="./test/examples/myApp01/config_dir.yaml")
    dctCommandArgs["bin"] = "./test/examples/bin/release/myApp01_dir"
    dctCommandArgs["app"] = "myApp01_dir"

    return dctCommandArgs
# End of test_dctCommandArgs_Build
