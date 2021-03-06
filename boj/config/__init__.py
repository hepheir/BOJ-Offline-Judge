import configparser
import os
import sys

PACKAGE_ROOT = os.path.dirname(sys.modules['boj'].__file__)
CONFIG_FILE = os.path.join(os.getcwd(), 'boj.config.cfg')

config = configparser.ConfigParser()

config['Paths'] = {
    "tempDirectory": os.path.join(PACKAGE_ROOT, "tmp"),
    "inputFilenamePattern": os.path.join("{srcDirname}", "data", "**", "*.in"),
    "outputFilenamePattern": os.path.join("{srcDirname}", "data", "**", "*.out"),
}

config['Judge'] = {
    "defaultTimeLimit": 10000,
    "briefTime": True,
    "briefDatapath": True,
}

config['Languages'] = {
    "c": {
        "compilerPath": "c:\\MinGW\\bin\\gcc.exe" # use "gcc" if Linux
    },
    "cpp": {
        "compilerPath": "c:\\MinGW\\bin\\g++.exe"
    },
}
