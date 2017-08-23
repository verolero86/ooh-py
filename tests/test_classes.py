#!/usr/bin/env python

from ..machine_types.cray_xk7 import CrayXK7 
from ..machine_types.ibm_power8 import IBMpower8
from ..machine_types.machine_factory import MachineFactory
from ..machine_types.lsf import LSF
from ..machine_types.pbs import PBS
from ..machine_types.aprun import Aprun
from ..machine_types.poe import Poe

#my_machine = CrayXK7('Chester','PBS','aprun',80,1,16)
#print my_machine.get_machine_name()
#my_machine.print_machine_info()
#
#my_machine = IBMpower8('Crest','LSF','poe',4,1,22)
#print my_machine.get_machine_name()
#my_machine.print_machine_info()

#fc = MachineFactory.create_machine('Chester','XK7','PBS')
fc = MachineFactory.create_machine('./somedir','12345')
print(fc)
fc.make_custom_batch_script()

#my_scheduler = LSF()
#print my_scheduler.get_scheduler_name()
#my_scheduler.print_scheduler_info()
#my_scheduler = PBS()
#print my_scheduler.get_scheduler_name()
#my_scheduler.print_scheduler_info()
#
#my_job_launcher = Aprun()
#my_job_launcher.print_jobLauncher_info()
#
#my_job_launcher = Poe()
#my_job_launcher.print_jobLauncher_info()
