'''All the frontend is here complete with the integration from backend as well.
'''

import sys
import os
import time
from hashlib import sha256
from PyQt5 import QtCore,QtGui,QtWidgets
from PyQt5.QtWidgets import QWidget,QLineEdit,QDesktopWidget, QPushButton, QGraphicsView, QGraphicsScene, QGraphicsPixmapItem
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtCore import QUrl, Qt, QTimer
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5.QtGui import QPixmap


# file file ui yang udah dicompile
from qt.LoginPage import Ui_MainWindow as LoginPage
from qt.Dashboard import Ui_MainWindow as Dashboard
from qt.Quiz import Ui_MainWindow as Quiz
from qt.QuizListening import Ui_MainWindow as QuizListening
from qt.Alert import Ui_MainWindow as Alert
from qt.LoginAlert import Ui_MainWindow as AlertLogin
from qt.Result import Ui_MainWindow as Score

#import classes
from User import User
from QuestionFetcher import QuestionsHandler
from QuizMaker import QuizBrain

DIFFICULTY = ['easy', 'medium', 'hard']
TABLE_NAME = ['vocabularies', 'grammars', 'listening']
DATABASE_NAME = 'my_database.db'

questions_getter = QuestionsHandler(DATABASE_NAME, 'vocabularies', 'grammars', 'listening')
brain = QuizBrain()


class Login(QtWidgets.QMainWindow, LoginPage):
    def __init__(self, obj=None, *args, **kwargs):
        super(Login,self).__init__(*args, **kwargs)

        self.ui = LoginPage()
        self.ui.setupUi(self)
        
        
        # Set fixed size
        self.setFixedSize(1200, 900)
        
        self.alertlogin = None
        self.dashboard_window = None

        
        # connect the button click event to the slot
        self.ui.pushButton_2.clicked.connect(self.switch_page)
        self.ui.pushButton_4.clicked.connect(self.switch_page)
        
        # get text login from lineedit
        self.ui.pushButton.clicked.connect(self.get_login)
        self.ui.pushButton_3.clicked.connect(self.get_register)
        # hide password
        self.ui.pushButton_7.clicked.connect(self.hide_eye1)
        self.ui.pushButton_5.clicked.connect(self.hide_eye2)
        self.ui.pushButton_6.clicked.connect(self.hide_eye3)
        
        #first hide text label on login and register
        self.ui.label_14.hide()
        self.ui.label_15.hide()
    
        self.hide_page = False
        self.hide_icon1 = True
        self.hide_icon2 = True
        self.hide_icon3 = True
        self.icon_eye = QtGui.QIcon('./assets/icon/eye.svg')
        self.icon_eye_off = QtGui.QIcon('./assets/icon/eye-off.svg')
        self.ui.retranslateUi(self)
        
    def showEvent(self, event):
        # Get the geometry of the screen
        screen_geometry = QDesktopWidget().screenGeometry()

        # Get the geometry of the window
        window_geometry = self.frameGeometry()

        # Center the window on the screen
        window_geometry.moveCenter(screen_geometry.center())

        # Move the window to the centered position
        self.move(window_geometry.topLeft())
    
    def hide_eye1(self):
        if self.hide_icon1:
            self.ui.lineEdit_2.setEchoMode(QLineEdit.Password)
            self.ui.pushButton_7.setIcon(self.icon_eye_off)
            self.hide_icon1= False
        else:
            self.ui.lineEdit_2.setEchoMode(QLineEdit.Normal)
            self.ui.pushButton_7.setIcon(self.icon_eye)
            self.hide_icon1= True
    def hide_eye2(self):
        if self.hide_icon2:
            self.ui.lineEdit_4.setEchoMode(QLineEdit.Password)
            self.ui.pushButton_5.setIcon(self.icon_eye_off)
            self.hide_icon2 = False
        else:
            self.ui.lineEdit_4.setEchoMode(QLineEdit.Normal)
            self.ui.pushButton_5.setIcon(self.icon_eye)
            self.hide_icon2 = True
    def hide_eye3(self):
        if self.hide_icon3:
            self.ui.lineEdit_5.setEchoMode(QLineEdit.Password)
            self.ui.pushButton_6.setIcon(self.icon_eye_off)
            self.hide_icon3 = False
        else:
            self.ui.lineEdit_5.setEchoMode(QLineEdit.Normal)
            self.ui.pushButton_6.setIcon(self.icon_eye)
            self.hide_icon3 = True
    
    
    def switch_page(self):
        curr_index = self.ui.stackedWidget.currentIndex()
        next_index = (curr_index + 1) % self.ui.stackedWidget.count()
        self.ui.stackedWidget.setCurrentIndex(next_index)

    def hash_password(self,password):
        pw = sha256()
        pw.update(password.encode('utf-8'))
        return pw.hexdigest()
    
    # connect with backend
    def get_login(self):
        username = self.ui.lineEdit.text()
        password = self.ui.lineEdit_2.text()
        
        verified = User.verify_credential(username=username, password=password)
        
        if username == '':
            self.ui.label_14.setText("Please enter your username.")
            self.ui.label_14.show()
        elif password == '':
            self.ui.label_14.setText("Please enter your password.")
            self.ui.label_14.show()
        elif verified: 
            profile = User(verified)
            
            #NYALAIN DASHBOARD WINDOW
            self.ui.label_14.setText("Login Successful")
            self.ui.label_14.show()
            self.ui.lineEdit.clear()
            self.ui.lineEdit_2.clear()
            self.close()
            
            if self.alertlogin is None:
                self.alertlogin = AlertLoginWindow()
            self.alertlogin.show()

            if self.dashboard_window is None:
                self.dashboard_window = DashboardWindow(profile)
            self.alertlogin.close()
            self.dashboard_window.show()
            
            
        else:
            self.ui.label_14.setText('Login Failed')
            self.ui.label_14.show()
        
     
    # connect wth backend   
    def get_register(self):
        username = self.ui.lineEdit_3.text()
        password_main = self.ui.lineEdit_4.text()
        password_confirm = self.ui.lineEdit_5.text()

        user_exist = User.get_user_by_username(username)
        if username == '':
            self.ui.label_15.setText('Please enter your username.')
            self.ui.label_15.show()
        elif password_main == '' or password_confirm == '':
            self.ui.label_15.setText('Please enter your password.')
            self.ui.label_15.show()
        elif user_exist: 
            self.ui.label_15.setText('Username already exists!')
            self.ui.label_15.show()
        elif password_main != password_confirm:
            self.ui.label_15.setText('Passwords do not match.')
            self.ui.label_15.show()
        else:
            User.register_to_database(username=username, password=password_main, real_name=username)
            profile = User(User.get_user_by_username(username=username))
            self.ui.label_15.setText('Register Successful')
            self.ui.label_15.show()
            #PINDAH PAGE LOGIN
            self.ui.stackedWidget.setCurrentIndex(0)
            self.ui.lineEdit_3.clear()
            self.ui.lineEdit_4.clear()
            self.ui.lineEdit_5.clear()
            self.ui.label_15.hide()
 
