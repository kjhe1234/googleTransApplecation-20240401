import sys
import googletrans
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic
import re

form_class = uic.loadUiType("ui/googleTrans.ui")[0]
# 디자인한 외부 ui파일 불러와서 저장


class GoogleTrans(QMainWindow, form_class):
    def __init__(self):
        super().__init__()  # 부모 클래스 생성자 호출
        self.setupUi(self)  # 불러온 ui파일을 연결
        self.setWindowTitle("구글 한줄 번역기")
        self.setWindowIcon(QIcon("icon/google.png"))
        self.statusBar().showMessage("Google Trans App v1.0 Made By kjhe1234")
        self.trans_btn.clicked.connect(self.trans_action) # signal
        self.init_btn1.clicked.connect(self.init1_action)
        self.init_btn2.clicked.connect(self.init2_action)


    def trans_action(self):  # 번역 실행 함수 -> solt 함수
        korText = self.kor_input.text()  # kor_input에 입력된 한글 텍스트 가져오기
        reg = re.compile(r'[^가-힣]') # 한글만 찾는 정규표현식


        if korText == "":
            print("공백입력!!")
            QMessageBox.warning(self, "입력오류!", "입력란에 번역할 문장을 넣어 주세요.")

        elif reg.match(korText):  # 한글인지 아닌지 여부 확인.(시작 단어가 숫자 또는 영어로 입력시 경고창 출력)
            # match 대신 search 하면 한글이 아닌거 사용시 에러 발생
            print("한글입력 오류")
            QMessageBox.warning(self, "입력오류!", "한글입력란에는 한글만 넣어주세요.")

        else:
            trans = googletrans.Translator()  # 구글트랜스 모듈의 객체 선언
            # print(googletrans.LANGUAGES) -> 번역 언어의 dset 영어 보기
            engText = trans.translate(korText, dest="en")  # 영어 번역결과
            japText = trans.translate(korText, dest="ja")  # 일어 번역 결과
            chText = trans.translate(korText, dest="zh-cn")  # 중국어 번역 결과
            self.eng_input.append(engText.text)
            # 번역된 영어 텍스트를 eng_input에 출력
            self.jap_input.append(japText.text)
            self.ch_input.append(chText.text)





    def init1_action(self):   # 입력 초기화 변수
        self.kor_input.clear()  #입력 내용 지우기
    def init2_action(self):   # 전체 초기화 변수
        self.kor_input.clear()  #입력 내용 지우기
        self.eng_input.clear()
        self.jap_input.clear()
        self.ch_input.clear()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    googleWin = GoogleTrans()
    googleWin.show()
    sys.exit(app.exec_())


# 윈도우에서 exe로 실행하게 하는법
# pyinstaller 패키지 설치
# 터미널에서 pyinstaller --onefile googleTransApplz.py  텍스트만 할시
# 터미널에서 pyinstaller --windowed googleTransApplz.py
# googleTransApplz.py 이거 대신 해당 파일 이름 작성

# 만든 후에 해당 파이썬프로젝트 폴더안에 dist 폴더 생성 그안에 Qt디자이너
# 하고 아이콘 이미지 있을시 해당 폴더 복사해서 넣어줘야 함
