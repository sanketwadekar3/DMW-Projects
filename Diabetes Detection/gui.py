#!/usr/bin/env python3

"""
GUI for diabetes prediction.
"""
import sys

from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QLineEdit, QVBoxLayout, QHBoxLayout, QApplication, QMessageBox
from PyQt5.QtGui import QDoubleValidator, QFont
from PyQt5.QtCore import Qt, QLine

import Random_Forest
import Support_Vector_Machine
import KNN

class Diabetes(QWidget):

    def __init__(self) -> None :
        super(Diabetes, self).__init__()
        self.sub_head = QLabel("Patient's Details")
        self.sub_head.setFont(QFont("Times",24, weight=QFont.Bold))
        self.l0 = QLineEdit()
        self.l1 = QLineEdit()
        self.l2 = QLineEdit()
        self.l3 = QLineEdit()
        self.l4 = QLineEdit()
        self.l5 = QLineEdit()
        self.t0 = QLabel("Patient's Name:")
        self.t1 = QLabel("Plasma glucose concentration:")
        self.t2 = QLabel("Diastolic blood pressure:")
        self.t3 = QLabel("Triceps skin fold thickness:")
        self.t4 = QLabel("Serum insulin:")
        self.t5 = QLabel("Body mass index:")
        self.r1 = QLabel("")
        self.r2 = QLabel("")
        self.r3 = QLabel("")
        self.r4 = QLabel("")
        self.r5 = QLabel("")
        self.h1 = QHBoxLayout()
        self.h0 = QHBoxLayout()
        self.h2 = QHBoxLayout()
        self.h3 = QHBoxLayout()
        self.h4 = QHBoxLayout()
        self.h5 = QHBoxLayout()
        self.clbtn = QPushButton("CLEAR")
        self.clbtn.setFixedWidth(100)
        self.rf = QPushButton("Random Forest")
        self.rf.setFixedWidth(100)
        self.svm = QPushButton("SVM")
        self.svm.setFixedWidth(100)
        self.knn = QPushButton("KNN")
        self.knn.setFixedWidth(100)
        self.v1_box = QVBoxLayout()
        self.v2_box = QVBoxLayout()
        self.final_hbox = QHBoxLayout()
        self.initui()

    def initui(self) -> None:
        """ The gui is created and widgets elements are set here """
        self.v1_box.addWidget(self.sub_head)
        self.v1_box.addSpacing(10)
        self.v1_box.setSpacing(5)
        self.l1.setValidator(QDoubleValidator())
        self.l2.setValidator(QDoubleValidator())
        self.l3.setValidator(QDoubleValidator())
        self.l4.setValidator(QDoubleValidator())
        self.l5.setValidator(QDoubleValidator())
        #self.l0.setToolTip("Enter name here")
        #self.l1.setToolTip("2 hours in an oral glucose tolerance test \n 70-180 mg/dl")
        #self.l2.setToolTip("80-140mm Hg")
        #self.l3.setToolTip("10-50mm")
        #self.l4.setToolTip("15-276mu U/ml")
        #self.l5.setToolTip("weight in kg/(height in m)^2 \n 10-50")
        self.l0.setFixedSize(265, 30)
        self.l1.setFixedSize(40,30)
        self.l2.setFixedSize(40,30)
        self.l3.setFixedSize(40,30)
        self.l4.setFixedSize(40,30)
        self.l5.setFixedSize(40,30)
        self.h0.addWidget(self.t0)
        self.h0.addWidget(self.l0)
        self.v1_box.addLayout(self.h0)
        self.h1.addWidget(self.t1)
        self.h1.addWidget(self.l1)
        self.h1.addWidget(self.r1)        
        self.v1_box.addLayout(self.h1)
        self.h2.addWidget(self.t2)
        self.h2.addWidget(self.l2)
        self.h2.addWidget(self.r2)       
        self.v1_box.addLayout(self.h2)
        self.h3.addWidget(self.t3)
        self.h3.addWidget(self.l3)
        self.h3.addWidget(self.r3)       
        self.v1_box.addLayout(self.h3)
        self.h4.addWidget(self.t4)
        self.h4.addWidget(self.l4)
        self.h4.addWidget(self.r4)      
        self.v1_box.addLayout(self.h4)
        self.h5.addWidget(self.t5)
        self.h5.addWidget(self.l5)
        self.h5.addWidget(self.r5)      
        self.v1_box.addLayout(self.h5)
        self.h6 = QHBoxLayout()
        self.rf.clicked.connect(lambda: self.test_input_rf())
        
        self.svm.clicked.connect(lambda: self.test_input_svm())
        
        self.knn.clicked.connect(lambda: self.test_input_knn())

        self.clbtn.clicked.connect(lambda: self.clfn())
        self.h6.addWidget(self.rf)
        self.h6.addWidget(self.svm)
        self.h6.addWidget(self.knn)
        self.h6.addWidget(self.clbtn)
        self.v1_box.addLayout(self.h6)
        self.report_ui()
        self.final_hbox.addLayout(self.v1_box)
        self.final_hbox.addSpacing(40)
        self.final_hbox.addLayout(self.v2_box)
        self.setLayout(self.final_hbox)

    def report_ui(self):
        self.v2_box.setSpacing(6)
        self.report_subhead = QLabel("About")
        self.report_subhead.setAlignment(Qt.AlignCenter)
        self.report_subhead.setFont(QFont("Times",24, weight=QFont.Bold))
        self.v2_box.addWidget(self.report_subhead)
        self.details = QLabel("This model uses Random Forest classifier, Support Vector classifier, K-Nearest Neighbours classifier.\nWe have used PIMA Indians diabetes dataset.")
        self.details.setFont(QFont("Arial",14, weight=QFont.Bold))
        self.details.setAlignment(Qt.AlignLeft)
        self.details.setWordWrap(True)
        self.model_details = QLabel("Fill details and press submit to see details.")
        self.model_details.setWordWrap(True)
        self.v2_box.addWidget(self.details)
        self.results = QLabel(" ")
        self.results.setWordWrap(True)
        self.v2_box.addWidget(self.results)
        self.v2_box.addWidget(self.model_details)

    def clfn(self):
        """ clear all the text fields via clear button"""
        self.l0.clear()
        self.l1.clear()
        self.l2.clear()
        self.l3.clear()
        self.l3.clear()
        self.l4.clear()
        self.l5.clear()
        self.report_subhead.setText("About")
        self.model_details.setText("Fill details and press submit to see details.")
        self.results.setText(" ")
        self.details.setText("")
        #print(self.frameGeometry().width())
        #print(self.frameGeometry().height())

    def test_input_rf(self) -> None:
        """ test for diabetes"""
        my_dict = {"B":float(self.l1.text()), "C":float(self.l2.text()),"D":float(self.l3.text()), "E":float(self.l4.text()), "F": float(self.l5.text())}
        rf_output = Random_Forest.check_input(my_dict)
        self.setFixedSize(850, 342)
        self.report_subhead.setText("Reports")
        self.model_details.setText("Random Forest classifier used.\nAccuracy of model: 77.92%\nWe have used PIMA Indians diabetes dataset.")
        self.details.setText("Patient's name: {}\nPlasma glucose concentration: {} \
\nDiastolic blood pressure: {}\nTriceps skin fold thickness: {}\nSerum insulin: {}\nBody mass index: {}".format(self.l0.text(), self.l1.text(), self.l2.text(), self.l3.text(),self.l4.text(),self.l5.text()))

        if rf_output==0:
            op=self.results.setText("Diagnosis suggests that patient does not suffers from diabetes.")
        else:
            op=self.results.setText("Our diagnosis suggests patient does suffer from diabetes.\nPlease get checked soon.")
        self.results.setFont(QFont("Arial",14, weight=QFont.Bold))


    def test_input_svm(self) -> None:
        """ test for diabetes"""
        my_dict = {"B":float(self.l1.text()), "C":float(self.l2.text()),"D":float(self.l3.text()), "E":float(self.l4.text()), "F": float(self.l5.text())}
        svm_output = Support_Vector_Machine.check_input(my_dict)
        self.setFixedSize(850, 342)
        self.report_subhead.setText("Reports")
        self.model_details.setText("Support Vector Machine classifier used.\nAccuracy of model: 69.48%\nWe have used PIMA Indians diabetes dataset.")
        self.details.setText("Patient's name: {}\nPlasma glucose concentration: {} \
\nDiastolic blood pressure: {}\nTriceps skin fold thickness: {}\nSerum insulin: {}\nBody mass index: {}".format(self.l0.text(), self.l1.text(), self.l2.text(), self.l3.text(),self.l4.text(),self.l5.text()))
        
        if svm_output==0:
            self.results.setText("Diagnosis suggests that patient does not suffers from diabetes.")
        else:
            self.results.setText("Our diagnosis suggests patient does suffer from diabetes.\nPlease get checked soon.")
        self.results.setFont(QFont("Arial",14, weight=QFont.Bold))

    def test_input_knn(self) -> None:
        """ test for diabetes"""
        my_dict = {"B":float(self.l1.text()), "C":float(self.l2.text()),"D":float(self.l3.text()), "E":float(self.l4.text()), "F": float(self.l5.text())}
        knn_output = KNN.check_input(my_dict)
        self.setFixedSize(850, 342)
        self.report_subhead.setText("Reports")
        self.model_details.setText("K-Nearest Neighbours classifier used.\nAccuracy of model: 81.16%\nWe have used PIMA Indians diabetes dataset.")
        self.details.setText("Patient's name: {}\nPlasma glucose concentration: {} \
\nDiastolic blood pressure: {}\nTriceps skin fold thickness: {}\nSerum insulin: {}\nBody mass index: {}".format(self.l0.text(), self.l1.text(), self.l2.text(), self.l3.text(),self.l4.text(),self.l5.text()))

        if knn_output==0:
           self.results.setText("Diagnosis suggests that patient does not suffers from diabetes.")
        else:
            self.results.setText("Our diagnosis suggests patient does suffer from diabetes.\nPlease get checked soon.")
        self.results.setFont(QFont("Arial",14, weight=QFont.Bold))


    def mwindow(self) -> None:
        """ window features are set here and application is loaded into display"""
        self.setFixedSize(898, 422)
        self.setWindowTitle("Diabetes Detection")
        self.show()


if __name__=="__main__":
    app = QApplication(sys.argv)
    a_window = Diabetes()
    a_window.mwindow()
    sys.exit(app.exec_())
