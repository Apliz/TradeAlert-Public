# simple database to store things in persistent memory
import sqlite3
from abc import ABC, abstractmethod
from . import models
from os import PathLike, path, fspath
from pathlib import Path

class Database(ABC):
    """
    Placeholder documentation.

    """

    @abstractmethod
    def create_table(self,name:str, connection:str) -> None:
        """
        Create new database table for existing sqlite3 database
        """
        pass
    
    @abstractmethod
    def destroy_table(self,name:str, connection:str) -> None:
        """
        Destroy table (name) of an existing database connection
        """
        pass
    
    @abstractmethod
    def connect_database(self, database:str) -> None:
        """
        Connect to an existing database
        """
        if path.isfile(fspath(f'{Path(".")}/{database}.db')):
            # database already exist
            pass
        else:
            # either the file or the directory does not exist and return and error.
            pass

        pass

    @abstractmethod
    def disconnect_database(self, connection:sqlite3.Connection) -> None:
        """
        Close an open database connection
        """
        pass

    @abstractmethod
    def create_record(self, connection:sqlite3.Connection, table:str, data:dict[str,str]) -> None:
        """
        Create new database record.
        """
        pass
    
    @abstractmethod
    def destroy_record(self, connection:sqlite3.Connection, table:str, id:int | str) -> None:
        """
        Destroy and existing database record from a table
        """
        pass

    @staticmethod
    def get_databases(file:str, dir_path:str) -> None:
        """
        Return list of existing databases in file (file) in directory (dir_path)
        """
        pass

    @staticmethod
    def get_tables(connection:str) -> None:
        """
        Return list of exiting tables in a database
        """
        pass





con = sqlite3.connect("credentials.db")
cur = con.cursor()


cur.execute("""CREATE TABLE IF NOT EXISTS users(
    username STRING PRIMARY KEY,
    apiKey STRING,
    password STRING,
    environment STRING,
    UNIQUE(username, apiKey));
""")


cur.execute("""
    INSERT OR IGNORE INTO users(username,apiKey,password,environment) VALUES
        ('plisdemoapi','412de339c1fe6eb45b46e3b489ee6fdb94f8a681','xinzaw-fandum-gydrY4','demo')
""")

cur.execute("""CREATE TABLE IF NOT EXISTS apiSessions(
    username STRING,
    clientId STRING,
    accountId STRING,
    timezoneOffset STRING,
    lightstreamerEndpoint STRING,
    accessToken STRING,
    refreshToken STRING,
    scope STRING,
    tokenType STRING,
    expiresIn STRING,
    FOREIGN KEY (username) REFERENCES users(username),
    UNIQUE(username));
""")


con.commit()
con.close()

