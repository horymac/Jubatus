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
    #row = recommender.decode_row(userid)
    #print row
    #complete_row = recommender.complete_row_from_id(userid)
    similar_row = recommender.similar_row_from_id(userid,5)

    #print complete_row
    print similar_row



