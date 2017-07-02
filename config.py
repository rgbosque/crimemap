#!/usr/bin/python
from ConfigParser import ConfigParser


def config(filename='database.ini', section='postgresql'):
    # create parser
    parser = ConfigParser()

    # read config file
    parser.read(filename)

    # get section, default postgresql
    db = {}
    if parser.has_section(section):
        params = parser.items(section)

        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception('Section {0} not found in {1} file'.format(section, filename))

    return db
