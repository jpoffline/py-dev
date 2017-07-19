
""" Sales app config """

import lib.services.hostinfo as hostinfo
assets_dir = 'assets'
OWNER = hostinfo.get_hostname()
APPNAME = 'Sales log'

SALES_db = 'app/data/db/sales.db'
SALES_tb = 'sales'

USERS_db = 'app/data/db/users.db'
USERS_tb = 'users'