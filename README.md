* Mark Taylor Thesis README



* Usage


Using the `nohup &` method:



(NOTE: check time it takes to run this so PBS job submission time can be determined)
Training Test (small number of iterations):
`nohup singularity exec --nv deeplabcut/sandbox_dlc/ python3 scripts/ir/test_train.py &`

Network Training:
`nohup singularity exec --nv deeplabcut/sandbox_dlc/ python3 scripts/ir/train.py &`

Network Evaluation:
`nohup singularity exec --nv deeplabcut/sandbox_dlc/ python3 scripts/ir/eval.py &`

Analyzing and annotating videos:
`nohup singularity exec --nv deeplabcut/sandbox_dlc/ python3 scripts/ir/vid.py /dartfs-hpc/rc/home/7/f002qw7/thesis/ir_test-markt-2020-02-28/videos/ir1.MP4 /dartfs-hpc/rc/home/7/f002qw7/thesis/ir_test-markt-2020-02-28/videos/ir2.MP4 /dartfs-hpc/rc/home/7/f002qw7/thesis/ir_test-markt-2020-02-28/videos/ir3.MP4 &`



Using the proper PBS job submission method:


Training Test:
`mksub jobs/ir/test_train.pbs`

Network Training:
`mksub jobs/ir/train.py`

Network Evaluation:
`mksub jobs/ir/eval.pbs`

Analyzing and annotating videos:
`mksub jobs/ir/vids.pbs