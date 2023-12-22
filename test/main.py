import subprocess
import json
import cv2
import numpy as np

# After Effects 실행 파일 경로
after_effects_path = "C:\\Program Files\\Adobe\\Adobe After Effects CC 2022\\Support Files\\AfterFX.exe"

# After Effects 스크립트 파일 경로
script_path = "script.jsx"

# After Effects를 백그라운드에서 실행
subprocess.Popen([after_effects_path, "-r", script_path], shell=True)

def preprocess_image(frame):
    rgb = frame
    gray_image = cv2.cvtColor(rgb, cv2.COLOR_RGB2GRAY)

    grad_thresh = cv2.adaptiveThreshold(gray_image, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 3, 12)
    contours, hierarchy = cv2.findContours(grad_thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    if len(contours) > 0:
        for idx, contour in enumerate(contours):
            rect = cv2.boundingRect(contour)
            if rect[3] > 10 and rect[2] > 40 and not (rect[2] >= 512 - 5 and rect[3] >= 512 - 5):
                cv2.rectangle(rgb, (rect[0], rect[1]), (rect[0] + rect[2], rect[1] + rect[3]), (0, 255, 0), 5)

        cv2.imwrite("/tmp/dev/doc_original.jpg", rgb)
        cv2.imwrite("/tmp/dev/doc_gray.jpg", gray_image)
        cv2.imwrite("/tmp/dev/doc_thresh.jpg", grad_thresh)
        cv2.imwrite("/tmp/dev/doc_contour.jpg", image_mat)

contours_x = []
contours_y = []
strings_included = []



def main():
    video_path = "orig.mp4"
    cap = cv2.VideoCapture(video_path)
    frame_index_to_load = 100 # 원하는 프레임 인덱스 (json에서 가져오기)
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    # 설정한 인덱스로 이동
    cap.set(cv2.CAP_PROP_POS_FRAMES, frame_index_to_load)

    ret, frame = cap.read()
    if ret:
        cv2.imshow("Frame", frame)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

# ~~~~
# contours.append([])

data = { 
    "contours_x_coordinates" : contours_x, 
    "contours_y_coordinates" : contours_y, 
    "strings_included" : strings_included
}

if __name__ == "__main__":
	main()