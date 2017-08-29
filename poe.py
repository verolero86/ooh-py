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
        BaseJobLauncher.__init__(self,self.__name)

    def build_job_command(self,total_processes,processes_per_node,processes_per_socket,executable):
        print("Building job command in the POE class")
        job_launch_command = self.__launchCmd + " " + executable + " 1> stdout.txt 2> stderr.txt"
        return job_launch_command

if __name__ == '__main__':
    print('This is the POE job launcher class')
