from DIC_LIPEC import *

def main():
    CaptureFrames()
    location1=r"Enter Location of Captured Frames"
    location2=r"Enter Location of Templates for Special Points"
    location3="Name of Template for Normal Point.Format"
    type1='*.Image Format of Captured Frames'
    type1='*.Image Format of Templates for Special Points'
    threshold1=#Define Threshold for DEtecting Normal Points
    threshold2=#Define Threshold for DEtecting Special Points
    point,special_points,parameters1,parameters2=SingleSurfaceCalibration(location1,type1,location2,type2,location3,threshold1,threshold2)
    
if __name__ == "__main__":
    main()
