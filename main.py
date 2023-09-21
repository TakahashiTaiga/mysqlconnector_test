import asyncio
from pyhocon import ConfigFactory
from execute_sqls import execute_sqls

async def main_func():
   # read configs
  print('open config')
  conf = ConfigFactory.parse_file('./mysql_config.conf')
  db = conf['db']

  print(db)
  # create instance
  print('create instance')
  exec_sqls = execute_sqls()
  # connect to MySQL
  print('connect to mysql')
  asyncio.gather(execute_sqls.connectToMySQL())
  # execute create tables by the order based on execute_sqls.conf
  print('use db')
  asyncio.gather(execute_sqls.useDB(db))
  print('insert data')
  asyncio.gather(execute_sqls.insertData())
  # close connection to MySQL
  print('close connection')
  exec_sqls.close()

if __name__=='__main__':
  asyncio.run(main_func())
 
  