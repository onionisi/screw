from __future__ import absolute_import

from .production import *

try:
    from .development import *
except ImportError as e:
    if e.args[0].startswith('No module named'):
        pass
    else:
        # the ImportError is raised inside local_config
        raise
