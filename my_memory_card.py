#создай приложение для запоминания информации
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import*
from random import shuffle,randint
app=QApplication([])
win=QWidget()
win.setWindowTitle('Memory Card')
win.resize(400,300)
que=QLabel('Какой национальности не существует?')
button=QPushButton('Ответить')
radiogroup=QGroupBox('Варианты ответов')
rb1=QRadioButton('Энцы')
rb2=QRadioButton('Чулымцы')
rb3=QRadioButton('Смурфы')
rb4=QRadioButton('Алеуты')
l1=QVBoxLayout()
l2=QVBoxLayout()
l3=QHBoxLayout()
l1.addWidget(rb1)
l1.addWidget(rb2)
l2.addWidget(rb3)
l2.addWidget(rb4)
l3.addLayout(l1)
l3.addLayout(l2)
radiogroup.setLayout(l3)
l4=QVBoxLayout()
l4.addWidget(que,alignment=Qt.AlignCenter)
l4.addWidget(radiogroup)


ansgroup=QGroupBox('Результат теста')
ans=QLabel('Правильный ответ')
l5=QHBoxLayout()
l5.addWidget(ans)
ansgroup.setLayout(l5)
ansgroup.hide()
l4.addWidget(ansgroup,stretch=6)
l4.addWidget(button,stretch=1)


RadioGroup = QButtonGroup()
RadioGroup.addButton(rb1)
RadioGroup.addButton(rb2)
RadioGroup.addButton(rb3)
RadioGroup.addButton(rb4)
win.setLayout(l4)
ansgroup.hide()
#Обработка нажатия на кнопку Ответить/Следующий вопрос
def show_question():
    RadioGroup.setExclusive(False)    
    rb1.setChecked(False)
    rb2.setChecked(False)
    rb3.setChecked(False)
    rb4.setChecked(False)
    RadioGroup.setExclusive(True)
def show_result():
    radiogroup.hide()
    ansgroup.show()
    button.setText('Следующий вопрос')
def start_test():
    if button.text() == 'Ответить':
        show_result()
    else:
        show_question()
class Question():
    def __init__(self, question, right_answer, wrong1, wrong2,wrong3):
        self.question=question
        self.right_answer=right_answer
        self.wrong1=wrong1
        self.wrong2=wrong2
        self.wrong3=wrong3

answers = [rb1,rb2,rb3,rb4]
def ask(ques):
    shuffle(answers)
    answers[0].setText(ques.right_answer)
    answers[1].setText(ques.wrong1)
    answers[2].setText(ques.wrong2)
    answers[3].setText(ques.wrong3)
    que.setText(ques.question)
    ans.setText(ques.right_answer)
    radiogroup.show()
    ansgroup.hide
def check_answer():
    if answers[0].isChecked():
        ans.setText('Правильно')
    else:
        ans.setText('Неправильно')
    radiogroup.hide()
    ansgroup.show()
    show_result()
question_list=[]
question_list.append(Question('Государственный язык Бразилии', 'Португальский', "Испанский", "Итальянский","Бразильский"))
question_list.append(
    Question('Дата основания Москвы',
    "1147 год",
    "1153 год",
    "1145 год",
    "1158 год"
    )
)
question_list.append(
    Question('Что находится на Северном полюсе?',
    "Антарктида",
    "Антарктика",
    "Северная Америка",
    "Гренландия"
    )
)
win.cur_question=-1
def next_question():
    show_question()
    win.cur_question = randint(0, len(question_list)-1)
    ask(question_list[win.cur_question])
    button.setText('Ответить')
    radiogroup.show()
    ansgroup.hide()
def click_ok():
    if button.text() == 'Ответить':
        check_answer()
    else:
        next_question()
next_question()
button.clicked.connect(click_ok)
win.show()
app.exec()