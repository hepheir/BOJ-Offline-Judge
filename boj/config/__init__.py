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

config['language'] = {
    "c": {
        "compilerPath": "c:\\MinGW\\bin\\gcc.exe" # use "gcc" if Linux
    },
    "cpp": {
        "compilerPath": "c:\\MinGW\\bin\\g++.exe"
    },
}

if not os.path.exists(CONFIG_FILE):
    with open(CONFIG_FILE, 'w') as configfile:
        config.write(configfile)
