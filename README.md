# aep_for_3b1bKR

기존 푸티지의 모든 라틴어 텍스트를 검정색으로 칠하고, 그 텍스트 위에 새 텍스트 레이어를 추가하는 after effect 스크립트.
- input:    orig.mp4
- output:   None

---

# WORKFLOW
import cv2, (딥러닝, OCR 인식,) subprocess, json

### 여러 함수
* has_next_frame()
* get_next_frame()
* find_text_contours(fr_preprocessed)
  * Contours 추출
* perform_ocr(list_contours)

### 주요함수1: preprocess_image(frame)
이미지 전처리
* 전처리 이미지 반환

### 주요함수2: extract_text_contours(fr_preprocessed)
텍스트 경계 그룹(Contours) 판별
* list_contours = find_text_contours(frame_preprocessed)
* 딥러닝을 활용하여 list_contours에서 텍스트인 녀석 판별
  * 텍스트이면: list_text_contours에 append
* list_text_contours = perform_ocr(list_contours)
* list_text_contours 반환

### 주요함수3: manipulate_after_effects(list_text_contours)
에프터 이펙트를 직접 조작.
* 리스트 별로:
  * 첫 번째 프레임이 아니라면:
    * 이전 프레임에 내용이 같은 텍스트 레이어가 존재한다면:
      * 텍스트 레이어의 위치가 해당 레이어와 많이 겹친다면:
        * 해당 레이어를 1프레임 연장
        * 해당 레이어 조정
          1. text layer:  position 조정
          2. solid layer: position, scale 조정
        * continue
  * contour의 위치에 새로운 레이어 생성
    1. text layer:    Noto serif CJK KR Medium, 54, 76, -30; Scale: 120%, 좌표: Contour의 왼쪽 끝
    2. solid layer:   Contour 영역. Black
    3. 둘다 position, scale keyframe on
* None 반환

### main함수
* While has_next_frame():
  * frame = get_next_frame()
  * fr_preprocessed = preprocess_image(frame)
  * list_text_contours = extract_text_contours(fr_preprocessed)
  * manipulate_after_effects(list_text_contours)
* 종료

이 때 main 파일은 JS로 제작하며, 나머지 부분은 파이썬 파일로 구현하여 subprocess와 json으로 결합시킨다.
