import cv2
import mediapipe as mp
import time

class faceMeshDetector():

    def __init__(self,staticMode = False, maxFaces=2, minDetectionCon=0.5, minTrackCon=0.5):

        self.staticMode = staticMode
        self.maxFaces = maxFaces
        self.minDetectionCon = minDetectionCon
        self.minTrackCon = minTrackCon

        # static_image_mode = False,
        # max_num_faces = 1,
        # min_detection_confidence = 0.5,
        # min_tracking_confidence = 0.5)

        self.mpDraw = mp.solutions.drawing_utils
        self.mpFaceMesh = mp.solutions.face_mesh
        self.faceMesh = self.mpFaceMesh.FaceMesh(self.staticMode, self.maxFaces,
                                                 self.minDetectionCon, self.minTrackCon)
        self.drawSpec = self.mpDraw.DrawingSpec(thickness=1, circle_radiu=2)

    def findFaceMesh(self,img, draw= True):
        self.imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = faceMesh.process(self.imgRGB)
        faces = []
        if self.results.multi_face_landmarks:
            for faceLms in self.results.multi_face_landmarks:
                if draw:
                self.mpDraw.draw_landmarks(img,faceLms,self.mpFaceMesh.FACE_CONNECTIONS,
                                      self.drawSpec, self.drawSpec)
                faces = []
                for lm in enumerate(faceLms.landmark):
                    print(lm)
                    ih, iw, ic = img.shape
                    x,y = int(lm.x*iw), int(lm.y*ih)
                    # cv2.putText(img, str(id), (x,y), cv2.FONT_HERSHEY_PAIN,
                    #             0.7,  (0,255,0), 1)
                    print(id,x,y)
                    face.append([x,y])
                faces.append(face0)
        return img, faces



def main():
    cap = cv2.VideoCapture("Video/1.MP4")
    pTime = 0
    detector = faceMeshDetector(maxFaces=2)
    while True:
        success, img = cap.read()
        img, faces = detector.findFaceMesh(img)
        if len(faces)!=0:
            print(len(faces[0]))
        cTime = time.time()
        fps = 1/(cTime-pTime)
        pTime = cTime
        cv2. putText(img,f'FPS':{int(fps)}(',(20, 70), cv2.FONT_HERSHEY_PLAIN,
                     3, (0,255,0), 3)
    cv2.imshow("Image", img)
    cv2.waitKey(1)
if __name__ == "__main__":
    main()