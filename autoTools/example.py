# -*- coding: utf-8 -*-
import ConfigParser
import string

config = ConfigParser.ConfigParser()
config.read("./app1.ini")
print string.upper(config.get("模拟器版本选择", "moveToX")),
print "by", config.get("模拟器版本选择", "moveToY"),
print "(" + config.get("模拟器版本选择", "time") + ")"
print
print config.get("info", "app")
print
# print config.sections()
#
for section in config.sections():
    print section
    for option in config.options(section):
        print " ", option, "=", config.get(section, option)
