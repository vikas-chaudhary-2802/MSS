#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

    mslib.mscolab.demodata
    ~~~~~~~~~~~~~~~~~~~~~~

    dummydata for mscolab

    This file is part of mss.

    :copyright: Copyright 2019 Shivashis Padhi
    :copyright: Copyright 2019-2020 by the mss team, see AUTHORS.
    :license: APACHE-2.0, see LICENSE for details.

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

import os
import fs
import sys
from flask import Flask
import logging
import argparse
import git
import psycopg2
import sqlalchemy
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT


try:
    import MySQLdb as ms
except ImportError:
    ms = None
    logging.debug("Failed to import MySQLdb")
from mslib.mscolab.conf import mscolab_settings
from mslib.mscolab.models import User, Project, Permission
from mslib.msui import MissionSupportSystemDefaultConfig as mss_default
from mslib.mscolab.seed import seed_data, create_tables


def create_test_data():
    with fs.open_fs(mscolab_settings.BASE_DIR) as fs_datadir:
        if fs_datadir.exists('colabTestData'):
            fs_datadir.removetree('colabTestData')
        fs_datadir.makedir('colabTestData')
    # creating filedata directory
    create_test_files()
    if mscolab_settings.SQLALCHEMY_DB_URI.split(':')[0] == "mysql":
        if ms is None:
            logging.info("""can't complete demodata setup,
                         use sqlite3 or configure mysql with proper modules""")
            sys.exit(0)
        try:
            db = ms.connect(host=mscolab_settings.DB_HOST,    # your host, usually localhost
                            user=mscolab_settings.DB_USER,         # your username
                            passwd=mscolab_settings.DB_PASSWORD,  # your password
                            db=mscolab_settings.DB_NAME)        # name of the data base
            cursor = db.cursor()
            logging.info("Database exists, please drop it before running mscolab/demodata.py")
            sys.exit(0)
        except Exception as e:
            logging.debug(e)
            db = ms.connect(host=mscolab_settings.DB_HOST, user=mscolab_settings.DB_USER,
                            passwd=mscolab_settings.DB_PASSWORD)
            cursor = db.cursor()
            sql = 'CREATE DATABASE ' + mscolab_settings.DB_NAME + ';'
            cursor.execute(sql)
            db = ms.connect(host=mscolab_settings.DB_HOST,    # your host, usually localhost
                            user=mscolab_settings.DB_USER,         # your username
                            passwd=mscolab_settings.DB_PASSWORD,  # your password
                            db=mscolab_settings.DB_NAME)        # name of the data base
            cursor = db.cursor()

        PATH_TO_FILE = os.getcwd() + '/schema_seed.sql'
        for line in open(PATH_TO_FILE):
            if line.split(' ')[0] not in ['CREATE', 'SET']:
                continue
            cursor.execute(line)

        app = Flask(__name__)
        app.config['SQLALCHEMY_DATABASE_URI'] = mscolab_settings.SQLALCHEMY_DB_URI
        from mslib.mscolab.models import db
        app.config['SECRET_KEY'] = 'secret!'.encode('utf-8')
        db.init_app(app)
        with app.app_context():
            db.create_all()
            data = [
                ('a', 8, 'a', 'a'),
                ('b', 9, 'b', 'b'),
                ('c', 10, 'c', 'c'),
                ('d', 11, 'd', 'd')
            ]
            for data_point in data:
                user = User(data_point[0], data_point[3], data_point[2])
                user.id = data_point[1]
                db.session.add(user)
                db.session.commit()

            data = [
                (1, 'one', 'a, b'),
                (2, 'two', 'b, c'),
                (3, 'three', 'a, c'),
                (4, 'four', 'd')
            ]
            for data_point in data:
                project = Project(data_point[1], data_point[2])
                project.id = data_point[0]
                db.session.add(project)
            db.session.commit()

            data = [
                (1, 8, 1, 'creator'),
                (2, 9, 1, 'collaborator'),
                (3, 9, 2, 'creator'),
                (4, 10, 2, 'collaborator'),
                (5, 10, 3, 'creator'),
                (6, 8, 3, 'collaborator'),
                (7, 10, 1, 'viewer'),
                (8, 11, 4, 'creator')
            ]
            for data_point in data:
                project = Permission(data_point[1], data_point[2], data_point[3])
                db.session.add(project)
            db.session.commit()

        pass
    elif mscolab_settings.SQLALCHEMY_DB_URI.split(':')[0] == "sqlite":
        create_tables(mscolab_settings.SQLALCHEMY_DB_URI)
        seed_data(mscolab_settings.SQLALCHEMY_DB_URI)

    elif mscolab_settings.SQLALCHEMY_DB_URI.split(':')[0] == "postgresql":
        create_postgres_test()


