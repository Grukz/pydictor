#!/usr/bin/env python
# coding:utf-8
# pydictor dictionary-handler tool: combiner
"""
Copyright (c) 2016-2017 pydictor developers (https://github.com/LandGrey/pydictor)
License: GNU GENERAL PUBLIC LICENSE Version 3
"""

from __future__ import unicode_literals


import os
import sys
import traceback
import mimetypes
from tools.uniqifer import uniqifer_enter
from lib.fun import finishcounter, finishprinter, cool
from lib.data import CRLF, filextension, get_result_store_path, get_buildtime, COMBINER_prefix


def combiner_enter(directory=os.path.abspath(sys.argv[0]), need_uniqifer=False):
    if not os.path.isdir(os.path.abspath(directory)):
        exit(CRLF + cool.red("[-] path: {} don't exists".format(directory)))
    filepaths = []
    combine_list = []
    storepath = os.path.join(get_result_store_path(), "%s_%s%s" % (COMBINER_prefix, get_buildtime(), filextension))
    for rootpath, subdirsname, filenames in os.walk(directory):
        filepaths.extend([os.path.abspath(os.path.join(rootpath, _)) for _ in filenames])
    if len(filepaths) > 0:
        for _ in filepaths:
            if mimetypes.guess_type(_)[0] == 'text/plain':
                combine_list.append(_)
    try:
        with open(storepath, "a") as f:
            for onefile in combine_list:
                with open(onefile, 'r') as tf:
                    f.write(tf.read())
        if not need_uniqifer:
            finishprinter(finishcounter(storepath), storepath)
        else:
            uniqifer_enter(storepath, from_combiner=True)
    except Exception as ex:
        print(CRLF + cool.red("[-] Combine file failed, Looking: "))
        exit(CRLF + traceback.print_exc())