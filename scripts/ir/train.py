import os
os.environ["DLClight"] = "True"
import deeplabcut
os.system('echo $$')
os.system('echo imported')
config_path = '/dartfs-hpc/rc/home/7/f002qw7/thesis/ir_test-markt-2020-02-28/config.yaml'
os.system('echo config_path')
deeplabcut.train_network(config_path)
os.system('echo done')
