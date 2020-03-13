# Octopus Eye Tracking

The *Octopus Eye Tracking* package can be used to autonomously estimate what an octopus can see based off of video footage.

The package enables users to create neural networks to estimate the locations of an octopuses eyes using [DeepLabCut](https://github.com/AlexEMG/DeepLabCut). Users must annotate some video frames, then can use the provided job scripts to train networks on the *Disocvery* cluster and analyze full videos.

Annotated video frames can then further analyzed using the python modules `data_loader`,`analyze`, and `visualize`. Estimates of where the octopus is looking are generated and a numeric estimate of how directly an octopus is tracking an object is predicted.

More comprehensive documentation is needed for all of the functions, however the notebook `example_usage.ipynb` shows how users can flexibly use the package to visualize data outputted from a DLC network.

Example data and the data used in `example_usage.ipynb` can be found [here](https://drive.google.com/open?id=1ZaiccLkC3LYrCD31T5pk_TDLzsaNAcWl). `eye_tracking_vid.mp4` is the finalized output from the python modules and was created from `label_data.csv` and `original_video.mp4`. 

## Usage

The following guide specifically utilizes a collection of infrared data. These examples can be run just like the guide, but users will need to modify the scripts to analyze new data.

### Annotating Data

Users must first use [DeepLabCut](https://github.com/AlexEMG/DeepLabCut) to create a project. Users must locally annotate video frames using the provided GUI, then copy the project to *Discovery* using `scp` for training.

See the [DeepLabCut](https://github.com/AlexEMG/DeepLabCut) documentation for project creation and data annotation.


### Further Work

I intend to refine the network with more data in the spring, particularly to identify when the eyes are occluded. With a robust model trained, I can begin to collect data using two cameras for 3D eye-tracking. I have work to do on the repo as far as better documentation, a package structure for the python modules, additional visualization options (including visual field representation, I need to do more literature review), more numerical analyses, and incorporating in the confidence DLC provides with its predictions into my analysis.


### Training

Once a [DeepLabCut](https://github.com/AlexEMG/DeepLabCut) project is copied to *Discovery*, a network can be trained to autonomously annotate frames using the job scripts below (located in `/jobs`). These job scripts submit jobs to *Discovery* and run the scripts located in `/scripts`.

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