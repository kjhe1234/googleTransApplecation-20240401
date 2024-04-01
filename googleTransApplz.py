import sys
import googletrans
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic

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

        trans = googletrans.Translator() # 구글트랜스 모듈의 객체 선언
        # print(googletrans.LANGUAGES) -> 번역 언어의 dset 영어 보기

        engText = trans.translate(korText, dest="en") # 영어 번역결과
        japText = trans.translate(korText, dest="ja") # 일어 번역 결과
        chText = trans.translate(korText, dest="zh-cn") # 중국어 번역 결과

        self.eng_input.append(engText.text)
        #번역된 영어 텍스트를 eng_input에 출력
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




