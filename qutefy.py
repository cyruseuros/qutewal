#!/usr/bin/env python3

import os, sys
from inotify_simple import INotify, flags
import daemon

with daemon.DaemonContext():
    inotify = INotify()
    watch_flags = flags.CREATE | flags.MODIFY
    wd = inotify.add_watch(sys.argv[1], watch_flags)

    while True:
        for event in inotify.read():
            os.system('qutebrowser :config-source')
