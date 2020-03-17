import cv2 as cv


def time_measure(func, description="Spend time: %s ms"):
    t1 = cv.getTickCount()
    func()
    t2 = cv.getTickCount()
    time = (t2 - t1) / cv.getTickFrequency()
    print(description % (time * 1000))


def time_measure_1(func, param, description="Spend time: %s ms"):
    t1 = cv.getTickCount()
    func(param)
    t2 = cv.getTickCount()
    time = (t2 - t1) / cv.getTickFrequency()
    print(description % (time * 1000))
