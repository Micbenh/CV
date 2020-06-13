import cv2

def instructions():
    print(""" 
    Change The color space of the video stream using the following buttons:
    GRAYSCALE - press 'g'
    YUV - press 'y'
    HSV - press 'h'
    """)

if __name__ == '__main__':
    instructions()
    capture = cv2.VideoCapture(0)
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter('output.avi', fourcc, 20 ,(640,480))

    if not capture.isOpened():
        raise IOError("Webcam could not be accessed!")

    cur_mode = None
    while True:
        ret, frame = capture.read()
        c = cv2.waitKey(1)
        if c == ord('q'):
            break
        if c != -1 and c != 255 and c != cur_mode:
            cur_mode = c
        
        if cur_mode == ord('g'):
            output = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        elif cur_mode == ord('y'):
            output = cv2.cvtColor(frame, cv2.COLOR_BGR2YUV)
        elif cur_mode == ord('h'):
            output = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        else:
            output = frame
        out.write(output)
        cv2.imshow('WEBCAM', output)


    capture.release()
    out.release()
    cv2.destroyAllWindows()