# Digital Image Correlation (DIC) Adapted for Damage Mechanics and Crack

## Stereo System
<p align="center">
It is a dual webcam system where both the cameras are considered as a single measurement system. This system is constructed to determine the relative orientation and position of an arbitrarily selected camera with respect to the remaining camera.
</p>

# Steps for a stero system setup

Step 1: We need two webcams of 1080 p each. Connect them to a laptop where the working code "Dual WebCam Setup using OpenCV" will be executed.

Step 2: Make sure the webcams are attachned to a fixed support (in our case we have used two tripods).

Step 3: Both the webcams are focused on a single target, i.e., calibration pattern. This ensures a common world coordinate system is used to define the extrinsic parameters.

Step 4: Normal to the centre of the calibration pattern must lie midway between the two webcams.

Step 5: For the calibration pattern:

A specific point on the calibration pattern is selected as the origin of the world coordinate system (WCS), OW.
A specific line of points on the pattern is set as the XW axis and a perpendicular line of points in the pattern is set as the YW axis.
Step 6: Now one of the webcams is arbitrarily selected as the master camera (MC), in our case it is camera 1.

Step 7: The orientation and position of the WCS with respect to the MC is determined.

Step 8: The orientation and position of the other webcam is defined relative to the MC.

![Focus of WebCams](https://github.com/stochasticmaterialism/Digital-Image-Correlation-DIC-/blob/main/Images/Focus%20of%20WebCams.png?raw=true)  

Step 9: The orientation, pinhole position, focus etc. of the MC and the other webcam with respect to each other muct remain invariant throughout the calibration and measurement procedure. These parameters combined are known as intrinsic parameters.

Step 10: Both the webcams must be inclined at a minimum angle of 10o and maximum angle of 30o with respect to the optical axis.

Step 11: The calibration pattern is rotated at different angles and the frames are captured by both the webcams. The parameters of rotation and translation (R0-1, R0-2, t0-1 and t0-2) constitute the extrinsic parameters.

![Different Coordinate System](https://drive.google.com/file/d/1WXSpBVu78kYFYN0Q7MLR7LzlvgqZpqUD/view?usp=sharing)
