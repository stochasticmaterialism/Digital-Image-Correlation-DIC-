# Function to capture frames from both the WebCams simultaneously

def CaptureFrames(stamp):

    import cv2
    import matplotlib.pyplot as plt
    import os
    import time
    import numpy as np

    print("Please wait for the WebCams to start for capturing frames!")
    print(" ")

    # Start the webcams
    cap1=cv2.VideoCapture(0)
    cap2=cv2.VideoCapture(1)

    #Check if the webcams is opened correctly, a message will be displayed corresponding to opening status of both the webcams
    if not cap1.isOpened():
        raise IOError("Cannot open WebCam1")
    else:
        print('Opening WebCam1')
    if not cap2.isOpened():
        raise IOError("Cannot open WebCam2")
    else:
        print('Opening WebCam2')
    
    print(" ")

    i,d1,d2=0,0,0
    image,name,time_stamp,delay=[],[],[],[]
    t=time.perf_counter()
    #print(t)

    print('Capturing Frames')
    print('Press the stop button of the Python scripting window when you are done!')
    print(" ")

    while True: # Run an infinite loop which will terminate upon keyboard interupt
    # Ret returns a boolean value, True indicating a frame has been recorded and vice versa for False
    # Frame records the image/ video from the webcam
        try:
            ret1,frame1=cap1.read()
            time.sleep(stamp)
            ret2,frame2=cap2.read()
            # The frame from the webcam will get displayed on screen
            if ret1:
                a=(int)(i/2+1)
                filename=(str)(a)+'_1' # Naming the frames, xxxxx_1 for right WebCam
                #print(filename)
                cv2.imshow("Frame 1",frame1)
                frame1=frame1[90:410,:] # To remove unnecessary backgroud from the frames
                #plt.imshow(frame1)
                #plt.show()
                i+=1
                image.append(frame1)
                name.append(filename)
                time1=time.perf_counter()
                #print("Time Stamp: {}".format(time1))
                b=round((time1-t),3)
                time_stamp.append(b)
                if i==1:
                    #print("Delay: {}".format(0))
                    delay.append(0)
                    d1=time1
                else:
                    #print("Delay: {}".format(time1-time2))
                    b=round(((time1-d2)*(10**3)),3)
                    delay.append(b)
                    d1=time1
                #print(" ")
            else:
                print('No frame captured')
            if ret2:
                a=(int)(i/2+1)
                filename=(str)(a)+'_0' # Naming the frames, xxxxx_0 for left WebCam
                #print(filename)
                cv2.imshow("Frame 2",frame2)
                frame2=frame2[90:410,:] # To remove unnecessary backgroud from the frames
                #plt.imshow(frame2)
                #plt.show()
                i+=1
                image.append(frame2)
                name.append(filename)
                time2=time.perf_counter()
                #print("Time Stamp: {}".format(time2))
                b=round((time2-t),3)
                time_stamp.append(b)
                #print("Delay: {}".format(time2-time1))
                b=round(((time2-d1)*(10**3)),3)
                delay.append(b)
                #print(" ")
                d2=time2
            else:
                print('No frame captured')
    
        except KeyboardInterrupt:  # Press the stop button of the Python scripting window
            break

    print("Keyboard Interrupt Encountered")
    print(" ")

    cap1.release()
    print("Closing WebCam 1")
    cap2.release()
    print("Closing WebCam 2")
    cv2.destroyAllWindows()
    
    # Capturing of frames is terminated here
    
    print(" ")
    print('Number of Frames Captured = {}'.format(len(image))) # Total number of frames captured across both WebCams
    print(' ')

    # Find the total time duration for which the WebCams were on
    
    if (d1>d2):
        print("Total execution time: {} s".format(d1-t))
    else:
        print("Total execution time: {} s".format(d2-t))
    print(" ")

    #print(len(name))

    '''for i in range(len(image)):
        plt.imshow(image[i])
        plt.show()'''
    
    # Save the captured frames using the format XXXXX_y where y can be either 0 or 1
    
    for i in range(len(name)):
        if len(name[i])==3:
            name[i]='0000'+name[i]+'.jpg'
        if len(name[i])==4:
            name[i]='000'+name[i]+'.jpg'
        if len(name[i])==5:
            name[i]='00'+name[i]+'.jpg'
        if len(name[i])==6:
            name[i]='0'+name[i]+'.jpg'
        else:
            continue
    
    '''for i in range(len(image)):
        print(name[i])'''
    
    print("Frame                   Time Stamp               Delay")
    for i in range(len(image)):
        print("{}             {} s                  {} ms".format(name[i],time_stamp[i],delay[i]))
        print(' ')
    
    ''' Use the following line only if you need to save the captured frames '''
    c=input("Press Y to save the frames: ")
    if c=='Y' or c=='y':
        print("Create a folder named Captured Frames in your C drive")
        print(" ")
        c1=input("Press Y once you have created the folder: ")
        if c1=='Y' or c1=='y':
            for i in range(len(image)):
                path=r"C:\Users\DEBANSHU BANERJEE\Captured Frames 2"  # Change the path according to the computer that you are using 
                cv2.imwrite(os.path.join(path,name[i]),image[i])
            print(r"Frames have been successfully save at C:\Users\**********\Captured Frames")
        else:
            print("Captured Frames folder not found in C drive")
    else:
        print("Code terminated!")
    
    # All images will be saved in C drive
    
    return None
