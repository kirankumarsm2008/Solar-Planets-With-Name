import cv2

img = cv2.imread("solar-system.jpg")


cv2.putText(img,
           'Sun',
            (20,100),
            cv2.FONT_HERSHEY_COMPLEX,
            1,
            (255,255,255)
            )

cv2.putText(img,
           'Mercury',
            (110,280),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
            )

cv2.putText(img,
           'Venus',
            (200,280),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
            )

cv2.putText(img,
           'Earth',
            (300,280),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
            )

cv2.putText(img,
           'Mars',
            (400,280),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
            )

cv2.putText(img,
           'Jupiter',
            (520,380),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
            )

cv2.putText(img,
           'Saturn',
            (700,300),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
            )

cv2.putText(img,
           'Uranus',
            (930,300),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
            )

cv2.putText(img,
           'Neptune',
            (1150,300),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
            )

cv2.putText(img,
           'Moon',
            (320,150),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
            )
cv2.imshow("output",img)
cv2.waitKey(0)

cv2.imwrite("Solar Planets With Name.jpg", img)