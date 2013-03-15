'''
Created on Mar 6, 2013

@author: papachan
'''
from daemon.daemon import Daemon
import httplib
import urllib
import sys
import time

settings = {
    'home': "/",
    'devnull': "/etc/null"
}

class MyDaemon(Daemon):
    def run(self):
        while True:
            time.sleep(1)

#class Build:
#    def run(self):
#        self.realbot = MyDaemon()
#        print "hello"
        

if __name__ == '__main__':
    print settings['devnull'] 
#    daemon = MyDaemon('/tmp/')
