# Octopus Eye Tracking

The *Octopus Eye Tracking* package can be used to autonomously estimate what an octopus can see based off of video footage.

The package enables users to create neural networks to estimate the locations of an octopuses eyes using `DeepLabCut`. Users must annotate some video frames, then can use the provided job scripts to train networks on the *Disocvery* cluster and analyze full videos.

Annotated video frames can then be inputed into `octo_track` for further analysis. Estimates of what the octopus can see are generated and a numeric estimate of how directly an octopus is tracking an object is predicted. The `octo_track` package is yet to be neatly composed, however the bulk of the code it will contain is located in `eye_tracking.ipynb`.


## Usage

### Annotating Data

Users must first use `DeepLabCut` to create a project. Users must locally annotate video frames using the provided GUI, then copy the project to *Discovery* using `scp` for training.

See the `DeepLabCut` documentation for project creation and data annotation.


### Training

Once a `DeepLabCut` project is copied to *Discovery*, a network can be trained to autonomously annotate frames using the job scripts below (located in `/jobs`). These job scripts submit jobs to *Discovery* and run the scripts located in `/scripts`.

Bash commands can be run to directly run the same `scripts`, however these commands do not use the job scheduling system and are not advised to be used outside of basic testing of the scripts.

### Using the proper PBS job submission method:


**Training Test:**
`mksub jobs/ir/test_train.pbs`

**Network Training:**
`mksub jobs/ir/train.py`

**Network Evaluation:**
`mksub jobs/ir/eval.pbs`

**Analyzing and annotating videos:**
`mksub jobs/ir/vids.pbs`


### Using the `nohup &` method:

**Training Test (small number of iterations):**
`nohup singularity exec --nv deeplabcut/sandbox_dlc/ python3 scripts/ir/test_train.py &`

**Network Training:**
`nohup singularity exec --nv deeplabcut/sandbox_dlc/ python3 scripts/ir/train.py &`

**Network Evaluation:**
`nohup singularity exec --nv deeplabcut/sandbox_dlc/ python3 scripts/ir/eval.py &`

**Analyzing and annotating videos:**
`nohup singularity exec --nv deeplabcut/sandbox_dlc/ python3 scripts/ir/vid.py /dartfs-hpc/rc/home/7/f002qw7/thesis/ir_test-markt-2020-02-28/videos/ir1.MP4 /dartfs-hpc/rc/home/7/f002qw7/thesis/ir_test-markt-2020-02-28/videos/ir2.MP4 /dartfs-hpc/rc/home/7/f002qw7/thesis/ir_test-markt-2020-02-28/videos/ir3.MP4 &`