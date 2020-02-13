#!/usr/bin/python2.7
import sys
import getopt
import matplotlib.pyplot as plt
def get_point(A,B):
    return [(A[0]+B[0])/2,(A[1]+B[1])/2]
if __name__ == '__main__':
    opts,args = getopt.getopt(sys.argv[1:],"f:h")
    filename=""
    usage = "drawNRtk -f ambfile -h"
    for op,value in opts:
        if op == '-h':
            print usage
            sys.exit()
        elif op == '-f':
            filename = value
        else:
            print usage
            sys.exit()
    baselines = []
    baselines_distance = []
    station_coods = {}
    try:
        fid_s = open(filename,"r")
    except:
        print "can't open file %s to read!"%filename
        pass
    for line in fid_s:
        if(line[0:6] == "#POINT"):
            data = line.rstrip().split()
            print data[1],data[2],data[3]
            station_coods[data[1]]=[float(data[3]),float(data[2])]
    
        if(line[0] == ' '):
            data = line.rstrip().split()
            baselines.append([data[0],data[1]])
            baselines_distance.append(data[3]) 
            pass
    baselines_points = []
    for i in range(len(baselines)):
        baseline_point = get_point(station_coods[baselines[i][0]],station_coods[baselines[i][1]])
        baselines_points.append(baseline_point)
        pX = [station_coods[baselines[i][0]][0],station_coods[baselines[i][1]][0]]
        pY = [station_coods[baselines[i][0]][1],station_coods[baselines[i][1]][1]]
        plt.scatter(pX,pY,color = 'b')
        plt.plot(pX,pY,color = 'black')
    for i in station_coods:
        plt.annotate(i, 
                     (station_coods[i][0],station_coods[i][1]))
    for i in range(len(baselines)):
        plt.annotate(baselines_distance[i],
                     tuple(baselines_points[i]))
    plt.axis('off')
    plt.show()