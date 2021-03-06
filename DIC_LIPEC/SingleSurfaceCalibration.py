# Function to perform stereo calibration using one surface

def SingleSurfaceCalibration(location1,type1,location2,type2,location3,threshold1,threshold2):
    import numpy as np
    import matplotlib.pyplot as plt
    from skimage.io import imread, imshow
    from skimage.color import rgb2gray
    from skimage.feature import match_template, peak_local_max
    from skimage import transform
    import os
    import glob
    import cv2
    import pandas as pd
    import statistics
    import math
    from scipy.ndimage import spline_filter1d
    
    print("This might take a few minutes")
    print(" ")

    #Load images

    img_dir=location1
    data_path=os.path.join(img_dir,type1)
    files=glob.iglob(data_path)
    data,name=[],[]
    for f in files:
        img=cv2.imread(f)
        img1=cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
        data.append(img1)
        #print(f)
        l1=len(f)-11
        l2=len(f)-4
        a=f[l1:l2]
        #print(a)
        name.append(a)
    
    #print(len(data))
    '''for i in range(len(data)):
        plt.imshow(data[i],cmap='gray')
        plt.show()'''

    #Load the calibration templates for special points

    img_dir=location2
    data_path=os.path.join(img_dir,type2)
    files=glob.iglob(data_path)
    t=[]
    for f in files:
        img=cv2.imread(f)
        img1=cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
        t.append(img1)
    
    #print(len(t))
    '''for i in range(len(t)):
        plt.imshow(t[i],cmap='gray')
        plt.show()'''
    
    #Load template for normal points

    img=cv2.imread(location3)
    img=cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)

    '''plt.imshow(img)
    plt.show()'''
    
    cord1,cord2=[],[]

    #Detecting normal points

    for i in range(len(data)):
        #print("Frame: {}".format(name[i]))
        temp=[]
        #plt.imshow(data[i],cmap='gray')
        result=match_template(data[i],img)
        x,y=np.unravel_index(np.argmax(result),result.shape)
        for x,y in peak_local_max(result,threshold_abs=threshold1):
            rect=plt.Rectangle((y,x),20,20,color='r',fc='none')
            #print(rect)
            a=rect.xy[0]
            a=(a+(a+15))/2
            b=rect.xy[1]
            b=(b+(b+15))/2
            temp.append([a,b])
            #c=plt.Circle((a,b),3,color='r',fc='r')
            #plt.gca().add_patch(c)
        cord1.append(temp)
        #plt.show()
    
    #print(len(cord1))
    #print(cord1)

    #Detecting special points

    for i in range(len(data)):
        #print("Frame: {}".format(name[i]))
        temp=[]
        #plt.imshow(data[i],cmap='gray')
        for j in range(len(t)):
            result=match_template(data[i],t[j])
            x,y=np.unravel_index(np.argmax(result),result.shape)
            for x,y in peak_local_max(result,threshold_abs=threshold2):
                rect=plt.Rectangle((y,x),20,20,color='r',fc='none')
                #print(rect)
                a=rect.xy[0]
                a=(a+(a+15))/2
                b=rect.xy[1]
                b=(b+(b+15))/2
                temp.append([a,b])
                #c=plt.Circle((a,b),3,color='r',fc='r')
                #plt.gca().add_patch(c)
            #plt.show()
        cord2.append(temp)
    
    #print(len(cord1))
    #print(len(cord2))
    
    w=data[0].shape[0]/2
    h=data[0].shape[1]/2

    #print(w)
    #print(h)

    special=[]    
    
    for i in range(len(cord2)):
        x1,x2,x3,y1,y2,y3,c1,c2,c3,temp=0,0,0,0,0,0,0,0,0,[]
        for j in range(len(cord2[i])):
            if cord2[i][j][0]>h and cord2[i][j][1]>w:
                x3+=cord2[i][j][0]
                y3+=cord2[i][j][1]
                c3+=1
            if cord2[i][j][0]>h and cord2[i][j][1]<w:
                x2+=cord2[i][j][0]
                y2+=cord2[i][j][1]
                c2+=1
            if cord2[i][j][0]<h and cord2[i][j][1]<w:
                x1+=cord2[i][j][0]
                y1+=cord2[i][j][1]
                c1+=1
        if c1 is not 0:
            x1=x1/c1
            y1=y1/c1
            temp.append([x1,y1])
        if c2 is not 0:
            x2=x2/c2
            y2=y2/c2
            temp.append([x2,y2])
        if c3 is not 0:
            x3=x3/c3
            y3=y3/c3
            temp.append([x3,y3])
        special.append(temp)
    
    #print(len(special))    
    #print(special)
    
    rejected,location=0,[]

    for i in range(len(cord1)):
        if len(cord1[i])==140 and len(special[i])==3:
            print("Frame: {}".format(name[i]))
            plt.imshow(data[i],cmap='gray')
            for j in range(len(cord1[i])):
                d=plt.Circle((cord1[i][j][0],cord1[i][j][1]),2,color='g',fc='g')
                plt.gca().add_patch(d)
                plt.axis("off")
            for j in range(len(special[i])):
                d=plt.Circle((special[i][j][0],special[i][j][1]),2,color='r',fc='r')
                plt.gca().add_patch(d)
                plt.axis("off")
            plt.show()
            location.append(i)
        else:
            rejected+=1
        
    print("Number of frames rejected due to improper detection of points are {} out of {}".format(rejected,len(cord1)))

    # Finding the reference coordinates

    reference=[]

    y=-3.4
    for i in range(10):
        x=18.7
        for j in range(14):
            reference.append([x,y])
            x=round(x-1.7,1)
        y=round(y+1.7,1)
      
    #count=0        
    '''for i in range(10):
        for j in range(14):
            print("{} ".format(reference[count]),end="")
            count+=1
        print("\n")'''
    
    #special_ref=[reference[30],reference[39],reference[109]]
    #print(special_ref)

    rotated=[]

    for i in range(len(location)):
        a=location[i]
        temp=[]
        slope=(special[a][1][1]-special[a][0][1])/(special[a][1][0]-special[a][0][0])
        theta=math.degrees(math.atan(slope))
        theta=(theta*3.14)/180
        s=math.sin(theta)
        c=math.cos(theta)
        s2=s*s
        c2=c*c
        h=special[a][1][0]
        k=special[a][1][1]
        for j in range(len(cord1[a])):
            cord1[a][j][1]=-cord1[a][j][1]
        for j in range(len(cord1[a])):
            x=cord1[a][j][0]
            y=cord1[a][j][1]
            x1=((x-h)*c+(k-y)*s)/(c2-s2)
            y1=((x-h)*s+(k-y)*c)/(c2-s2)
            temp.append([x1,y1])
        #print(len(temp))
        rotated.append(temp)
    
    mapped=[]
    for i in range(len(rotated)):
        rotated[i]=sorted(rotated[i],key=lambda x:x[1],reverse=False)
        temp1,temp2,temp3,temp4,temp5,temp6,temp7,temp8,temp9,temp10=[],[],[],[],[],[],[],[],[],[]
        temp1=rotated[i][0:14]
        temp1=sorted(temp1,key=lambda x:x[0],reverse=False)
        temp2=rotated[i][14:28]
        temp2=sorted(temp2,key=lambda x:x[0],reverse=False)
        temp3=rotated[i][28:42]
        temp3=sorted(temp3,key=lambda x:x[0],reverse=False)
        temp4=rotated[i][42:56]
        temp4=sorted(temp4,key=lambda x:x[0],reverse=False)
        temp5=rotated[i][56:70]
        temp5=sorted(temp5,key=lambda x:x[0],reverse=False)
        temp6=rotated[i][70:84]
        temp6=sorted(temp6,key=lambda x:x[0],reverse=False)
        temp7=rotated[i][84:98]
        temp7=sorted(temp7,key=lambda x:x[0],reverse=False)
        temp8=rotated[i][98:112]
        temp8=sorted(temp8,key=lambda x:x[0],reverse=False)
        temp9=rotated[i][112:126]
        temp9=sorted(temp9,key=lambda x:x[0],reverse=False)
        temp10=rotated[i][126:140]
        temp10=sorted(temp10,key=lambda x:x[0],reverse=False)
        temp=[]
        temp=temp1+temp2+temp3+temp4+temp5+temp6+temp7+temp8+temp9+temp10
        #print(len(temp))
        mapped.append(temp)
    
    '''for i in range(len(mapped)):
        print(mapped[i])
        print(" ")'''
    
    #print(len(location))

    eta=[]
    for i in range(len(location)):
        p=location[i]
        frame=name[p]
        #print(frame[6])
        if frame[6]=='0':
            temp=[]
            #print(len(mapped[i]))
            for j in range(0,len(mapped[i]),4):
                a=reference[j]
                b=reference[j+1]
                c=reference[j+2]
                d=reference[j+3]
                #print(a)
                #print(b)
                #print(c)
                #print(d)
                e=cord1[p][j]
                f=cord1[p][j+1]
                g=cord1[p][j+2]
                h=cord1[p][j+3]
                #print(e)
                #print(f)
                #print(g)
                #print(h)
                arr1=[1,0,a[0],a[1],0,0,-a[0]*e[0],-a[1]*e[0]]
                arr2=[0,1,0,0,a[0],a[1],-a[0]*e[1],-a[1]*e[1]]
                arr3=[1,0,b[0],b[1],0,0,-b[0]*f[0],-b[1]*f[0]]
                arr4=[0,1,0,0,b[0],b[1],-b[0]*f[1],-b[1]*f[1]]
                arr5=[1,0,c[0],c[1],0,0,-c[0]*g[0],-c[1]*g[0]]
                arr6=[0,1,0,0,c[0],c[1],-c[0]*g[1],-c[1]*g[1]]
                arr7=[1,0,d[0],d[1],0,0,-d[0]*h[0],-d[1]*h[0]]
                arr8=[0,1,0,0,d[0],d[1],-d[0]*h[1],-d[1]*h[1]]
                A=np.array([arr1,arr2,arr3,arr4,arr5,arr6,arr7,arr8])
                B=np.array([e[0],e[1],f[0],f[1],g[0],g[1],h[0],h[1]])
                try:
                    X=np.linalg.solve(A,B)
                    #print(X)
                    temp.append(X)
                except:
                    continue
            eta.append(temp)
    
    #print(len(eta))
    '''for i in range(len(eta)):
        #print(len(eta[i]))
        for j in range(len(eta[i])):
            print(len(eta[i][j]))
            print(eta[i][j])'''

    final_eta=[]
    for i in range(len(eta)):
        temp1,temp2,temp3,temp4,temp5,temp6,temp7,temp8=[],[],[],[],[],[],[],[]
        for j in range(len(eta[i])):
            for k in range(len(eta[i][j])):
                if k==0:
                    temp1.append(eta[i][j][k])
                if k==1:
                    temp2.append(eta[i][j][k])
                if k==2:
                    temp3.append(eta[i][j][k])
                if k==3:
                    temp4.append(eta[i][j][k])
                if k==4:
                    temp5.append(eta[i][j][k])
                if k==5:
                    temp6.append(eta[i][j][k])
                if k==6:
                    temp7.append(eta[i][j][k])
                if k==7:
                    temp8.append(eta[i][j][k])
        #print(temp1)
        #print(temp2)
        #print(temp3)
        #print(temp4)
        #print(temp5)
        #print(temp6)
        #print(temp7)
        #print(temp8)
        temp=[]
        mean,std_dev=0,0
        for j in range(len(temp1)):
            mean=mean+temp1[j]
        mean=mean/8
        std_dev=statistics.stdev(temp1)
        temp.append([mean,std_dev])
        mean,std_dev=0,0
        for j in range(len(temp2)):
            mean=mean+temp2[j]
        mean=mean/8
        std_dev=statistics.stdev(temp2)
        temp.append([mean,std_dev])
        mean,std_dev=0,0
        for j in range(len(temp3)):
            mean=mean+temp3[j]
        mean=mean/8
        std_dev=statistics.stdev(temp3)
        temp.append([mean,std_dev])
        mean,std_dev=0,0
        for j in range(len(temp4)):
            mean=mean+temp4[j]
        mean=mean/8
        std_dev=statistics.stdev(temp4)
        temp.append([mean,std_dev])
        mean,std_dev=0,0
        for j in range(len(temp5)):
            mean=mean+temp5[j]
        mean=mean/8
        std_dev=statistics.stdev(temp5)
        temp.append([mean,std_dev])
        mean,std_dev=0,0
        for j in range(len(temp6)):
            mean=mean+temp6[j]
        mean=mean/8
        std_dev=statistics.stdev(temp6)
        temp.append([mean,std_dev])
        mean,std_dev=0,0
        for j in range(len(temp7)):
            mean=mean+temp7[j]
        mean=mean/8
        std_dev=statistics.stdev(temp7)
        temp.append([mean,std_dev])
        mean,std_dev=0,0
        for j in range(len(temp8)):
            mean=mean+temp8[j]
        mean=mean/8
        std_dev=statistics.stdev(temp8)
        temp.append([mean,std_dev])
        final_eta.append(temp)
    
    #print(len(final_eta))
    '''for i in range(len(final_eta)):
        a=location[i]
        #print(len(final_eta[i]))
        print(name[a])
        print(final_eta[i])'''
    
    count,singular=0,[]

    optical_centre,focal_point,translation,rotation=[],[],[],[]

    for i in range(len(final_eta)):
        a=final_eta[i][0]
        b=final_eta[i][1]
        c=final_eta[i][2]
        d=final_eta[i][3]
        e=final_eta[i][4]
        f=final_eta[i][5]
        g=final_eta[i][6]
        h=final_eta[i][7]
        A=np.array([[c[0]*h[0]+d[0]*g[0],e[0]*f[0],e[0]*h[0]+f[0]*g[0],g[0]*h[0]],[2*(c[0]*g[0]-d[0]*h[0]),e[0]*e[0]-f[0]*f[0],2*(e[0]*g[0]-f[0]*h[0]),g[0]*g[0]-h[0]*h[0]],[0,0,0,0],[0,0,0,0]])
        #print(A.shape)
        B=np.array([-c[0]*d[0],d[0]*d[0]-c[0]*c[0],0,0])
        #print(B.shape)
        regular=np.array([[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]])
        #print(regular.shape)
        A_new=np.add(A,regular)
        #print(A_new.shape)
        try:
            A_inv=np.linalg.inv(A_new) 
            #print(A_inv.shape)
            res=np.multiply(A_inv,B)
            #print(res.shape)
            #print(res)
            e1=res[0][0]
            e2=res[0][1]
            e3=res[1][0]
            e4=res[1][1]
            #print("{} {} {} {}".format(e1,e2,e3,e4))
            cx=-e1
            cy=-e3/e2
            fx=(e4-(cx*cx)-(cy*cy*e2))*0.5
            fy=fx/(e2**0.5)
            optical_centre.append([cx,cy])
            focal_point.append([fx,fy])
            tz=((1/((((c[0]-g[0]*cx)**2+(d[0]-h[0]*cx)**2)/(fx**2))+(((e[0]-g[0]*cy)**2+(f[0]-h[0]*cy)**2)/(fy**2))+(g[0]**2)+(h[0]**2)))**0.5)/0.5
            tx=(a[0]-cx)*(tz/fx)
            ty=(b[0]-cy)*(tz/fy)
            translation.append([tx,ty,tz])
            R11=(tz*(c[0]-g[0]*cx))/fx
            R12=(tz*(d[0]-h[0]*cx))/fx
            R21=(tz*(e[0]-g[0]*cy))/fy
            R22=(tz*(f[0]-g[0]*cy))/fy
            R31=tz*g[0]
            R32=tz*h[0]
            R=np.array([[R11,R12,0],[R21,R22,0],[R31,R32,0]])
            #print(R.shape)
            rotation.append(R)
        except:
            count+=1
            singular.append(i)

    print("{} frames resulted in singular matrix during parameter estimation of WebCam1".format(count))
    #print(singular)

    #print(len(optical_centre))
    #print(len(focal_point))
    #print(len(translation))
    #print(len(rotation))

    correct=0
    correct_location=[]

    for i in range(len(optical_centre)):
        c=0
        if np.isnan(optical_centre[i][0]) or np.isnan(optical_centre[i][1]):
            c=1
        if c is not 1:
            if np.isnan(focal_point[i][0]) or np.isnan(focal_point[i][1]):
                c=1
            if c is not 1:
                if np.isnan(translation[i][0]) or np.isnan(translation[i][1]) or np.isnan(translation[i][1]):
                    c=1
                if c is not 1:
                    for j in range(3):
                        for k in range(3):
                            if np.isnan(rotation[i][j][k]):
                                c=1
                                break
                            else:
                                continue
                    if c is not 1:
                        '''a=location[i]
                        print("Frame {}".format(name[a]))
                        print(" ")
                        print("Optical Centre")
                        print(optical_centre[i])
                        print(" ")
                        print("Focal Points")
                        print(focal_point[i])
                        print(" ")
                        print("Translation Matrix")
                        print(translation[i])
                        print(" ")
                        print("Rotation Matrix")
                        print(rotation[i])
                        print(" ")
                        print(" ")'''
                        correct+=1
                        correct_location.append(i)
             
    print("{} number of frames having no negative roots in the calibration calculation of WebCam1".format(correct))

    webcam1=[]

    l=len(correct_location)

    x,y=0,0
    for i in range(l):
        a=correct_location[i]
        x+=optical_centre[a][0]
        y+=optical_centre[a][1]
    x=x/(l*10)
    y=y/(l*(10**9))
    webcam1.append([x,y])

    x,y=0,0
    for i in range(l):
        a=correct_location[i]
        x+=focal_point[a][0]
        y+=focal_point[a][1]
    x=x/(l*(10**8))
    y=y/(l*(10**14))
    webcam1.append([x,y])

    x,y,z=0,0,0
    for i in range(l):
        a=correct_location[i]
        x+=translation[a][0]
        y+=translation[a][1]
        z+=translation[a][2]
    x=x/l
    y=y/l
    z=z/l
    webcam1.append([x,y,z])

    u,v,w,x,y,z=0,0,0,0,0,0
    for i in range(l):
        a=correct_location[i]
        u+=rotation[a][0][0]
        v+=rotation[a][0][1]
        w+=rotation[a][1][0]
        x+=rotation[a][1][1]
        y+=rotation[a][2][0]
        z+=rotation[a][2][1]
    u=u/l
    v=v/l
    w=w/l
    x=x/l
    y=y/l
    z=z/l
    webcam1.append([u,v,w,x,y,z])

    #print(len(location))

    eta=[]
    for i in range(len(location)-1):
        p=location[i]
        frame1=name[p]
        frame1=frame1[0:5]
        p=location[i+1]
        frame2=name[p]
        frame2=frame2[0:5]
        #print(frame[6])
        if frame1==frame2:
            reference=mapped[i+1]
            temp=[]
            #print(len(mapped[i]))
            for j in range(0,len(mapped[i]),4):
                a=reference[j]
                b=reference[j+1]
                c=reference[j+2]
                d=reference[j+3]
                #print(a)
                #print(b)
                #print(c)
                #print(d)
                e=cord1[p][j]
                f=cord1[p][j+1]
                g=cord1[p][j+2]
                h=cord1[p][j+3]
                #print(e)
                #print(f)
                #print(g)
                #print(h)
                arr1=[1,0,a[0],a[1],0,0,-a[0]*e[0],-a[1]*e[0]]
                arr2=[0,1,0,0,a[0],a[1],-a[0]*e[1],-a[1]*e[1]]
                arr3=[1,0,b[0],b[1],0,0,-b[0]*f[0],-b[1]*f[0]]
                arr4=[0,1,0,0,b[0],b[1],-b[0]*f[1],-b[1]*f[1]]
                arr5=[1,0,c[0],c[1],0,0,-c[0]*g[0],-c[1]*g[0]]
                arr6=[0,1,0,0,c[0],c[1],-c[0]*g[1],-c[1]*g[1]]
                arr7=[1,0,d[0],d[1],0,0,-d[0]*h[0],-d[1]*h[0]]
                arr8=[0,1,0,0,d[0],d[1],-d[0]*h[1],-d[1]*h[1]]
                A=np.array([arr1,arr2,arr3,arr4,arr5,arr6,arr7,arr8])
                B=np.array([e[0],e[1],f[0],f[1],g[0],g[1],h[0],h[1]])
                try:
                    X=np.linalg.solve(A,B)
                    #print(X)
                    temp.append(X)
                except:
                    continue
            eta.append(temp)
        else:
            continue
    
    #print(len(eta))
    '''for i in range(len(eta)):
        #print(len(eta[i]))
        for j in range(len(eta[i])):
            print(len(eta[i][j]))
            print(eta[i][j])'''

    final_eta=[]
    for i in range(len(eta)):
        temp1,temp2,temp3,temp4,temp5,temp6,temp7,temp8=[],[],[],[],[],[],[],[]
        for j in range(len(eta[i])):
            for k in range(len(eta[i][j])):
                if k==0:
                    temp1.append(eta[i][j][k])
                if k==1:
                    temp2.append(eta[i][j][k])
                if k==2:
                    temp3.append(eta[i][j][k])
                if k==3:
                    temp4.append(eta[i][j][k])
                if k==4:
                    temp5.append(eta[i][j][k])
                if k==5:
                    temp6.append(eta[i][j][k])
                if k==6:
                    temp7.append(eta[i][j][k])
                if k==7:
                    temp8.append(eta[i][j][k])
        #print(temp1)
        #print(temp2)
        #print(temp3)
        #print(temp4)
        #print(temp5)
        #print(temp6)
        #print(temp7)
        #print(temp8)
        temp=[]
        mean,std_dev=0,0
        for j in range(len(temp1)):
            mean=mean+temp1[j]
        mean=mean/8
        std_dev=statistics.stdev(temp1)
        temp.append([mean,std_dev])
        mean,std_dev=0,0
        for j in range(len(temp2)):
            mean=mean+temp2[j]
        mean=mean/8
        std_dev=statistics.stdev(temp2)
        temp.append([mean,std_dev])
        mean,std_dev=0,0
        for j in range(len(temp3)):
            mean=mean+temp3[j]
        mean=mean/8
        std_dev=statistics.stdev(temp3)
        temp.append([mean,std_dev])
        mean,std_dev=0,0
        for j in range(len(temp4)):
            mean=mean+temp4[j]
        mean=mean/8
        std_dev=statistics.stdev(temp4)
        temp.append([mean,std_dev])
        mean,std_dev=0,0
        for j in range(len(temp5)):
            mean=mean+temp5[j]
        mean=mean/8
        std_dev=statistics.stdev(temp5)
        temp.append([mean,std_dev])
        mean,std_dev=0,0
        for j in range(len(temp6)):
            mean=mean+temp6[j]
        mean=mean/8
        std_dev=statistics.stdev(temp6)
        temp.append([mean,std_dev])
        mean,std_dev=0,0
        for j in range(len(temp7)):
            mean=mean+temp7[j]
        mean=mean/8
        std_dev=statistics.stdev(temp7)
        temp.append([mean,std_dev])
        mean,std_dev=0,0
        for j in range(len(temp8)):
            mean=mean+temp8[j]
        mean=mean/8
        std_dev=statistics.stdev(temp8)
        temp.append([mean,std_dev])
        final_eta.append(temp)
    
    #print(len(final_eta))
    '''for i in range(len(final_eta)):
        a=location[i]
        #print(len(final_eta[i]))
        print(name[a])
        print(final_eta[i])'''
    
    count,singular=0,[]

    optical_centre,focal_point,translation,rotation=[],[],[],[]

    for i in range(len(final_eta)):
        a=final_eta[i][0]
        b=final_eta[i][1]
        c=final_eta[i][2]
        d=final_eta[i][3]
        e=final_eta[i][4]
        f=final_eta[i][5]
        g=final_eta[i][6]
        h=final_eta[i][7]
        A=np.array([[c[0]*h[0]+d[0]*g[0],e[0]*f[0],e[0]*h[0]+f[0]*g[0],g[0]*h[0]],[2*(c[0]*g[0]-d[0]*h[0]),e[0]*e[0]-f[0]*f[0],2*(e[0]*g[0]-f[0]*h[0]),g[0]*g[0]-h[0]*h[0]],[0,0,0,0],[0,0,0,0]])
        #print(A.shape)
        B=np.array([-c[0]*d[0],d[0]*d[0]-c[0]*c[0],0,0])
        #print(B.shape)
        regular=np.array([[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]])
        #print(regular.shape)
        A_new=np.add(A,regular)
        #print(A_new.shape)
        try:
            A_inv=np.linalg.inv(A_new) 
            #print(A_inv.shape)
            res=np.multiply(A_inv,B)
            #print(res.shape)
            #print(res)
            e1=res[0][0]
            e2=res[0][1]
            e3=res[1][0]
            e4=res[1][1]
            #print("{} {} {} {}".format(e1,e2,e3,e4))
            cx=-e1
            cy=-e3/e2
            fx=(e4-(cx*cx)-(cy*cy*e2))*0.5
            fy=fx/(e2**0.5)
            optical_centre.append([cx,cy])
            focal_point.append([fx,fy])
            tz=((1/((((c[0]-g[0]*cx)**2+(d[0]-h[0]*cx)**2)/(fx**2))+(((e[0]-g[0]*cy)**2+(f[0]-h[0]*cy)**2)/(fy**2))+(g[0]**2)+(h[0]**2)))**0.5)/0.5
            tx=(a[0]-cx)*(tz/fx)
            ty=(b[0]-cy)*(tz/fy)
            translation.append([tx,ty,tz])
            R11=(tz*(c[0]-g[0]*cx))/fx
            R12=(tz*(d[0]-h[0]*cx))/fx
            R21=(tz*(e[0]-g[0]*cy))/fy
            R22=(tz*(f[0]-g[0]*cy))/fy
            R31=tz*g[0]
            R32=tz*h[0]
            R=np.array([[R11,R12,0],[R21,R22,0],[R31,R32,0]])
            #print(R.shape)
            rotation.append(R)
        except:
            count+=1
            singular.append(i)

    print("{} frames resulted in singular matrix during parameter estimation of WebCam2".format(count))
    #print(singular)

    #print(len(optical_centre))
    #print(len(focal_point))
    #print(len(translation))
    #print(len(rotation))

    correct=0
    correct_location=[]

    for i in range(len(optical_centre)):
        c=0
        if np.isnan(optical_centre[i][0]) or np.isnan(optical_centre[i][1]):
            c=1
        if c is not 1:
            if np.isnan(focal_point[i][0]) or np.isnan(focal_point[i][1]):
                c=1
            if c is not 1:
                if np.isnan(translation[i][0]) or np.isnan(translation[i][1]) or np.isnan(translation[i][1]):
                    c=1
                if c is not 1:
                    for j in range(3):
                        for k in range(3):
                            if np.isnan(rotation[i][j][k]):
                                c=1
                                break
                            else:
                                continue
                    if c is not 1:
                        '''a=location[i]
                        print("Frame {}".format(name[a]))
                        print(" ")
                        print("Optical Centre")
                        print(optical_centre[i])
                        print(" ")
                        print("Focal Points")
                        print(focal_point[i])
                        print(" ")
                        print("Translation Matrix")
                        print(translation[i])
                        print(" ")
                        print("Rotation Matrix")
                        print(rotation[i])
                        print(" ")
                        print(" ")'''
                        correct+=1
                        correct_location.append(i)
             
    print("{} number of frames having no negative roots in the calibration calculation of WebCam2".format(correct))

    webcam2=[]

    l=len(correct_location)

    x,y=0,0
    for i in range(l):
        a=correct_location[i]
        x+=optical_centre[a][0]
        y+=optical_centre[a][1]
    x=x/(l*(10**11))
    y=y/(l*(10**7))
    webcam2.append([x,y])

    x,y=0,0
    for i in range(l):
        a=correct_location[i]
        x+=focal_point[a][0]
        y+=focal_point[a][1]
    x=x/(l*(10**33))
    y=y/(l*(10**25))
    webcam2.append([x,y])

    x,y,z=0,0,0
    for i in range(l):
        a=correct_location[i]
        x+=translation[a][0]
        y+=translation[a][1]
        z+=translation[a][2]
    x=x/l
    y=y/l
    z=z/l
    webcam2.append([x,y,z])

    u,v,w,x,y,z=0,0,0,0,0,0
    for i in range(l):
        a=correct_location[i]
        u+=rotation[a][0][0]
        v+=rotation[a][0][1]
        w+=rotation[a][1][0]
        x+=rotation[a][1][1]
        y+=rotation[a][2][0]
        z+=rotation[a][2][1]
    u=u/l
    v=v/l
    w=w/l
    x=x/l
    y=y/l
    z=z/l
    webcam2.append([u,v,w,x,y,z])

    print("Parameters for WebCam1")
    print(" ")
    print("Optical Centre")
    print(webcam1[0])
    print(" ")
    print("Focal Points")
    print(webcam1[1])
    print(" ")
    print("Translation Parameters")
    print(webcam1[2])
    print(" ")
    print("Rotation Parameters")
    print(webcam1[3])

    print("Parameters for WebCam2")
    print(" ")
    print("Optical Centre")
    print(webcam2[0])
    print(" ")
    print("Focal Points")
    print(webcam2[1])
    print(" ")
    print("Translation Parameters")
    print(webcam2[2])
    print(" ")
    print("Rotation Parameters")
    print(webcam2[3])
    
    return cord1,special,webcam1,webcam2
