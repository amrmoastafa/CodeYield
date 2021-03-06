import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

# Tuning Parameters
sigma = 0.33 # Canny's formula
approxComparisonValue = 4
houghLineLength = 100
houghLineGap = 10
dilationIterations = 3
erosionIterations = 2
epsilonFactor = 0.03
houghLineThickness = 2
minContourArea = 2000
minDiff_XPoints = 20

def sortContours(contours):

    proccessingContoursX = [[0 for i in range(2)] for j in range(4)]

    for ite in range(len(contours)):
        proccessingContoursX[ite][0]= (contours[ite][0][0])
        proccessingContoursX[ite][1]= (contours[ite][0][1])

    proccessingContoursY = proccessingContoursX
    # Sorting founded contours by x-axis points
    proccessingContoursX.sort(key=lambda x:x[0])

    return proccessingContoursX

def  filterContours(contours):

    proccessingContoursX = [[0 for i in range(2)] for j in range(4)]


    proccessingContoursX = sortContours(contours)

    verticalLineDiff1 = abs(proccessingContoursX[1][0] - proccessingContoursX[0][0])
    verticalLineDiff2 = abs(proccessingContoursX[3][0] - proccessingContoursX[2][0])
    # Checking if the rectangle edges aren't quite vertical or not
    if(verticalLineDiff1 > minDiff_XPoints or verticalLineDiff2 > minDiff_XPoints):
        return False
    else:
        return True

def labelBarDetection(path):

    # Image Preparation & Kernel defintion of 5*5 Matrix
    img = cv.imread(path)
    grayImg = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    kernel = np.ones((3, 3), np.uint8)

    # Automatic canny edge detection using sigma value = 0.33
    v = np.median(grayImg)
    lower = int(max(0, (1.0 - sigma) * v))
    upper = int(min(255, (1.0 + sigma) * v))
    edges = cv.Canny(grayImg, lower, upper)

    # Dilating output of canny to achieve a huge edges
    dil = cv.dilate(edges, kernel, iterations=dilationIterations)

    # Using probabilistic hough line transform to get clear & semi complete lines
    processingImg = dil.copy()
    lines = cv.HoughLinesP(processingImg, 1, np.pi / 180, 100, minLineLength=houghLineLength, maxLineGap=houghLineGap)

    for line in lines:
        x1, y1, x2, y2 = line[0]
        cv.line(processingImg, (x1, y1), (x2, y2), (255, 255, 255), houghLineThickness)

    # Eroding to remove noise edges
    erode = cv.erode(processingImg, kernel, iterations=erosionIterations)

    # Finding contours
    contours, hierarchy = cv.findContours(processingImg, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

    detectedLabelBars = []
    hierarchyCounter = 0
    
    # Drawing contours
    for cont in contours:
        epsilon = epsilonFactor * cv.arcLength(cont, True)
        approx = cv.approxPolyDP(cont, epsilon, True)

        x, y, w, h = cv.boundingRect(cont)
        # Checking if it is a rectangle
        if len(approx) == approxComparisonValue  and cv.contourArea(cont) > minContourArea and filterContours(approx) == True:
            if(hierarchy.ravel()[hierarchyCounter*4 + 2] == -1 ):
                cv.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
                detectedLabelBars.append(approx)
                
        hierarchyCounter += 1
    cv.imshow('label', img)
    return detectedLabelBars

