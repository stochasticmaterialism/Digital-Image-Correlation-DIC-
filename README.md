# Digital Image Correlation (DIC) Adapted for Damage Mechanics and Crack

## Stereo System
<p align="center">
It is a dual webcam system where both the cameras are considered as a single measurement system. This system is constructed to determine the relative orientation and position of an arbitrarily selected camera with respect to the remaining camera.
</p>

## Experimental Setup for Stereo System Calibration
Step 1: We need two webcams of 1080 p each. Connect them to a laptop where the working code "Dual WebCam Setup using OpenCV" will be executed. \
                          \
Step 2: Make sure the webcams are attachned to a fixed support (in our case we have used two tripods).\
                        \
Step 3: Both the webcams are focused on a single target, i.e., calibration pattern. This ensures a common world coordinate system is used to define the extrinsic parameters. \
                     \
Step 4: Normal to the centre of the calibration pattern must lie midway between the two webcams.\
                      \
Step 5: For the calibration pattern: 
* A specific point on the calibration pattern is selected as the origin of the world coordinate system (WCS), O<sub>W</sub>. 
* A specific line of points on the pattern is set as the X<sub>W</sub> axis and a perpendicular line of points in the pattern is set as the Y<sub>W</sub> axis.
<p align='left'>
Step 6: Now one of the webcams is arbitrarily selected as the master camera (MC), in our case it is camera 1. 
<p>
<p align='left'>
Step 7: The orientation and position of the WCS with respect to the MC is determined. 
<p>
<p align='left'>
Step 8: The orientation and position of the other webcam is defined relative to the MC. 
<p>
<p align='left'>
Step 9: The orientation, pinhole position, focus etc. of the MC and the other webcam with respect to each other muct remain invariant throughout the calibration and measurement procedure. These parameters combined are known as intrinsic parameters. 
<p>
<p align='left'>
Step 10: Both the webcams must be inclined at a minimum angle of 10<sup>o</sup> and maximum angle of 30<sup>o</sup> with respect to the optical axis. 
<p>
<p align='left'>
Step 11: The calibration pattern is rotated at different angles and the frames are captured by both the webcams. The parameters of rotation and translation (R<sub>0-1</sub>, R<sub>0-2</sub>, t<sub>0-1</sub> and t<sub>0-2</sub>) constitute the extrinsic parameters.
<p>

  
<p align='center'>
![stereo 6](https://user-images.githubusercontent.com/79299979/122669335-7622cd00-d1da-11eb-8a43-618779e5b908.png)
<p>

<p align='center'>
![stereo 7](https://user-images.githubusercontent.com/79299979/122669350-86d34300-d1da-11eb-9846-492614a300a4.png)
<p>
