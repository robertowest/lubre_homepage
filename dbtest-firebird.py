# ./manage.py shell < dbtest-firebird.py

# instalación del cliente 
# sudo apt install libfbclient2
# firebird-libfbclient

import sys
from django.conf import settings
from django.db import connections
from django.db.utils import OperationalError

try:
    db_conn = connections['firebird']
    c = db_conn.cursor()
    print('  ..... éxito')
    c.execute("select * from asientos")
    c.fetchone()
except Exception as err:
    print('  ..... ', err)
finally:
    db_conn.close()    