def create_test_files():
    with fs.open_fs(mscolab_settings.DATA_DIR) as fs_datadir:
        if fs_datadir.exists('filedata'):
            fs_datadir.removetree('filedata')
        fs_datadir.makedir('filedata')

    with fs.open_fs(fs.path.join(mscolab_settings.DATA_DIR, 'filedata')) as file_dir:
        # make directories
        file_paths = ['one', 'two', 'three', 'four', 'Admin_Test', 'test_mscolab']
        for file_path in file_paths:
            file_dir.makedir(file_path)
            file_dir.writetext(f'{file_path}/main.ftml', mscolab_settings.STUB_CODE)
            # initiate git
            r = git.Repo.init(fs.path.join(mscolab_settings.DATA_DIR, 'filedata', file_path))
            r.git.clear_cache()
            r.index.add(['main.ftml'])
            r.index.commit("initial commit")


def create_postgres(seed=False):
    try:
        # if database exists it'll create tables
        create_tables(mscolab_settings.SQLALCHEMY_DB_URI)
    except sqlalchemy.exc.OperationalError as e:
        if e.args[0].find("database \"{}\" does not exist".format(mscolab_settings.DB_NAME)) != -1:
            logging.debug("database doesn't exist, creating one")
            con = psycopg2.connect(dbname="template1",
                                   user=mscolab_settings.DB_USER,
                                   host=mscolab_settings.DB_HOST,
                                   password=mscolab_settings.DB_PASSWORD)

            con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

            cur = con.cursor()
            cur.execute("CREATE DATABASE {};".format(mscolab_settings.DB_NAME))
            create_tables(mscolab_settings.SQLALCHEMY_DB_URI)
            if seed:
                seed_data(mscolab_settings.SQLALCHEMY_DB_URI)


def create_postgres_test():
    con = psycopg2.connect(dbname="template1",
                           user=mscolab_settings.DB_USER,
                           host=mscolab_settings.DB_HOST,
                           password=mscolab_settings.DB_PASSWORD)

    con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

    cur = con.cursor()
    cur.execute("DROP DATABASE IF EXISTS {};".format(mscolab_settings.DB_NAME))
    cur.execute("CREATE DATABASE {};".format(mscolab_settings.DB_NAME))
    create_tables(mscolab_settings.SQLALCHEMY_DB_URI)
    # to reset cursors
    con = psycopg2.connect(dbname=mscolab_settings.DB_NAME,
                           user=mscolab_settings.DB_USER,
                           host=mscolab_settings.DB_HOST,
                           password=mscolab_settings.DB_PASSWORD)

    con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

    cur = con.cursor()
    cur.execute("ALTER SEQUENCE users_id_seq RESTART WITH 4;")
    cur.execute("ALTER SEQUENCE projects_id_seq RESTART WITH 4;")
    cur.execute("ALTER SEQUENCE permissions_id_seq RESTART WITH 11;")
    seed_data(mscolab_settings.SQLALCHEMY_DB_URI)


def create_data():
    create_mssdir()
    with fs.open_fs(mscolab_settings.BASE_DIR) as fs_datadir:
        if not fs_datadir.exists('colabdata/filedata'):
            fs_datadir.makedir('colabdata/filedata')
    if mscolab_settings.SQLALCHEMY_DB_URI.split(':')[0] == "sqlite":
        create_tables(mscolab_settings.SQLALCHEMY_DB_URI)
    elif mscolab_settings.SQLALCHEMY_DB_URI.split(':')[0] == "postgresql":
        create_postgres()


def create_mssdir():
    basename = fs.path.basename(mss_default.mss_dir)
    with fs.open_fs('~') as fs_datadir:
        if not fs_datadir.exists(basename):
            fs_datadir.makedir(basename)


def delete_test_data(temp_fs):
    temp_fs.clean()


def main():
    parser = argparse.ArgumentParser(description="Tool to setup data for usage of mscolab")
    parser.add_argument("--test", action="store_true", help="setup test data")
    parser.add_argument("--init", action="store_true", help="setup deployment data")
    args = parser.parse_args()
    if args.test:
        create_test_data()
    elif args.init:
        create_data()
    else:
        print("for help, use -h flag")


if __name__ == '__main__':
    main()
