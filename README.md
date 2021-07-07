# <p align="center">Digital Image Correlation (DIC) Adapted for Damage Mechanics and Cracks</p>

## <p align="center">This work in a nutshell</p>
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
We now detect the special points in the calibration pattern using the code "Detecting Special Points" following a template matching technique for all the captured frames. With this done, we are able to mark x and y axes for all the frames irrespectie of their rotations. Now, our aim is to determine the intrinsic and extrinsic parameters for both WebCams and derive the relations between them as elaborated in "Calibration Formulae".
</p>
