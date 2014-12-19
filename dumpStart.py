import os
from config import db_parametrers

a = db_parametrers.origin_abc
b = db_parametrers.destination_xyz

dump_file_name = 'export/temp_db_2.sql'

dump_from_abc = "./utils/expect_dump_schema %s %s %s %s %s %s %s"%(a['db_name'], a['host'], a['port'], a['user'], a['schema'], dump_file_name, a['password'])

restore_to_xyz = "./utils/expect_push_schema %s %s %s %s %s"%(b['db_name'], b['host'], b['user'], dump_file_name, b['password'])

os.system(dump_from_abc)

os.system(restore_to_xyz)