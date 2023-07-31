import cv2
import mediapipe as mp
import pyautogui
x1 = y1 = x2 = y2 =0
cam = cv2.VideoCapture(0)
palm = mp.solutions.hands.Hands()
drawing_utils = mp.solutions.drawing_utils

while True:
    _ , picture = cam.read()
    picture = cv2.flip(picture,1)
    frame_hg, frame_wd, _ = picture.shape
    image = cv2.cvtColor(picture,cv2.COLOR_BGR2RGB)
    op = palm.process(image)
    hands = op.multi_hand_landmarks
    if hands:
        for hand in hands:
            drawing_utils.draw_landmarks(picture,hand)
            lm = hand.landmark
            for id, landmark in enumerate(lm):
                x = int(landmark.x * frame_wd)
                y = int(landmark.y * frame_hg)
                if id == 8:
                    cv2.circle(img=picture,center=(x,y),radius=8,color=(0,0,139),thickness=2)
                    x1 = x
                    y1 = y
                if id == 4:
                    cv2.circle(img=picture, center=(x, y),radius=8,color=(127,0,255),thickness=2)
                    x2 = x
                    y2 = y
        dist = ((x2-x1)**2 + (y2-y1)**2)**(0.5)//4
        cv2.line(picture,(x1,y1),(x2,y2),(255,255,255),3)
        if dist > 20:
            pyautogui.press("volumeup")
        else:
             pyautogui.press("volumedown")



    cv2.imshow("wireless sound control", picture)
    pin = cv2.waitKey(10)
    if pin == 27:
        break
cam.release()
cv2.destroyAllWindows()