class AlertLoginWindow(QtWidgets.QMainWindow, AlertLogin):
    def __init__(self):
        super(AlertLoginWindow,self).__init__()
        
        self.ui = AlertLogin()
        self.ui.setupUi(self)
        self.setFixedSize(310, 125)  
        
        
            
class DashboardWindow(QtWidgets.QMainWindow, Dashboard):
    def __init__(self, profile: User):
        super(DashboardWindow,self).__init__()

        self.profile = profile
        self.question_data = questions_getter.count_questions()
        total_questions = 0
        for table in TABLE_NAME:
            total_questions += self.question_data['total'][table]
        self.total_questions = total_questions
        self.ui = Dashboard()
        self.ui.setupUi(self) 
        self.setFixedSize(1500, 932)  
        
        self.quiz_window = None
        self.login_window = None
        self.alert_window = None
        
        self.setup_page_first()
        #DUMMY FIGURE
        scene = QGraphicsScene(self)
        self.ui.graphicsView.setScene(scene)

        sessions = ['Session 1', 'Session 2', 'Session 3', 'Session 4', 'Session 5']
        exp_gains = np.random.randint(0, 501, len(sessions))  # Random exp gains for demonstration

        fig, ax = plt.subplots()
        ax.bar(sessions, exp_gains, color='skyblue', width=0.5)  # Adjust the width of the bars

        ax.plot(sessions, exp_gains, marker='o', color='orange', linestyle='-')

        ax.set_xlabel('Sessions')
        ax.set_ylabel('Exp Gain')

        
        fig.savefig('graph.png')

        
        pixmap = QPixmap('graph.png')


        pixmap_item = QGraphicsPixmapItem(pixmap)
        scene.addItem(pixmap_item)
        
        self.ui.nav_1.clicked.connect(self.setup_page_first)
        self.ui.nav_2.clicked.connect(self.page_two)
        self.ui.vocab_button.clicked.connect(self.vocab_page)
        self.ui.grammar_button.clicked.connect(self.grammar_page)
        self.ui.listen_button.clicked.connect(self.listen_page)        
        self.ui.pushButton_4.clicked.connect(self.page_two)
        self.ui.pushButton_12.clicked.connect(self.page_two)
        self.ui.pushButton_16.clicked.connect(self.page_two)
        
        self.ui.logout.clicked.connect(self.logout_button)
        # button for quiz
        self.ui.pushButton.clicked.connect(self.vocab_easy)
        self.ui.pushButton_2.clicked.connect(self.vocab_med)
        self.ui.pushButton_3.clicked.connect(self.vocab_hard)
        self.ui.pushButton_9.clicked.connect(self.gramm_easy)
        self.ui.pushButton_10.clicked.connect(self.gramm_med)
        self.ui.pushButton_11.clicked.connect(self.gramm_hard)
        self.ui.pushButton_14.clicked.connect(self.listen)
    
    def logout_button(self):
        if self.alert_window is None:
            self.alert_window = AlertWindow(self.profile)
        self.close_dashboard()
        self.alert_window.show()    

    def close_dashboard(self):
        self.close()       
                    
    
    def setup_page_first(self):
        self.ui.stackedWidget.setCurrentIndex(0)

        self.ui.label.setText(self.profile.username)
        
        self.ui.label_2.setText(self.profile.quotes) # buat quote
        self.ui.label_9.setText(str(self.total_questions)) # buat total question

        self.ui.label_11.setOpenExternalLinks(True)
        self.ui.label_11.setText(self.profile.article_link) 
        
        # ini buat progress vocab, grammar, listening
        self.ui.progressBar_8.value()
        percentage = (self.profile.progress_data['total']['vocabularies']/self.question_data['total']['vocabularies'])*100
        self.ui.progressBar_8.setValue(int(percentage))
        self.ui.progressBar_9.value()
        percentage = (self.profile.progress_data['total']['grammars']/self.question_data['total']['grammars'])*100
        self.ui.progressBar_9.setValue(int(percentage))
        self.ui.progressBar_10.value()
        percentage = (self.profile.progress_data['total']['listening']/self.question_data['total']['listening'])*100
        self.ui.progressBar_10.setValue(int(percentage))
        
        
    def page_two(self):
        self.ui.stackedWidget.setCurrentIndex(1)
    
    # THIS GOES LAST
    def vocab_page(self):
        self.ui.stackedWidget.setCurrentIndex(2)
        
        #easy
        self.ui.progressBar.value()
        percentage = (self.profile.progress_data['vocabularies']['easy']/self.question_data['vocabularies']['easy'])*100
        self.ui.progressBar.setValue(int(percentage))
        #med
        self.ui.progressBar_2.value()
        percentage = (self.profile.progress_data['vocabularies']['medium']/self.question_data['vocabularies']['medium'])*100
        self.ui.progressBar_2.setValue(int(percentage))
        #hard
        self.ui.progressBar_3.value()
        percentage = (self.profile.progress_data['vocabularies']['hard']/self.question_data['vocabularies']['hard'])*100
        self.ui.progressBar_3.setValue(int(percentage))

    
    def grammar_page(self):
        self.ui.stackedWidget.setCurrentIndex(3)
        
        #easy
        self.ui.progressBar_4.value()
        percentage = (self.profile.progress_data['grammars']['easy']/self.question_data['vocabularies']['easy'])*100
        self.ui.progressBar_4.setValue(int(percentage))
        #med
        self.ui.progressBar_5.value()
        percentage = (self.profile.progress_data['grammars']['medium']/self.question_data['vocabularies']['medium'])*100
        self.ui.progressBar_5.setValue(int(percentage))
        #hard
        self.ui.progressBar_6.value()
        percentage = (self.profile.progress_data['grammars']['hard']/self.question_data['vocabularies']['hard'])*100
        self.ui.progressBar_6.setValue(int(percentage))
        
        
    def listen_page(self):
        self.ui.stackedWidget.setCurrentIndex(4)
        
        self.ui.progressBar_7.value()
        percentage = (self.profile.progress_data['total']['listening']/self.question_data['total']['listening'])*100
        self.ui.progressBar_7.setValue(int(percentage))
        
        
        
    def vocab_easy(self):
        #ambil data pertanyaan dari database
        questions = questions_getter.fetch_questions_byCategory('vocabularies', DIFFICULTY[0])
        answered_questions = self.profile.get_userCorrectAnswer(userid = self.profile.userid, from_table='vocabularies', category=DIFFICULTY[0])
        questions_for_user = brain.filter_questions(questions=questions, answered_questions=answered_questions)[:20]
        
        if self.quiz_window is None:
            self.quiz_window = QuizWindow(questions_for_user, self.profile, 'vocabularies')
            self.close()

        # Show the quiz window
        self.quiz_window.show()
        
    def vocab_med(self):
        #ambil data pertanyaan dari database
        questions = questions_getter.fetch_questions_byCategory('vocabularies', DIFFICULTY[1])
        answered_questions = self.profile.get_userCorrectAnswer(userid = self.profile.userid, from_table='vocabularies', category=DIFFICULTY[1])
        questions_for_user = brain.filter_questions(questions=questions, answered_questions=answered_questions)[:20]
        
        if self.quiz_window is None:
            self.quiz_window = QuizWindow(questions_for_user, self.profile, 'vocabularies')
            self.close()

        # Show the quiz window
        self.quiz_window.show()
        
    def vocab_hard(self):
        #ambil data pertanyaan dari database
        questions = questions_getter.fetch_questions_byCategory('vocabularies', DIFFICULTY[2])
        answered_questions = self.profile.get_userCorrectAnswer(userid = self.profile.userid, from_table='vocabularies', category=DIFFICULTY[2])
        questions_for_user = brain.filter_questions(questions=questions, answered_questions=answered_questions)[:20]
        
        if self.quiz_window is None:
            self.quiz_window = QuizWindow(questions_for_user, self.profile, 'vocabularies')
            self.close()

        # Show the quiz window
        self.quiz_window.show()
        
    def gramm_easy(self):
        #ambil data pertanyaan dari database
        questions = questions_getter.fetch_questions_byCategory('grammars', DIFFICULTY[0])
        answered_questions = self.profile.get_userCorrectAnswer(userid = self.profile.userid, from_table='grammars', category=DIFFICULTY[0])
        questions_for_user = brain.filter_questions(questions=questions, answered_questions=answered_questions)[:20]

        if self.quiz_window is None:
            self.quiz_window = QuizWindow(questions_for_user, self.profile, 'grammars')
            self.close()

        # Show the quiz window
        self.quiz_window.show()
        
    def gramm_med(self):
        #ambil data pertanyaan dari database
        questions = questions_getter.fetch_questions_byCategory('grammars', DIFFICULTY[1])
        answered_questions = self.profile.get_userCorrectAnswer(userid = self.profile.userid, from_table='grammars', category=DIFFICULTY[1])
        questions_for_user = brain.filter_questions(questions=questions, answered_questions=answered_questions)[:20]
        
        if self.quiz_window is None:
            self.quiz_window = QuizWindow(questions_for_user, self.profile, 'grammars')
            self.close()

        # Show the quiz window
        self.quiz_window.show()
    
    def gramm_hard(self):
        #ambil data pertanyaan dari database
        questions = questions_getter.fetch_questions_byCategory('grammars', DIFFICULTY[2])
        answered_questions = self.profile.get_userCorrectAnswer(userid = self.profile.userid, from_table='grammars', category=DIFFICULTY[2])
        questions_for_user = brain.filter_questions(questions=questions, answered_questions=answered_questions)[:20]
        
        if self.quiz_window is None:
            self.quiz_window = QuizWindow(questions_for_user, self.profile, 'grammars')
            self.close()

        # Show the quiz window
        self.quiz_window.show()
        
    def listen(self):
        #ambil data pertanyaan dari database
        questions = questions_getter.fetch_all_listening_questions('listening')
        answered_questions = self.profile.get_userCorrectAnswer(userid = self.profile.userid, from_table='listening')
        questions_for_user = brain.filter_questions(questions=questions, answered_questions=answered_questions)[:10]
        
        if self.quiz_window is None:
            self.quiz_window = QuizListeningWindow(questions_for_user, self.profile)
            self.close()

        # Show the quiz window
        self.quiz_window.show()

        

