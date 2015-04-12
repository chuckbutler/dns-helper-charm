#!/usr/bin/python

import os
import sys

from charmhelpers.core import (
    hookenv,
    host,
)

hooks = hookenv.Hooks()
log = hookenv.log

def refresh_config():
    config = hookenv.config()
    changed = False
    for key in config:
        if config.changed(key):
            log("config['{}'] changed from {} to {}".format(
                key, config.previous(key), config[key]))
            changed = True

    config.save()
    return changed


