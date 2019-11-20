# -*- coding: utf-8 -*-
"""Dummy package for `{{ module_name }}`."""

from __future__ import print_function, unicode_literals

import os
import sys


def check_call(cmd):
    """Wrapper for functionality of `subprocess.check_call`."""
    return_code = os.system(cmd)
    if return_code != 0:
        raise OSError

# try to reinstall
print(u'This package is a dummy package for `{{ module_name }}`.', file=sys.stderr)
print(u'Trying to reinstall...', file=sys.stderr)
try:
    check_call('%s -m pip uninstall -y {{ name }}' % sys.executable)
    check_call('%s -m pip install {{ module_name }}' % sys.executable)
except OSError:
    print(u'Failed to reinstall...', file=sys.stderr)
    print(u'Please uninstall `{{ name }}` and directly install `{{ module_name }}` instead.', file=sys.stderr)
    sys.exit(1)
print(u'Successfully reinstalled...', file=sys.stderr)

# try to restart
print(u'Trying to restart your program...', file=sys.stderr)
try:
    os.execlp(sys.argv[0], *sys.argv)
except BaseException:
    print(u'Failed to restart your program...', file=sys.stderr)
    print(u'Please manually restart `%s`.' % ' '.join(sys.argv), file=sys.stderr)
    sys.exit(1)