class QuizWindow(QtWidgets.QMainWindow, Quiz):
    def __init__(self, questions: list, profile: User, mode: str, obj=None, *args, **kwargs):
        super(QuizWindow,self).__init__(*args, **kwargs)

        self.profile = profile
        self.mode = mode
        self.ui = Quiz()
        self.ui.setupUi(self) 
        self.setFixedSize(609, 800)  
        self.score_window = None
        
        self.dashboard_window = None  
        self.questions = questions
        self.current_question_index = 0
        self.total_question = len(questions)
        self.setup_quiz(self.questions)
        
        self.correctly_answered_questions = {
            'total_attempted': self.total_question,
            'correct_questions': []
        } # ini buat nyimpen semua answer benar

        self.ui.pushButton.clicked.connect(self.close_hehe)
        self.ui.pushButton_2.clicked.connect(lambda: self.handle_answer(self.ui.pushButton_2.text()))
        self.ui.pushButton_3.clicked.connect(lambda: self.handle_answer(self.ui.pushButton_3.text()))
        self.ui.pushButton_4.clicked.connect(lambda: self.handle_answer(self.ui.pushButton_4.text()))
        self.ui.pushButton_9.clicked.connect(lambda: self.handle_answer(self.ui.pushButton_9.text()))
        
    def setup_quiz(self,questions):
        question = questions[self.current_question_index]
        self.ui.label_5.setText(question['question'].capitalize())
        options = question['options']
        
        self.ui.label_2.setText(str(self.current_question_index+1))
        self.ui.label_3.setText('of')
        self.ui.label_4.setText(str(self.total_question))
        
        self.ui.pushButton_2.setText(options[0])
        self.ui.pushButton_3.setText(options[1])
        self.ui.pushButton_4.setText(options[2])
        self.ui.pushButton_9.setText(options[3])
    
    def compare_answer(self,questions,user_answer):
        question = questions[self.current_question_index]
        answer_benar = question['answer']
        if answer_benar == user_answer:
            question_in_tuple = (self.profile.userid, question['id'], self.mode, question['category'])
            self.correctly_answered_questions['correct_questions'].append(question_in_tuple)
        
    def close_hehe(self):
        self.close()
        if self.dashboard_window is None:    
            self.dashboard_window = DashboardWindow(self.profile)
        self.dashboard_window.show()
         
        
    def handle_answer(self, user_answer):
        self.compare_answer(self.questions, user_answer)
        self.handle_submit()
        
    
    def handle_submit(self):
        self.current_question_index += 1
        if self.current_question_index < self.total_question:
            self.setup_quiz(self.questions)
        else:
            self.profile.played_quiz_this_session = True
            self.profile.insertTo_userCorrectAnswer_table(self.correctly_answered_questions['correct_questions'])
            self.profile.update_attributes(self.correctly_answered_questions)
            self.profile.update_users_table()
            self.close()
            # tampilkan score
            if self.score_window is None:
                self.score_window = ScoreWindow(len(self.correctly_answered_questions['correct_questions']), self.total_question - len(self.correctly_answered_questions['correct_questions'])) #isi parameter correct and wrong
            self.score_window.show()
            
            # kasih delay
            if self.dashboard_window is None:    
                self.dashboard_window = DashboardWindow(self.profile)
            self.dashboard_window.show()
        
        
