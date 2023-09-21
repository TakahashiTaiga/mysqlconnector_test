import os
from dotenv import load_dotenv
import mysql.connector
from mysql.connector import errorcode


"""
memo
{
    prototype_db = [
        "users",
        "login_sessions",
        "attribute_sets",
        "attributes",
        "categories",
        "files",
        "descriptions"]
}

conf = ConfigFactory.parse_file('./config/execute_sqls.conf')

for c in conf:
  print(type(c)) -> str
  print(c)       -> 'prototype'
  print(conf[c]) -> ['users', 'login_sessions', 'attribute_sets', 'attributes', 'categories', 'files', 'descriptions']
"""

class execute_sqls:  
  """
    class values
      self.mysql_user
      self.mysql_root_password
      self.mysql_port
      self.cnx
      self.cursor
  """
  def __init__(self):
    print('init')
    # get env for connecting mysql
    load_dotenv()
    self.mysql_user = os.getenv('MYSQL_USER')
    self.mysql_root_password = os.getenv('MYSQL_ROOT_PASSWORD')
    self.mysql_port = os.getenv('DB_PORT')

  def connectToMySQL(self):
    """
      no arguments required
      create cnx and cursor
      cnx and cursor are class values
    """
    print('connectToMySQL')
    try:
      # create connect
      self.cnx = mysql.connector.connect(
        user=self.mysql_user,
        password=self.mysql_root_password,
        port=self.mysql_port)
      # create cursor
      self.cursor = self.cnx.cursor()
    
    # throw error
    except mysql.connector.Error as err:
      if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
      elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
      else:
        print(err)

  def useDB(self, db):
    """
      argument: 
        db  database name for use command

      create and execute use command
    """
    print('useDB')
    try:
      # create use command
      use_db = "USE {};".format(db)
      # execute use command
      self.cursor.execute(use_db)
    # throw error
    except mysql.connector.Error as err:
      print(err)
      exit(1)


  def openSQLFile(self):
    """
      argument:
        db    database name
        table table name

      open sql file of specified db and table
      retrun the file
    """
    print('openSqlFile')
    # create file path
    path = "insert_testdata.sql"
    # opne file
    with open(path) as f:
      create_table = f.read()
      # file close before return
      f.close()
      # return file contents
      return create_table
  
  def insertData(self):
    """
      arguments:
        db    create table in this db
        table table created

      get specified sql file contents
      execute the create table 
    """
    print('insertData')
    try:
      # get sql file contents
      insert_data = self.openSQLFile()
      # execute create table
      self.cursor.execute(insert_data)
    # throw error
    except mysql.connector.Error as err:
      print("Failed creating database: {}".format(err))
      exit(1)

  def closeConnection(self):
    """
      no arguments required
      cnx is a class value
      close cnx
      execute_sqls class must use closeConnection at the end of processing
    """
    print('closeConnection')
    self.cnx.close()
      
 