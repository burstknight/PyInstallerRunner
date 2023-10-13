# PyInstallerRunner
This repo is a tool that can load configuration file to use `PyInstaller` to build python code as an executable file.

## Requirments
This repo uses `Python 3.8` to develop, so you must install python `3.8` or later version. This repo need install the python packages:
Package Name 	| Version
----------------|----------------------
`pyinstaller` 	| `>=5.9.0`
`pyyaml` 		| `>=6.0`

This repo need use `pytest` for unit test, so you should use these commands to install necessary modules:
```sh
$ pip3 install pytest
$ pip3 install pytest-cov
$ pip3 install pytest-mock
```

### Install
You can use two ways to install this repo:
1. Use `pip` install this repo:
	- For linux:
	```sh
	pip3 install git+https://github.com/burstknight/PyInstallerRunner.git@release
	```
	- For windows:
	```batch
	pip install git+https://github.com/burstknight/PyInstallerRunner.git@release
	```
2. Clone this repo to install:
```sh
git clone git@github.com:burstknight/PyInstallerRunner.git
cd PyInstallerRunner
python setup.py install
```

## Usage
### Configuration File
This repo need use `*.yaml` file as the configuration file to build python code as an executable file. You can edit your `*.yaml` file to build your python code if you need.

The configuration file contains two parts:
- `BuildPath`: Set the paths for building python code file.
- `CompileConfig`: Set the settings for building.

Here is a table for `BuildPath`:
Key 		| Type 		| Default 			| Description
------------|-----------|-------------------|----------------------------------------------------------------
`DistPath` 	| `string`	| `./bin/release` 	| Set the target release path. This repo will store the built executable file into the path.
`SpecPath` 	| `string` 	| `./bin/` 			| The setting file will store into this path for `PyInstaller`.
`WorkPath` 	| `string` 	| `./bin/build` 	| All temporary files will store into this path during bulding python code file.
`IconPath` 	| `string` 	| `""` 				| Set the icon file path. The default is empty string.

Here is a table for `CompileConfig`:
Key 				| Type 		| Default 			| Description
--------------------|-----------|-------------------|----------------------------------------------------------------
`IsFile` 			| `boolean` | `true` 			| This repo will build the given python code file as an executable file if this flag is set `true`. Otherwise, this repo will create a directory to store the executable file and all necessary dependent files.
`NeedShowConsole` 	| `boolean` | `true` 			| The built executable file will show a console during running if this flag is set `true`. Otherwise, the built executable file will not show a console. Note, if you want to develop a GUI program for windows, this flag should be set `false`.
`AppName` 			| `string` 	| `Application` 	| Set the file name for the executable file.
`Resources` 		| `list` 	| `[]` 				| Set the list fo the resource files. Each item in the list need set the source path with the key `Source` and the target path with the key `Target`. All the resource files will copy into `DistPath`. Note, if `Target` is set `.`, the resource file or directory will copy into the target release path, and otherwise this repo will create a subdirectory to put the resource file or directory.

Here is a complete `*.yaml` file example:
```yaml
BuildPath:
  DistPath: ./bin/release
  SpecPath: ./bin
  WorkPath: ./bin/build
  IconPath: ./resources/image.icon
CompileConfig:
  IsFile: false
  NeedShowConsole: true
  AppName: MyApp
  Resources:
    - Source: ./resources/config.cfg
      Target: resources/
    - Source: ./data/
      Target: .
    - Source: ./version.txt
      Target: .
```

If you need, you can edit a complete `*.yaml` file to set build configuration. However, maybe you want to change few settings instead of complete settings. That's OK. You can edit a incomplete `*.yaml` file. Here is an incomplete example:
```yaml
BuildPath:
  WorkPath: ./build/tmp
  IconPath: ./resources/image.icon
CompileConfig:
  IsFile: true
  NeedShowConsole: false
```

If you offer an incomplete `*.yaml` file, this repo will use default for the remained settings. Of course, you can use all default settings to build your python code if you don't edit your `*.yaml` file.

### Terminal Tool
This repo offers a terminal tool to use `PyInstaller` to build python code file.

If you want to get the usage for the terminal tool, you can use the command:
```sh
$ PyInstallerRunner -h
```

You can use the command to build your python code file without any `*.yaml` file:
```
$ PyInstallerRunner <source_path>
```
where `<source_path>` is your python code file path.

If you edit your `*.yaml` file, you can use the command to build your python code file:
```sh
$ PyInstallerRunner -c <config_path> <source_path>
```
where `<config_path>` is your `*.yaml` file path.

