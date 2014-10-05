#!/usr/bin/python
# -*- coding: utf-8 -*-

import os, sys, glob, string
import json
from jubatus.recommender import client
from jubatus.recommender import types
from jubatus.common import Datum

NAME = "recommender_artist";

if __name__ == '__main__':

    # params check
    if len(sys.argv) < 2:
        print 'ERROR: need params'
        sys.exit(0)

    # params
    userid = sys.argv[1]

    recommender = client.Recommender("192.168.33.10", 9199, NAME)
    recommender.clear_row(userid)

