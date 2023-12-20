# aep_for_3b1bKR

기존 푸티지의 모든 라틴어 텍스트를 검정색으로 칠하고, 그 텍스트 위에 새 텍스트 레이어를 추가합니다.
- input:    orig.mp4
- output:   None



### WORKFLOW
- import:     OpenCV, 딥러닝, OCR 인식

* 함수1 - **이미지 전처리**
* 함수2 - **텍스트 경계 그룹(Contours) 판별 및 반환**
* 함수3 - **OCR을 통해 contours에 text 내용도 포함**
* 함수4 - **에프터 이펙트를 직접 조작**g

---

* 실행
* While 원본 영상의 프레임:
  * 이미지 전처리
  * Contours 찾기 ==> Array_contours
  * Array_contours에서 텍스트인 녀석 판별
    * 텍스트이면: Array_text_contours에 append
  * OCR로 Array_text_contours의 내용 인식
    * 수식이면: pop
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
* 종료