#!/usr/bin/env python3

import os
import signal
import sys

import daemon
from daemon.pidfile import PIDLockFile
from inotify_simple import INotify, flags

pidfile='/tmp/qutefy.pid'

def cleanup():
    os.remove(pidfile)

with daemon.DaemonContext(
        pidfile=PIDLockFile(pidfile),
        signal_map={signal.SIGTERM: cleanup}
):
    inotify = INotify()
    watch_flags = flags.CREATE | flags.MODIFY
    wd = inotify.add_watch(sys.argv[1], watch_flags)

    while True:
        for event in inotify.read():
            os.system('qutebrowser :config-source')
