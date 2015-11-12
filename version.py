# -*- coding: utf-8 -*-
# x.y.z.svn
# x major release : major change in architecture / feature
# y minor release : significant feature addition
# z development number : bug fix, documentation update, refactoring
# svn commit number
# svn propset svn:keywords "Revision" version.py
# this will replace $revision$ with the real version after every commit

__version__ = '0.0.1.'+'$Revision: 0 $'.split(':')[1].split('$')[0].strip()



