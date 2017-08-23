#!/usr/bin/env python
#
# Author: Veronica G. Vergara L.
#


class RgtTest():

    def __init__(self):
        self.__total_processes = None
        self.__processes_per_node = None
        self.__processes_per_socket = None
        self.__jobname = None
        self.__batchqueue = None
        self.__walltime = None
        self.__batchfilename = None
        self.__buildscriptname = None
        self.__checkscriptname = None
        self.__reportscriptname = None
        self.__executablename = None
        self.__testinputfile = None
        self.__template_dict = {}
        self.__builtin_dict = {}
        self.__builtin_params = {'total_processes', 'processes_per_node', 'processes_per_socket', 
        'jobname', 'batchqueue', 'walltime', 'batchfilename', 'buildscriptname', 'checkscriptname',
        'executablename', 'reportscriptname', 'testinputfile'}

    def set_test_parameters(self,total_processes, processes_per_node, processes_per_socket, jobname, batchqueue, 
                            walltime, batchfilename, buildscriptname, checkscriptname, executablename, reportscriptname,
                            testinputfile):
        self.__total_processes = total_processes
        self.__processes_per_node = processes_per_node
        self.__processes_per_socket = processes_per_socket
        self.__jobname = jobname
        self.__batchqueue = batchqueue
        self.__walltime = walltime
        self.__batchfilename = batchfilename
        self.__buildscriptname = buildscriptname
        self.__checkscriptname = checkscriptname
        self.__reportscriptname = reportscriptname
        self.__executablename = executablename
        self.__testinputfile = testinputfile

    def set_custom_test_parameters(self,template_dict):
        self.__template_dict = template_dict
        for (k,v) in self.__template_dict.items():
            if k == 'total_processes':
                self.__total_processes = v
            elif k == 'processes_per_node':
                self.__processes_per_node = v
            elif k == 'processes_per_socket':
                self.__processes_per_socket = v
            elif k == 'jobname':
                self.__jobname = v
            elif k == 'batchqueue':
                self.__batchqueue = v
            elif k == 'walltime':
                self.__walltime = v
            elif k == 'batchfilename':
                self.__batchfilename = v
            elif k == 'buildscriptname':
                self.__buildscriptname = v
            elif k == 'checkscriptname':
                self.__checkscriptname = v
            elif k == 'reportscriptname':
                self.__reportscriptname = v
            elif k == 'executablename':
                self.__executablename = v
            elif k == 'testinputfile':
                self.__testinputfile = v
                     
    def check_builtin_parameters(self):
        if (not self.__total_processes 
           or not self.__processes_per_node
           or not self.__processes_per_socket
           or not self.__jobname
           or not self.__batchqueue
           or not self.__walltime
           or not self.__batchfilename
           or not self.__buildscriptname
           or not self.__checkscriptname
           or not self.__reportscriptname
           or not self.__executablename
           or not self.__testinputfile):
            print("")
            print("Required variable(s) missing!")
            print(" total_processes = ",self.__total_processes)
            print(" processes_per_node = ",self.__processes_per_node)
            print(" processes_per_socket = ",self.__processes_per_socket)
            print(" jobname = ",self.__jobname)
            print(" batchqueue = ",self.__batchqueue)
            print(" walltime = ",self.__walltime)
            print(" batchfilename = ",self.__batchfilename)
            print(" buildscriptname = ",self.__buildscriptname)
            print(" checkscriptname = ",self.__checkscriptname)
            print(" reportscriptname = ",self.__reportscriptname)
            print(" executablename = ",self.__executablename)
            print(" testinputfile = ",self.__testinputfile)
            
            exit(1)

    def get_template_dict(self):
        return self.__template_dict

    def get_batchfilename(self):
        return self.__batchfilename
    
    def get_testinputfile(self):
        return self.__testinputfile

    def get_buildscriptname(self):
        return self.__buildscriptname

    def get_checkscriptname(self):
        return self.__checkscriptname

    def get_reportscriptname(self):
        return self.__reportscriptname

    def get_executablename(self):
        return self.__executablename

    def get_jobname(self):
        return self.__jobname

    def get_walltime(self):
        return str(self.__walltime)

    def get_batchqueue(self):
        return self.__batchqueue

    def get_total_processes(self):
        return str(self.__total_processes)

    def get_processes_per_node(self):
        return str(self.__processes_per_node)

    def get_processes_per_socket(self):
        return str(self.__processes_per_socket)

    def print_custom_test_parameters(self):
        print("RGT Test Parameters")
        print("===================")
        for k in self.__template_dict:
            print(k,"=",self.__template_dict[k])

    def print_test_parameters(self):
        print("RGT Test parameters")
        print("===================")
        print("total_processes = " + str(self.__total_processes))
        print("processes_per_node = " + str(self.__processes_per_node))
        print("processes_per_socket = " + str(self.__processes_per_socket))
        print("jobname = " + self.__jobname)
        print("batchqueue = " + self.__batchqueue)
        print("walltime = " + str(self.__walltime))
        print("batchfilename = " + self.__batchfilename)
        print("buildscriptname = " + self.__buildscriptname)
        print("checkscriptname = " + self.__checkscriptname)
        print("reportscriptname = " + self.__reportscriptname)
        print("executablename = " + self.__executablename)
        print("testinputfile = " + self.__testinputfile)

if __name__ == "__main__":
    print('This is the RgtTest class')
