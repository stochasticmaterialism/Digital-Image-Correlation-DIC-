from DIC_LIPEC import *

def main():
    location1=r"C:\Users\DEBANSHU BANERJEE\Captured Framez"
    location2=r"C:\Users\DEBANSHU BANERJEE\Calibration Templates"
    location3="Calibration Template.jpg"
    point,special_points,parameters1,parameters2=calibration_1(location1,location2,location3,0.6,0.5)
    
if __name__ == "__main__":
    main()
