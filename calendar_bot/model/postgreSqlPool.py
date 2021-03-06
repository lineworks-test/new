#!/bin/env python
# -*- coding: utf-8 -*-

import psycopg2
import psycopg2.extras as extras
from psycopg2.errors import DuplicateTable
from DBUtils.PooledDB import PooledDB
from DBUtils.PersistentDB import PersistentDB
from calendar_bot.constant import DB_CONFIG


class PostGreSql:
    __pool = None
    _conn = None
    _cursor = None

    def __init__(self):
        return

    def cursor(self):
        self._conn = PostGreSql.__get_conn()
        self._cursor = self._conn.cursor()
        return self._cursor

    def commit(self):
        self._conn.commit()

    def rollback(self):
        self._conn.rollback()

    def execute(self, sql):
        self._cursor.execute(sql)

    def fetchall(self):
        return self._cursor.fetchall()

    def fetchone(self):
        return self._cursor.fetchone()

    def close(self):
        self._conn.close()
        self._cursor.close()

    def __enter__(self):
        # Code to start a new transaction
        return self.cursor()

    def __exit__(self, type, value, tb):
        if tb is None:
            # No exception, so commit
            self.commit()
        else:
            # Exception occurred, so rollback.
            self.rollback()
            # return False
        self.close()

    @staticmethod
    def __get_conn():
        if PostGreSql.__pool is None:
            __pool = PooledDB(creator=psycopg2, mincached=1, maxcached=20,
                              host=DB_CONFIG["host"],
                              port=DB_CONFIG["port"],
                              user=DB_CONFIG["user"],
                              password=DB_CONFIG["password"],
                              database=DB_CONFIG["dbname"],
                              sslmode=DB_CONFIG["sslmode"])
        return __pool.connection()
