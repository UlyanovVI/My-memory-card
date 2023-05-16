from PyQt5.QtCore import Qt 
from PyQt5.QtWidgets import QApplication, QButtonGroup, QWidget, QHBoxLayout, QVBoxLayout, QGroupBox, QRadioButton, QPushButton, QLabel 
from random import shuffle, randint

class Question():
    def __init__(self,question,right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

q_list = []
q_list.append(Question('Когда умер Шоичиро Тойода?', '14 февраля 2023', '8 сентября 1945', '1991', '6 октября 2020'))
q_list.append(Question('Сколько лошадиных сил у Porsche 911 GT3 RS (992)?', '525 л.с.', '620 л.с.', '110 л.с.', '582 л.с.'))
q_list.append(Question('У какого гонщика F1 больше всего подиуомов?', 'Льюис Хемильтон', 'Юки Цунода', 'Чарльз Леклер', 'Фернандо Алонсо'))

app = QApplication([]) 
window = QWidget() 
window.count_quest = -1
window.total = 0
window.score = 0
cur_quest = 0
ButtonGroup = QButtonGroup() 
window.setWindowTitle('Memory Card') 
btn_ok = QPushButton('Ответить') 
lb_question = QLabel('Когда умер Шоичиро Тойода?') 
 
RadioGroupBox = QGroupBox('Варианты ответов') 
rbtn_1 = QRadioButton('14 февраля 2023') 
rbtn_2 = QRadioButton('8 сенятбря 1945') 
rbtn_3 = QRadioButton('6 октября 2020') 
rbtn_4 = QRadioButton('1991') 
 
ButtonGroup.addButton(rbtn_1) 
ButtonGroup.addButton(rbtn_2) 
ButtonGroup.addButton(rbtn_3) 
ButtonGroup.addButton(rbtn_4) 
 
layout_ans1 = QHBoxLayout() 
layout_ans2 = QVBoxLayout() 
layout_ans3 = QVBoxLayout() 
 
layout_ans2.addWidget(rbtn_1) 
layout_ans2.addWidget(rbtn_2) 
layout_ans3.addWidget(rbtn_3) 
layout_ans3.addWidget(rbtn_4) 
 
layout_ans1.addLayout(layout_ans2) 
layout_ans1.addLayout(layout_ans3) 
 
RadioGroupBox.setLayout(layout_ans1) 
 
AnsGroupBox = QGroupBox('Результат теста') 
lb_result = QLabel('Прав ты или нет?') 
lb_correct = QLabel('Ответ будет тут!') 
 
layout_res = QVBoxLayout() 
layout_res.addWidget(lb_result, alignment=(Qt.AlignLeft | Qt.AlignTop)) 
layout_res.addWidget(lb_correct, alignment=Qt.AlignHCenter, stretch=2) 
AnsGroupBox.setLayout(layout_res) 
 
layout_line1 = QHBoxLayout() 
layout_line2 = QHBoxLayout() 
layout_line3 = QHBoxLayout() 
 
layout_line1.addWidget(lb_question, alignment = (Qt.AlignHCenter | Qt.AlignVCenter)) 
layout_line2.addWidget(RadioGroupBox) 
layout_line2.addWidget(AnsGroupBox) 
RadioGroupBox.show() 
AnsGroupBox.hide() 
 
layout_line3.addStretch(1) 
layout_line3.addWidget(btn_ok, stretch = 2) 
layout_line3.addStretch(1) 
 
layout_card = QVBoxLayout() 
 
layout_card.addLayout(layout_line1, stretch = 2) 
layout_card.addLayout(layout_line2, stretch = 8) 
 
layout_card.addStretch(1) 
layout_card.addLayout(layout_line3, stretch = 1) 
layout_card.addStretch(1) 
 
def question_show(): 
    AnsGroupBox.hide() 
    RadioGroupBox.show() 
    btn_ok.setText('Ответить') 
    ButtonGroup.setExclusive(False) 
    rbtn_1.setChecked(False) 
    rbtn_2.setChecked(False) 
    rbtn_3.setChecked(False) 
    rbtn_4.setChecked(False) 
    ButtonGroup.setExclusive(True) 
 
def result_show(): 
    RadioGroupBox.hide() 
    AnsGroupBox.show() 
    btn_ok.setText("Следующий вопрос")   
 
answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4] 
 
def ask(q : Question): 
    shuffle(answers) 
    answers[0].setText(q.right_answer) 
    answers[1].setText(q.wrong1) 
    answers[2].setText(q.wrong2) 
    answers[3].setText(q.wrong3) 
    lb_question.setText(q.question) 
    lb_correct.setText(q.right_answer) 
    question_show() 
 
def correct_show(res): 
    lb_result.setText(res) 
    result_show() 
 
def check_answer(): 
    if answers[0].isChecked(): 
        correct_show('Правильно!')
        window.score += 1
    else: 
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked(): 
            correct_show('Неверно!')
    print('Количество правильных ответов:',window.score)
    print('Количество вопросов:',window.total)
              
def click_OK(): 
    if 'Ответить' == btn_ok.text(): 
        check_answer() 
    else: 
        next_question()

def next_question():
    window.total += 1
    if window.total >= len(q_list):
        window.total = 0
    cur_quest = randint(0,len(q_list) - 1)
    q = q_list[cur_quest]
    ask(q)

window.setLayout(layout_card) 
window.setWindowTitle('Memory card') 
btn_ok.clicked.connect(click_OK)
next_question()
window.show() 
app.exec_()