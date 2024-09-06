#!/usr/bin/env python

import sys
import site

site.addsitedir('/var/www/backend_test/.venv/lib/python3.12/site-packages')

sys.path.insert(0, '/var/www/backend_test')

from app import app as application
