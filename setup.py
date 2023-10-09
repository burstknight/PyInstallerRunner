from setuptools import find_packages, setup
from PyInstallerRunner.myPyInstallerRunner import __version__

def main():
    with open("README.md", "r", encoding="utf-8") as oReader:
        strLongDescription = oReader.read()
    # End of with-block

    setup(name="PyInstallerRunner",
            version=__version__,
            author="burstknight",
            author_email="burstknight@gmail.com",
            long_description=strLongDescription,
            long_description_content_type="text/markdown",
            url="https://github.com/burstknight/PyInstallerRunner",
            packages=find_packages(),
            entry_points={
                "console_scripts": [
                    "PyInstallerRunner = PyInstallerRunner.myPyInstallerRunner:main"
                    ]
                },
            classifiers=[
                "Programming Language :: Python :: 3",
                "License :: OSI Approved :: MIT ::License",
                "Operating System :: POSIX :: Linux"
                ],
            python_requries=">=3.8",
            install_requires=["pyinstaller>=5.9.0", "pyyaml>=6.0"])
# End of main

if "__main__" == __name__:
    main()
# End f of if-condition
