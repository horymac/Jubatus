#!/usr/bin/python
# -*- coding: utf-8 -*-

import os, sys, glob, string
import json
from jubatus.recommender import client
from jubatus.recommender import types
from jubatus.common import Datum

try:
    import sqlite3
except ImportError:
    print 'need sqlite3 installed'
    sys.exit(0)


NAME = "recommender_artist";

if __name__ == '__main__':

    # params check
    if len(sys.argv) < 3:
        print 'ERROR: need params'
        sys.exit(0)

    # params
    userid = sys.argv[1]
    artistid = sys.argv[2]

    train_data = Datum({
        "artist": artistid
        })
    
    print train_data

    recommender = client.Recommender("192.168.33.10", 9199, NAME)
    recommender.update_row(userid, train_data)

    #row = recommender.decode_row(userid)
    #complete_row = recommender.complete_row_from_id(userid)
    similar_row = recommender.similar_row_from_id(userid,5)
    #print row
    #print complete_row
    print similar_row

