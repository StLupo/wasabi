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



def _read_alarm():

    ret_hour = 0
    ret_minute = 0
    ret_days = []
    ret_active = False

    _f = os.popen("crontab -l")
    lines = _f.readlines()
    for line in lines:
        if line.count(ALARM_FILE):
            if line[0] != "#":
                ret_active = True
            elements = line.split()
            ret_minute = int(elements [0])
            ret_hour = int(elements[1])
            days = elements[4]
            if days.count("-"):
                ret_day = 8
                start_day, end_day = days.split("-")
                ret_days = range(int(start_day), int(end_day) + 1)
            else:
                ret_days = [int(el) for el in days.split(",")]
    return ret_days, ret_hour, ret_minute, ret_active


class AlarmDialog(QtGui.QDialog):
    def __init__(self):

        self._alarm_state = None
        QtGui.QDialog.__init__(self)

        # Set up the user interface from Designer.
        self.ui = set_alarm_dialog.Ui_Dialog()
        self.ui.setupUi(self)
        alarm_days, alarm_hour, alarm_minute, alarm_state = _read_alarm()
        self.ui.radio_sun.setChecked(False)
        self.ui.radio_man.setChecked(False)
        self.ui.radio_tue.setChecked(False)
        self.ui.radio_wed.setChecked(False)
        self.ui.radio_thu.setChecked(False)
        self.ui.radio_fri.setChecked(False)
        self.ui.radio_sat.setChecked(False)
        for day in alarm_days:
            if day == 0:
                self.ui.radio_sun.setChecked(True)
            elif day == 1:
                self.ui.radio_man.setChecked(True)
            elif day == 2:
                self.ui.radio_tue.setChecked(True)
            elif day == 3:
                self.ui.radio_wed.setChecked(True)
            elif day == 4:
                self.ui.radio_thu.setChecked(True)
            elif day == 5:
                self.ui.radio_fri.setChecked(True)
            elif day == 6:
                self.ui.radio_sat.setChecked(True)
        self.ui.timeEdit.setTime(QtCore.QTime(alarm_hour, alarm_minute))
        if alarm_state == True:
            self.ui.pushButton.setIcon(QtGui.QIcon(QtGui.QPixmap(ALARM_DIALOG_ON)))
            self._alarm_state = True
        else:
            self.ui.pushButton.setIcon(QtGui.QIcon(QtGui.QPixmap(ALARM_DIALOG_OFF)))
            self._alarm_state = False

        self.connect(self.ui.pushButton, QtCore.SIGNAL('clicked()'), self._toggle_alarm)

    def reject(self):
        
        QtGui.QDialog.reject(self)
        
    def accept(self):
        try:
            hour, minute, days, on = self._get_result()

            with open(os.path.join(CACHE_DIR, "addcron.txt"), "w") as _f:
                _f.write("%s%i %i * * %s touch %s%s" % ("" if on else "#", minute, hour, ",".join([str(el) for el in days]), ALARM_FILE, os.linesep))
            os.system("crontab %s" % (os.path.join(CACHE_DIR, "addcron.txt")))
        except:
            with open("fail.txt", "w") as _f:
                import traceback
                traceback.print_exc(file = _f)


        QtGui.QDialog.accept(self)
        
    def _toggle_alarm(self):

        self._alarm_state = not self._alarm_state
        if self._alarm_state == True:
            self.ui.pushButton.setIcon(QtGui.QIcon(QtGui.QPixmap(ALARM_DIALOG_ON)))
        else:
            self.ui.pushButton.setIcon(QtGui.QIcon(QtGui.QPixmap(ALARM_DIALOG_OFF)))


    def _get_result(self):

        ret_hour = 0
        ret_minute = 0
        ret_days = [0]
        ret_on = False

        alarm_time = self.ui.timeEdit.time()
        ret_hour = alarm_time.hour()
        ret_minute = alarm_time.minute()
        if self.ui.radio_sun.checkState():
            ret_days.append(0)
        if self.ui.radio_man.checkState():
            ret_days.append(1)
        if self.ui.radio_tue.checkState():
            ret_days.append(2)
        if self.ui.radio_wed.checkState():
            ret_days.append(3)
        if self.ui.radio_thu.checkState():
            ret_days.append(4)
        if self.ui.radio_fri.checkState():
            ret_days.append(5)
        if self.ui.radio_sat.checkState():
            ret_days.append(6)

        ret_on = self._alarm_state
        return ret_hour, ret_minute, ret_days, ret_on


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
        self._dialog.setStyleSheet("background-color:#ff4081;")
        self._dialog.show()

    def mousePressEvent(self, QMouseEvent):
        
        if not pygame.mixer.music.get_busy():
            self._show_alarm_dlg()
        else:
            pygame.mixer.music.stop()
            
    
    def _hide_pointer(self):
        
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
