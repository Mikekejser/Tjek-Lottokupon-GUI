import requests
from bs4 import BeautifulSoup
from PyQt5 import QtWidgets
from vindue import Ui_MainWindow
import sys


class MyWindow(QtWidgets.QMainWindow):

	def __init__(self):
		super(MyWindow, self).__init__()

		self.ui = Ui_MainWindow()

		self.ui.setupUi(self)

		self.ui.pushButton.clicked.connect(self.onsLottoClick)
		self.ui.pushButton_2.clicked.connect(self.lorLottoClick)


	def onsLottoClick(self):
		vinder_tal = []
		kupon = []
		rigtige = ""
		antal_rigtige = 0
		antal_tal = 6

		page = requests.get('https://vindertal.com/onsdags-lotto.aspx')
		if page.status_code == 200:
			soup = BeautifulSoup(page.content, 'html.parser')
			for i in range(antal_tal):
				vinder_tal.append(soup.find(id="ContentPlaceHolderDefault_CphMain_AllNumbers_5_LvWinnerNumbers_LblNumber_"+str(i)).contents)
			else:
				self.ui.label_3.setText(f'Kunne ikke hente vindertal. Prøv igen senere. Status kode: {page.status_code}')
		
			vinder_tal = [item for sublist in vinder_tal for item in sublist]

		kupon.append(self.ui.lineEdit.text())
		kupon.append(self.ui.lineEdit_2.text())
		kupon.append(self.ui.lineEdit_3.text())
		kupon.append(self.ui.lineEdit_4.text())
		kupon.append(self.ui.lineEdit_5.text())
		kupon.append(self.ui.lineEdit_6.text())

		for i in vinder_tal:
			if i in kupon:
				antal_rigtige += 1
				rigtige += i+"  "

		if antal_rigtige == 0:
			self.ui.label_3.setText('Ingen rigtige.')
		elif antal_rigtige == 1:
			self.ui.label_3.setText(f'{antal_rigtige} rigtig: {rigtige}')
		else:
			self.ui.label_3.setText(f'{antal_rigtige} rigtige: {rigtige}')
	

	def lorLottoClick(self):
		vinder_tal = []
		kupon = []
		rigtige = ""
		antal_rigtige = 0
		antal_tal = 7

		page = requests.get('https://vindertal.com/loerdags-lotto.aspx')
		if page.status_code == 200:
			soup = BeautifulSoup(page.content, 'html.parser')
			for i in range(antal_tal):
				vinder_tal.append(soup.find(id="ContentPlaceHolderDefault_CphMain_AllNumbers_5_LvWinnerNumbers_LblNumber_"+str(i)).contents)
			else:
				self.ui.label_4.setText(f'Kunne ikke hente vindertal. Prøv igen senere. Status kode: {page.status_code}')
		
			vinder_tal = [item for sublist in vinder_tal for item in sublist]

		kupon.append(self.ui.lineEdit_7.text())
		kupon.append(self.ui.lineEdit_8.text())
		kupon.append(self.ui.lineEdit_9.text())
		kupon.append(self.ui.lineEdit_10.text())
		kupon.append(self.ui.lineEdit_11.text())
		kupon.append(self.ui.lineEdit_12.text())
		kupon.append(self.ui.lineEdit_13.text())

		for i in vinder_tal:
			if i in kupon:
				antal_rigtige += 1
				rigtige += i+"  "

		if antal_rigtige == 0:
			self.ui.label_4.setText('Ingen rigtige.')
		elif antal_rigtige == 1:
			self.ui.label_4.setText(f'{antal_rigtige} rigtig:  {rigtige}')
		else:
			self.ui.label_4.setText(f'{antal_rigtige} rigtige:  {rigtige}')


app = QtWidgets.QApplication([])
 
application = MyWindow()
 
application.show()

sys.exit(app.exec())
