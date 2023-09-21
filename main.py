from pyhocon import ConfigFactory
from execute_sqls import execute_sqls

if __name__=='__main__':
  # read configs
  print('open config')
  conf = ConfigFactory.parse_file('./mysql_config.conf')
  db = conf['db']
  
  # create instance
  print('create instance')
  exec_sqls = execute_sqls()
  # connect to MySQL
  print('connect to mysql')
  exec_sqls.connectToMySQL()
  # execute create tables by the order based on execute_sqls.conf
  print('insert data')
  exec_sqls.insertData()
  # close connection to MySQL
  print('close connection')
  exec_sqls.close()