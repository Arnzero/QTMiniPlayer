import sys, os
from PySide2.QtUiTools import QUiLoader #allows us to import .ui files
from PySide2.QtWidgets import QApplication, QLineEdit, QPushButton, QFileDialog, QAction, QSlider, QMouseEventTransition, QLabel
from PySide2.QtCore import QFile, QObject, QUrl
from PySide2.QtMultimedia import QMediaPlayer
from PySide2.QtGui import QPixmap

class MainWindow(QObject):

    #class constructor
    def __init__(self, ui_file, parent=None):

        #reference to our music player
        self.music_player = QMediaPlayer()
        self.music_player.setVolume(89)
        
        #call parent QObject constructor
        super(MainWindow, self).__init__(parent)

        #add background image
        """
        self.title = "Adrian's boombox"
        self.MainWindow.setWindowTitle(self.title)

        label = QLabel(self)
        pixmap = QPixmap('MW_background.jfif')
        label.setPixmap(pixmap)
        self.setCentralWidget(label)
        self.resize(pixmap.width(), pixmap.height())
        """

        #load the UI file into Python
        ui_file = QFile(ui_file)
        ui_file.open(QFile.ReadOnly)
        loader = QUiLoader()
        self.window = loader.load(ui_file)
        
        #always remember to close files
        ui_file.close()

        #add event listeners
        open_action = self.window.findChild(QAction, 'action_open')
        open_action.triggered.connect(self.open_action_triggered)

        quit_action = self.window.findChild(QAction, 'action_quit')
        quit_action.triggered.connect(self.quit_action_triggered)

        play_button = self.window.findChild(QPushButton, 'play_button')
        play_button.clicked.connect(self.play_button_clicked)

        stop_button = self.window.findChild(QPushButton, 'stop_button')
        stop_button.clicked.connect(self.stop_button_clicked)

        volume_slider = self.window.findChild(QSlider, 'volume_slider')
        """
        #volume_slider.setFocusPolicy(QSlider.StrongFocus)
        #volume_slider.clicked.connect(self.music_player.setVolume(15))
        volume_slider.SliderToMaximum
        """
        volume_slider.setTickInterval(10)
        volume_slider.setSingleStep(1)
        volume_slider.setTickPosition(QSlider.TicksBothSides)
        volume_slider.setMinimum(1)
        volume_slider.setMaximum(100)
        volume_slider.setValue(25)

        volume_slider.valueChanged.connect(self.volume_change)


        volume_plus = self.window.findChild(QPushButton, 'volume_plus')
        volume_plus.clicked.connect(self.volume_plus_button_clicked)
        
        volume_minus = self.window.findChild(QPushButton, 'volume_minus')
        volume_minus.clicked.connect(self.volume_minus_button_clicked)


        #show window to user
        self.window.show()

    def open_action_triggered(self):
        file_name = QFileDialog.getOpenFileName(self.window)
        self.music_player.setMedia(QUrl.fromLocalFile(file_name[0]))
        song_label = self.window.findChild(QLabel, 'song_playing_label')
        display_title = os.path.basename(str(file_name[0]))
        song_label.setText(display_title)
        

    def quit_action_triggered(self):
        self.window.close()

    def play_button_clicked(self):
        self.music_player.play()
        

    def stop_button_clicked(self):
        self.music_player.stop()
    
    def volume_plus_button_clicked(self):
        self.music_player.setVolume(100)

    def volume_minus_button_clicked(self):
        self.music_player.setVolume(0)

    def volume_change(self):
  
        print(self.window.volume_slider.value()) # this prints volume of Qslider object
        #print(self.music_player.volume()) # this prints volume of music_player object
        self.music_player.setVolume(self.window.volume_slider.value())
    

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow('MainWindow.ui')
    sys.exit(app.exec_())
