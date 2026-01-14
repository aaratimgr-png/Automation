# import configparser

# def configRead(section,key):
#     config=configparser.ConfigParser()
#     config.read('../ConfigurationFiles/Config.cfg')

#     return config.get(section,key)
# #print(configRead('Details','APP_URL'))

# def ElementsRead(section,key):
#     config=configparser.ConfigParser()
#     config.read('../ConfigurationFiles/Elements.cfg')
#     return config.get(section,key)

import configparser
import os

config = configparser.ConfigParser()

# Get project root (Selenium Automation)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Absolute path to config.ini
CONFIG_PATH = os.path.join(BASE_DIR, "Library", "config.ini")

# Load config file
if not os.path.exists(CONFIG_PATH):
    raise FileNotFoundError(f"config.ini not found at: {CONFIG_PATH}")

config.read(CONFIG_PATH)

def configRead(section, key):
    if not config.has_section(section):
        raise Exception(f"Missing section [{section}] in config.ini")
    if not config.has_option(section, key):
        raise Exception(f"Missing key '{key}' in section [{section}]")
    return config.get(section, key)
