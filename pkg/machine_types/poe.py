#!/usr/bin/env python
#
# Author: Veronica G. Vergara L.
#
#

from .base_jobLauncher import BaseJobLauncher

class Poe(BaseJobLauncher):

    def __init__(self):
        self.__name = 'POE'
        self.__launchCmd = 'poe'
        self.__numTasksOpt = None
        self.__numTasksPerNodeOpt = None
        BaseJobLauncher.__init__(self,self.__name,self.__launchCmd,self.__numTasksOpt,self.__numTasksPerNodeOpt)

if __name__ == '__main__':
    print('This is the POE job launcher class')
