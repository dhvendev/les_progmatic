from PyQt6.QtCore import QUrl, Qt
from PyQt6.QtMultimedia import QAudioOutput, QMediaPlayer

from PyQt6.QtWidgets import (QApplication, QWidget,
                             QVBoxLayout, QPushButton,
                             QLabel, QFileDialog,
                             QProgressBar,QHBoxLayout,
                             QSlider, QSizePolicy)


class MusicPlayer(QWidget):
    def __init__(self):
        super().__init__()

        #настройки окна:
        self.setWindowTitle("MusicPlayer")
        self.setGeometry(0, 0, 550, 200)
        self.setMaximumSize(550, 200)
        self.setMinimumSize(550, 200)

        #подключаем медиа плейер
        self.filename = ""
        self.player = QMediaPlayer()
        self.audio_output = QAudioOutput()
        self.audio_output.setVolume(0.5)
        self.player.setAudioOutput(self.audio_output)

        self.main_layout = QVBoxLayout()
        self.setLayout(self.main_layout)

        self.track_name = QLabel('Сейчас проигрывается: ')
        self.main_layout.addWidget(self.track_name)

        #Центральная панель
        self.center_layout = QHBoxLayout()
        self.main_layout.addLayout(self.center_layout)

        self.playButton = QPushButton("Play", self)
        self.center_layout.addWidget(self.playButton)

        self.pauseButton = QPushButton("Pause", self)
        self.center_layout.addWidget(self.pauseButton)

        self.stopButton = QPushButton("Stop", self)
        self.center_layout.addWidget(self.stopButton)

        #временные метки
        self.time_layout = QHBoxLayout()
        self.main_layout.addLayout(self.time_layout)

        self.label_position = QLabel('00:00')
        self.time_layout.addWidget(self.label_position)

        self.label_duration = QLabel('05:50')
        self.label_duration.setAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)
        self.time_layout.addWidget(self.label_duration)

        #события запуска функций
        self.playButton.clicked.connect(self.play)
        self.stopButton.clicked.connect(self.stop)
        self.pauseButton.clicked.connect(self.pause)

    def play(self):
        if not self.filename:
            self.filename = 'music.mp3'
            self.player.setSource(QUrl.fromLocalFile(self.filename))
            self.track_name.setText(f'Сейчас проигрывается: {self.filename}')
        self.player.play()

    def stop(self):
        self.player.stop()
        self.player.setPosition(0)

    def pause(self):
        self.player.pause()




if __name__ == "__main__":
    app = QApplication([])
    player = MusicPlayer()
    player.show()
    app.exec()
