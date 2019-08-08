#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 21 10:58:37 2019

@author: MASTER
"""

#write function that reads binary file and return data 
#measure time required 
# this is something you might do if you are running a clour service 
#that build users buy time used
# we will be logging the results and timing the code 

import logging
import time

#create a basic logger with debug level 
#We will use this logger to record both expections and time used 

logging.basicConfig(filename = "E:\\python_Lessons\\problems.log",
                    level = logging.DEBUG)
logger = logging.getlogger()

#define fucntion 
#the input is the path to the binary file 
def read_file_time(path):
    """Read the contents of the file at 'path' and measure time required"""
    #first we record the time the method began 
    start_time = time.time()
    # try to open the binary file and return the contents
    try:
        #by default open assumes you are opening a file in read text mode
        #we will override this default and open the file and read binary mode
        f = open(path, mode = "rb")
# read the contents of the file 
        data = f.read()
        return data 
    except FileNotFoundError as err:
        logger.error(err) # in the event the file does not exist we will logged the error
        raise # instruct py to pass along the file not found error to the user 
    else:
        f.close()
    finally:
        stop_time = time.time() # compute the time required 
        dt = stop_time - start_time
        logger.info("Time required for {file} = {time}".format(file=path,time=dt))
        
        
data = read_file_timed("E:\\python_lessons\\audio_file.wav") # 45 MB file