#!/usr/bin/env python
# vim:fileencoding=utf-8

import sys
import os

from root import app
app.debug = True
app.run(host='0.0.0.0')
