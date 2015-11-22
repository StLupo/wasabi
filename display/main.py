# -*- coding: utf-8 -*-


import sys
import time
import os
import random
import urllib2
import pygame
import shutil

from PyQt4 import QtCore, QtGui

import kaja_clock
import set_alarm_dialog
import yr_info 
#from sip import enableautoconversion

from config import *





class AlarmDialog(QtGui.QDialog):
    def __init__(self):
        QtGui.QDialog.__init__(self)

        # Set up the user interface from Designer.
        self.ui = set_alarm_dialog.Ui_Dialog()
        self.ui.setupUi(self)



class MyMainWindow(QtGui.QMainWindow):
 
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self._show_colon = True
        self._ctr = 0
        self._is_night = False
        self._is_day = False
        
        self._set_volume(85)
        self._enable_audio_jack(False)
        pygame.mixer.init()
        pygame.mixer.music.load(ALARM_SOUND)
 
    def start(self, ui):
        
        #Link to the UI
        self._ui = ui
        
        #Our Timer
        self._timer = QtCore.QTimer(self)
        self._timer.timeout.connect(self.time)
        self._timer.start(1000)
        
        #Background
        hour = int(time.strftime("%H"))
        if hour >= 7 and hour <=20:
            self._is_night = False
        else:
            self._is_night = True
        self._update_background(self._is_night)
        
        #Hide the mouse pointer
        self._hide_pointer()
        
    def _update_background(self, is_night):
        
        self._ui.centralwidget.setStyleSheet("QWidget { color : white; }")
        palette = QtGui.QPalette()
        if is_night:
            photo_path = self._random_photo_path(NIGHT_BACKGROUND_FOLDER)
            self._ui.clock.setStyleSheet("QLabel {color:#606060;}")
        else:
            photo_path = self._random_photo_path(DAY_BACKGROUND_FOLDER)
            self._ui.clock.setStyleSheet("QLabel {color:#ffffff;}")
        palette.setBrush(self.backgroundRole(), QtGui.QBrush(QtGui.QImage(photo_path)))
        self.setPalette(palette)
        
    def _random_photo_path(self, photo_dir):
        
        files = os.listdir(photo_dir)
        idx = random.randint(0,len(files) - 1)
        return os.path.join(photo_dir, files[idx])
        
    def _random_photo_in_label(self, photo_dir, label):
        
        if self._is_night:
            label.clear()
        else:
            files = os.listdir(photo_dir)
            idx = random.randint(0,len(files) - 1)
            label.setPixmap(QtGui.QPixmap(self._random_photo_path(photo_dir)))
            label.setScaledContents(True)
        
    def _check_weather(self):
        
        ywf = yr_info.YrWeatherFetcher()
        ywf.open(WEATHER_URL)
        ret = ywf.get_result(CACHE_DIR)
        
        for i, info in enumerate(ret):
            time_label = [self._ui.yr_time_1, self._ui.yr_time_2, self._ui.yr_time_3, self._ui.yr_time_4][i]
            temp_label = [self._ui.yr_temp_1, self._ui.yr_temp_2, self._ui.yr_temp_3, self._ui.yr_temp_4][i]
            gphx_label = [self._ui.yr_precip_1, self._ui.yr_precip_2, self._ui.yr_precip_3, self._ui.yr_precip_4][i]
            time_label.setText(info[0].decode("utf-8"))
            if info[1][0] in ["-", "0"]:
                temp_label.setStyleSheet("QLabel {color:#6495ed;}")
            else:
                temp_label.setStyleSheet("QLabel {color:red;}")
            temp_label.setText(info[1].decode("utf-8"))
            gphx_label.setPixmap(QtGui.QPixmap(info[2]))
        
    def _update_alarm(self):
        
        alarm_string = "No Alarm"
        alarm_light = ALARM_LIGHT_OFF
        _f = os.popen("crontab -l")
        lines = _f.readlines()
        for line in lines:
            if line.count(ALARM_FILE) and line[0] != "#":
                alarm_light = ALARM_DELAYED
                elements = line.split()
                minute = int(elements [0])
                hour = int(elements[1])
                alarm_string = "Alarm:  %02i:%02i" % (hour, minute)
                days = elements[4]
                if days.count("-"):
                    start_day, end_day = days.split("-")
                    days = range(int(start_day), int(end_day) + 1)
                else:
                    days = [int(el) for el in days.split(",")]
                now_day = int(time.strftime("%w"))
                now_hour = int(time.strftime("%H"))
                now_minute = int(time.strftime("%M"))
                if days.count(now_day + 1):
                    alarm_light = ALARM_LIGHT_ON
                    break
                elif days.count(now_day):
                    if now_hour < hour:
                        alarm_light = ALARM_LIGHT_ON
                        break
                    elif now_hour == hour and now_minute < minute:
                        alarm_light = ALARM_LIGHT_ON
                        break
        self._ui.alarm_light.setPixmap(QtGui.QPixmap(alarm_light))   
        self._ui.alarm_time.setText(alarm_string) 
        
    def _check_alarm(self):
        
        if os.path.exists(ALARM_FILE):
            print "Found Alarm!!!"
            #Remove the alarm file so we don't keep alarming
            os.remove(ALARM_FILE)
            #Set the volume back to 100%
            self._enable_audio_jack(True)
            pygame.mixer.music.play(1)
        else:
            pass
            
    def _set_volume(self, pct):
        
        vol_cmd = "amixer cset numid=1 -- %i%%" % (pct)
        os.system(vol_cmd)
        
    def _enable_audio_jack(self, enable):
          
        if enable:
            print "Enabling Audio Jack"
            cmd = "sudo amixer cset numid=3 1"
        else:
            print "Disabling Audio Jack"
            cmd = "sudo amixer cset numid=3 2"
        os.system(cmd)
        
    def _check_playback(self):
        
        if not pygame.mixer.music.get_busy():
            print "Not Busy"
            self._enable_audio_jack(False)
        else:
            print "Busy"

    def _show_alarm_dlg(self):

        self._dialog  = AlarmDialog()
        self._dialog.show()
        # self._dialog = QtGui.QDialog()
        # self._dialog.accept = self.accept_alarm
        # self._dialog.reject = self.reject_alarm
        # self._dialog.ui = set_alarm_dialog.Ui_Dialog()
        # self._dialog.ui.setupUi(self._dialog)
        # self._dialog.show()

    def accept_alarm(self):
        print "Accept"
        self._dialog.close()

    def reject_alarm(self):
        print "Reject"
        self._dialog.close()
            
    def mousePressEvent(self, QMouseEvent):
        
        pygame.mixer.music.stop()
        self._show_alarm_dlg()
    
    def _hide_pointer(self):
        
        #QtGui.QCursor.setPos(QtCore.QPoint(800, 480))
        self.setCursor(QtCore.Qt.BlankCursor)
            
    def time(self):
        
        #Show Time
        if self._show_colon:
            self._ui.clock.setText(time.strftime("%H"+":"+"%M."))
        else:
            self._ui.clock.setText(time.strftime("%H"+":"+"%M"))
        self._show_colon = not self._show_colon
            
        #Show Date
        self._ui.date.setText(time.strftime("%A  %d. %m %Y"))
        
        #Show Alarm
        self._update_alarm()
        
        #Check Alarm
        self._check_alarm()
        
        #Check sound playback and shut the jack up if nothing playing
        self._check_playback()
              
            
        #Update photos
        if not self._ctr % PHOTO_PERIOD_1:
            self._random_photo_in_label(PHOTO_DIR_1, self._ui.graphics_upper)
        if not self._ctr % PHOTO_PERIOD_2:
            self._random_photo_in_label(PHOTO_DIR_2, self._ui.graphics_lower)
        
        #Update weather
        if not (self._ctr - 1) % WEATHER_QUERY_PERIOD:
            self._check_weather()
            
        #Update Background
        hour = int(time.strftime("%H"))
        if hour >= DARK_HOUR_END and hour <=DARK_HOUR_START:
            if self._is_night:
                self._is_night = False
                self._update_background(self._is_night)
                print "Change to day"
        else:
            if not self._is_night:
                self._is_night = True
                self._update_background(self._is_night)
                print "Change to night"
            
        self._ctr += 1

def main():
    app = QtGui.QApplication(sys.argv)
    window = MyMainWindow()
    ui = kaja_clock.Ui_MainWindow()
    ui.setupUi(window)
    window.start(ui)
    window.show()
 
    sys.exit(app.exec_())
 
if __name__ == "__main__":
    main()
