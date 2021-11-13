import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import Nvidia
import time

class GpuWindow(QMainWindow):
    
    priceLevel = 0

    def __init__(self, name, price, bool, title):
        self.name = name
        self.price = price
        self.bool = bool
        self.title = title
        super().__init__()
        self.initUI()
        self.worker = PriceUpdate(self, self.name, self.price, self.priceLevel, self.bool)
        self.worker.start()

    def initUI(self):
        self.setWindowTitle(self.title)
        i = 0
        self.skip = []
        while(i<len(self.name)):
            if self.bool[i] == 10:
                self.skip.append([self.name[i],"출시예정",self.price[i]])
            else:
                self.skip.append([self.name[i],"0,000,000원",str(self.price[i])+"$"])
            i+=1
        self.rows = self.skip
        headers = ['모델명', '시세', '출시가']

        centerGeometry = QDesktopWidget().availableGeometry().center()
        self.setFixedSize(400, 230)
        frameGeometry = self.frameGeometry()
        frameGeometry.moveCenter(centerGeometry)

        self.tableWidget = QTableWidget(self)
        self.tableWidget.resize(400, 230)
        self.tableWidget.setRowCount(len(self.rows))
        self.tableWidget.setColumnCount(len(headers))
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        
        self.tableWidget.setHorizontalHeaderLabels(headers)
        self.setTableWidgetData()

        self.spinBox = QSpinBox(self)
        self.spinBox.move(8192, 8192)
        self.spinBox.resize(80, 22)
        self.spinBox.setValue(0)
        self.spinBox.setSingleStep(1)
        self.spinBox.setMinimum(0)
        self.spinBox.setMaximum(5)
        self.spinBox.valueChanged.connect(self.spinBoxChanged)

        self.statusBar = QStatusBar(self)
        self.setStatusBar(self.statusBar)
        self.slider = QSlider(Qt.Horizontal, self)
        self.slider.move(250, 20)
        self.slider.setRange(0, 5)
        self.slider.valueChanged.connect(self.sliderChanged)

        button = QPushButton("새로고침", self)
        button.move(250, 80)
        button.clicked.connect(self.pressed)

    def pressed(self):
        self.worker = PriceUpdate(self, self.name, self.price, self.priceLevel, self.bool)
        self.worker.start()
        
    def spinBoxChanged(self):
        value = self.spinBox.value()
        self.slider.setValue(value)
        self.statusBar.showMessage('%d' % value)
    
    def sliderChanged(self):
        value = self.slider.value()
        self.spinBox.setValue(value)
        self.statusBar.showMessage('%d''단계' % value)
        self.priceLevel = value

    def setTableWidgetData(self):
        for b in range(len(self.rows)):
            for c in range(len(self.rows[b])):
                item = QTableWidgetItem(self.rows[b][c])
                if c == 0:
                    item.setTextAlignment(Qt.AlignRight)
                self.tableWidget.setItem(b, c, item)
                
        self.tableWidget.resizeColumnsToContents()
        self.tableWidget.resizeRowsToContents()

class PriceUpdate(QThread):
    def __init__(self, window, name, price, priceLevel, bool):
        super().__init__()
        self.mainWindow = window
        self.gpuName = name
        self.gpuPrice = price
        self.gpuPriceLevel = priceLevel
        self.gpuBool = bool

    def run(self):
        i = 0
        while(i<len(self.gpuName)):
            if self.gpuBool[i] == 0:
                self.mainWindow.tableWidget.item(i,1).setText(Nvidia.YsrpBest(self.gpuName[i] ,self.gpuPrice[i]*(1+0.1*self.gpuPriceLevel)))
            if self.gpuBool[i] == 5:
                self.mainWindow.tableWidget.item(i,1).setText(Nvidia.YsrpBest(self.gpuName[i] ,(self.gpuPrice[i]*(1+0.1*self.gpuPriceLevel))/2))
            i+=1

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setFixedSize(600, 150)

        button1 = QPushButton("RTX30", self)
        button1.move(50, 25)
        button1.clicked.connect(self.button1Clicked)

        button2 = QPushButton("RTX20", self)
        button2.move(150, 25)
        button2.clicked.connect(self.button2Clicked)
        
        button3 = QPushButton("GTX16", self)
        button3.move(250, 25)
        button3.clicked.connect(self.button3Clicked)

        button4 = QPushButton("GTX10", self)
        button4.move(350, 25)
        button4.clicked.connect(self.button4Clicked)

        button5 = QPushButton("GTX900", self)
        button5.move(450, 25)
        button5.clicked.connect(self.button5Clicked)

    def button1Clicked(self):
        rtx30.show()
        
    def button2Clicked(self):
        rtx20.show()
        
    def button3Clicked(self):
        gtx16.show()
        
    def button4Clicked(self):
        gtx10.show()
        
    def button5Clicked(self):
        gtx900.show()



class Load(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle("Now Loading")

if __name__ == "__main__":
    
    app = QApplication(sys.argv)
    
    name30 = ['RTX3090S','RTX3090','RTX3080TI','RTX3080','RTX3070TI','RTX3070','RTX3060TI','RTX3060','RTX3050']
    price30 = ["출시예정",1499,1199,699,599,499,399,329,"출시예정"]
    bool30 = [10,0,0,0,0,0,0,0,10]

    name20 = ['TITAN_RTX','RTX 2080TI','RTX2080S','RTX2080','RTX2070S','RTX2070','RTX2060S','RTX2060']
    price20 = [2499,999,699,699,499,499,399,349]
    bool20 = [5,5,5,5,5,5,5,5]

    name16 = ['GTX1660TI','GTX1660S','GTX1660','GTX1650S','GTX1650']
    price16 = [279,229,219,159,149]
    bool16 = [5,5,5,5,5]

    name10 = ['TITAN_V','TITAN_XP','TITAN_X','GTX1080TI','GTX1080','GTX1070TI','GTX1060','GTX1050TI','GTX1050','GT1030']
    price10 = [2999,1199,1199,699,599,399,299,139,109,79]
    bool10 = [5,5,5,5,5,5,5,5,5,5]

    name900 = ['TITAN_X','GTX980TI','GTX980','GTX970','GTX960','GTX950']
    price900 = [999,649,549,329,199,159]
    bool900 = [5,5,5,5,5,5]

    gtx900 = GpuWindow(name900, price900, bool900, 'GeForce 900 Series')

    gtx10 = GpuWindow(name10, price10, bool10, 'GeForce 10 Series')

    gtx16 = GpuWindow(name16, price16, bool16, 'GeForce 16 Series')

    rtx20 = GpuWindow(name20, price20, bool20, 'GeForce 20 Series')

    rtx30 = GpuWindow(name30, price30, bool30, 'GeForce 30 Series')

    window = MyWindow()
    window.show()
 
    sys.exit(app.exec_())