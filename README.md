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
git clone https://github.com/ilyasst/pydictoolkit.git
cd pydictoolkit
python3 -m venv .env
source .env/bin/activate
pip install -r requirements.txt
python main.py -h
```

Basic usage:
```
python main.py -d "./deck.yaml"
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
CaptureFrames(stamp)

Input
stamp: This parameter defines the delay between two webcams

Output
Displays the total time duration for which the webcams were on along with their time stamp along with the total number of frames captured by both webcams. Besides, with the user permission, the functions saves all the captured frames in the C drive of the devicebeing used. Images are saved in by the names xxxxx_y where xxxxx represents the frame number while y is 1 if the frame is captured by the left webcam and 0 for right webcam.

```
```yaml
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


# Disclaimer

This software is for educational and research purposes only. Use it at your own risks.

















# <p align="center">Digital Image Correlation (DIC) Adapted for Damage Mechanics and Cracks</p>

<p align="center">
Stereo system is a dual webcam system where both the cameras are considered as a single measurement system. This system is constructed to determine the relative orientation and position of an arbitrarily selected camera with respect to the other camera.
</p>

<p align="center">
We need two webcams of 1080 p each. Connect them to a laptop where the working code "Dual WebCam Setup using OpenCV" will be executed. Make sure the webcams are attached to a fixed support (in our case we have used two tripods). Both the webcams are focused on a single ponit on the calibration pattern. This ensures a common world coordinate system is used to define the extrinsic parameters. Normal to the centre of the calibration pattern must lie midway between the two webcams. For the calibration pattern, a specific point on the calibration pattern is selected as the origin of the world coordinate system (WCS). Consequently, a specific line of points on the pattern is set as the X axis and a perpendicular line of points in the pattern is set as the Y axis. Now one of the webcams is arbitrarily selected as the master camera (MC), in our case it is WebCam 1. The orientation and position of the WCS with respect to the MC is determined. The orientation and position of the other webcam is defined relative to the MC. It is to be ensured that views from both the WebCams must be identical.
</p>

![Focus of WebCams](https://github.com/stochasticmaterialism/Digital-Image-Correlation-DIC-/blob/main/Images/Focus%20of%20WebCams.png?raw=true)  

<p align="center">
The orientation, pinhole position, focus etc. of the MC and the other webcam with respect to each other must remain invariant throughout the calibration and measurement procedure. These parameters combined are known as intrinsic parameters. Both the webcams must be inclined at a minimum angle of 10 degrees and maximum angle of 30 degrees with respect to the optical axis. The calibration pattern is rotated at different angles and the frames are captured by both the webcams. The parameters of rotation and translation constitute the extrinsic parameters.
</p>

![Extrinsic Parameters](https://github.com/stochasticmaterialism/Digital-Image-Correlation-DIC-/blob/main/Images/Extrinsic%20Parameters.png?raw=true)

<p align="center">
We now detect the special points in the calibration pattern using the code "Detecting Special Points" following a template matching technique for all the captured frames. With this done, we are able to mark x and y axes for all the frames irrespectie of their rotations. Now, our aim is to determine the intrinsic and extrinsic parameters for both WebCams and derive the relations between them as elaborated in "Numerical Aspects of Calibration".
</p>
