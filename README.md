# DIC_LIPEC
Python package to perform stereo calibration for Digital Image Correlation (DIC)

# Main features

* The package is built using Python 3.7.6 consisting of three different functions.
* Function CaptureFrames() is used to setup the dual webcam framework required for DIC. Following this the webcams are used to capture frames of the calibration pattern for different rotations of the pattern.
* Function SingleSurfaceCalibration() is used for stereo calibration involving only one calibration pattern, i.e., a single grid.
* Function DoubleSurfaceCalibration() is used for stereo calibration involving two calibration patterns, i.e., two grids.

# Quickstart

If you know what you're doing, then this section is for you. Otherwise, you should go to the `Getting Started` section.

#### Windows:

```
sudo apt install python3-pip python3-venv
git clone https://github.com/stochasticmaterialism/Digital-Image-Correlation-DIC-/tree/DIC_LIPEC/DIC_LIPEC
pip install -r requirements.txt
cd DIC
python setup.py install
```

Basic usage:
```
from DIC_LIPEC import *
```

# Getting started

## Installation

The following pieces of software are required to implement the package:

* Python 3.6 or higher
* A Python editing platform like Jupyter Notebook which comes as a part of the Anaconda Distribution

The list of necessary python packages is provided in the `requirements.txt` file and can be installed using pip:
```
pip install -r requirements.txt
```
# Function description
```yaml
from DIC_LIPEC import CaptureFrames
CaptureFrames(stamp)

Input
stamp: This parameter defines the delay between two webcams

Output
Displays the total time duration for which the webcams were on along with their time stamp along with the total number of frames captured by both webcams. Besides, with the user permission, the functions saves all the captured frames in the C drive of the devicebeing used. Images are saved in by the names xxxxx_y where xxxxx represents the frame number while y is 1 if the frame is captured by the left webcam and 0 for right webcam.

```
```yaml
from DIC_LIPEC import SingleSurfaceCalibration
arr1,arr2,arr3,arr4=SingleSurfaceCalibration(location1,type1,location2,type2,location3,threshold1,threshold2)

Input
location1: Location of the folder where the captured frames are saved
type1: Image format of the captured frames
location2: Location of the folder where the templates to detect the special points are saved
type1: Image format of the templates used to detect the special points
location3: Location of the image template used to detect the normal points
threshold1: parameter to detect normal points
threshold2: parameter to detect special points

Output
arr1: Array with all pixel coordinates for the normal points detected for all frames
arr2: Array with all pixel coordinates for the special points detected for all frames
arr3: Array with the intrinsic and extrinsic parameters for left webcam
arr4: Array with the intrinsic and extrinsic parameters for right webcam

```

```yaml
from DIC_LIPEC import DoubleSurfaceCalibration
arr1,arr2,arr3,arr4,arr5,arr6,arr7,arr8=DoubleSurfaceCalibration(location1,type1,location2,type2,location3,threshold1,threshold2)

Input
location1: Location of the folder where the captured frames are saved
type1: Image format of the captured frames
location2: Location of the folder where the templates to detect the special points are saved
type1: Image format of the templates used to detect the special points
location3: Location of the image template used to detect the normal points
threshold1: parameter to detect normal points
threshold2: parameter to detect special points

Output
arr1: Array with all pixel coordinates for the normal points detected for grid 1 for all frames
arr2: Array with all pixel coordinates for the special points detected for grid 2 for all frames
arr3: Array with all pixel coordinates for the normal points detected for grid 1 for all frames
arr4: Array with all pixel coordinates for the special points detected for grid 2 for all frames
arr5: Array with the intrinsic and extrinsic parameters for left webcam for grid 1
arr6: Array with the intrinsic and extrinsic parameters for left webcam for grid 2
arr7: Array with the intrinsic and extrinsic parameters for right webcam for grid 1
arr8: Array with the intrinsic and extrinsic parameters for right webcam for grid 2

```

# Guide
* 

# Disclaimer

This software is for educational and research purposes only. Use it at your own risks.