class QuizListeningWindow(QtWidgets.QMainWindow, QuizListening):
    def __init__(self,questions: list, profile: User):
        super(QuizListeningWindow,self).__init__()

        self.profile = profile
        self.ui = QuizListening()
        self.ui.setupUi(self) 
        self.setFixedSize(609, 800)
        self.audio_played = 0
        self.dashboard_window = None  
        self.score_window = None
        self.questions = questions
        self.current_question_index = False
        self.total_question = len(questions)
        self.setup_quiz_listening(self.questions)

        self.player = QMediaPlayer()
        
        self.correctly_answered_questions = {
            'total_attempted': self.total_question,
            'correct_questions': []
        } # ini buat nyimpen semua answer benar
        
        self.ui.pushButton_11.clicked.connect(self.play_audio)
        self.ui.pushButton_2.clicked.connect(lambda: self.handle_answer(self.ui.pushButton_2.text()))
        self.ui.pushButton_3.clicked.connect(lambda: self.handle_answer(self.ui.pushButton_3.text()))
        self.ui.pushButton_4.clicked.connect(lambda: self.handle_answer(self.ui.pushButton_4.text()))
        self.ui.pushButton_9.clicked.connect(lambda: self.handle_answer(self.ui.pushButton_9.text()))

        self.player.stateChanged.connect(self.update_button_state)
        
        
    def setup_quiz_listening(self,questions):
        self.audio_played = False
        question = questions[self.current_question_index]
        if question['category'] != 'vocabularies':
            options = question['options']
        else:
            options = brain.create_options_for_listening(question['script'])

        self.ui.label_5.setText(question['question'])
        
        brain.create_audio_file(question, question['category'])
        self.ui.label_2.setText(str(self.current_question_index+1))
        self.ui.label_3.setText('of')
        self.ui.label_4.setText(str(self.total_question))
        
        self.ui.pushButton_2.setText(options[0])
        self.ui.pushButton_3.setText(options[1])
        self.ui.pushButton_4.setText(options[2])
        self.ui.pushButton_9.setText(options[3])
    
    def play_audio(self):
        self.player.stop()
        self.player.setMedia(QMediaContent())
        if not self.audio_played:
            temp_file = 'temp_answer.mp3'
            os.system(f'copy answer.mp3 {temp_file}')
            media = QMediaContent(QUrl.fromLocalFile(temp_file))
            self.player.setMedia(media)
            self.player.play()
            self.audio_played = True

            self.player.mediaStatusChanged.connect(lambda status: self.delete_temp_file(temp_file, status))
    
    def delete_temp_file(self, temp_file, status):
        if status == QMediaPlayer.EndOfMedia:
            try:
                os.remove(temp_file)
            except FileNotFoundError:
                return
    
    def update_button_state(self, state):
        if state == QMediaPlayer.PlayingState:
            self.ui.pushButton_2.setEnabled(False)
            self.ui.pushButton_3.setEnabled(False)
            self.ui.pushButton_4.setEnabled(False)
            self.ui.pushButton_9.setEnabled(False)
        else:
            self.ui.pushButton_2.setEnabled(True)
            self.ui.pushButton_3.setEnabled(True)
            self.ui.pushButton_4.setEnabled(True)
            self.ui.pushButton_9.setEnabled(True)
        
        
    def compare_answer(self,questions,user_answer):
        question = questions[self.current_question_index]
        answer_benar = question['answer']
        
        if answer_benar == user_answer:
            question_in_tuple = (self.profile.userid, question['id'], 'listening', question['category'])
            self.correctly_answered_questions['correct_questions'].append(question_in_tuple)
        
    def handle_answer(self, user_answer):
        self.compare_answer(self.questions, user_answer)
        self.handle_submit()
        
    
    def handle_submit(self):
        self.current_question_index += 1
        if self.current_question_index < self.total_question:
            self.setup_quiz_listening(self.questions)
        else:
            self.profile.played_quiz_this_session = True
            self.profile.insertTo_userCorrectAnswer_table(self.correctly_answered_questions['correct_questions'])
            self.profile.update_attributes(self.correctly_answered_questions)
            self.profile.update_users_table()
            self.close()
            # tampilkan score
            if self.score_window is None:
                self.score_window = ScoreWindow(len(self.correctly_answered_questions['correct_questions']), self.total_question - len(self.correctly_answered_questions['correct_questions'])) #isi parameter correct and wrong
            self.score_window.show()
            
            # kasih delay
            if self.dashboard_window is None:    
                self.dashboard_window = DashboardWindow(self.profile)
            self.dashboard_window.show()    

class ScoreWindow(QtWidgets.QMainWindow, Score):
    def __init__(self, correct, wrong):
        super(ScoreWindow, self).__init__() 
        self.ui = Score()
        self.ui.setupUi(self) 
        self.setFixedSize(400, 240)
        self.ui.label_4.setText(str(correct))
        self.ui.label_5.setText(str(wrong))
              
            
class AlertWindow(QtWidgets.QMainWindow, Alert):
    def __init__(self,profile: User):
        super(AlertWindow, self).__init__()
        
        self.ui = Alert()
        self.ui.setupUi(self) 
        self.setFixedSize(400, 200)  
        self.profile = profile
        self.login_window = None
        self.prev_dashboard = DashboardWindow(profile)
        
        self.ui.pushButton.clicked.connect(self.handle_logout)
        self.ui.pushButton_2.clicked.connect(self.handle_cancel)

    def handle_logout(self):
        if self.login_window is None:
           self.login_window = Login()

        if self.prev_dashboard is not None:
            self.prev_dashboard.close_dashboard()  # Tutup jendela dashboard sebelumnya

        self.close()
        self.login_window.show()
        
    
    def handle_cancel(self):
        self.prev_dashboard.show()
        self.close()