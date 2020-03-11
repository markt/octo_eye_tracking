import sys
import os
os.environ["DLClight"] = "True"
import deeplabcut
config_path = '/dartfs-hpc/rc/home/7/f002qw7/thesis/ir_test-markt-2020-02-28/config.yaml' 
os.system('echo NEW')
deeplabcut.evaluate_network(config_path,Shuffles=[1], plotting=True)
os.system('echo analyzed!')
