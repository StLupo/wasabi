import os

#BASE_DIR = "C:\\Users\\jason\\Documents\\GitHub\\wasabi"
BASE_DIR = "/home/pi/git/wasabi"
PHOTO_DIR_1 = os.path.join(BASE_DIR, "photos/ski")
PHOTO_DIR_2 = os.path.join(BASE_DIR, "photos/cats")
WEATHER_URL = "http://www.yr.no/place/Norway/Buskerud/Kongsberg/Kongsberg/"
ALARM_LIGHT_ON = os.path.join(BASE_DIR, "resources/alarm_on.png")
ALARM_LIGHT_OFF = os.path.join(BASE_DIR, "resources/alarm_off.png")
ALARM_DELAYED = os.path.join(BASE_DIR, "resources/alarm_blue.png")
ALARM_DIALOG_ON = os.path.join(BASE_DIR, "resources/power_button_on_80.png")
ALARM_DIALOG_OFF = os.path.join(BASE_DIR, "resources/power_button_off_80.png")
BACKGROUND_IMAGE = os.path.join(BASE_DIR, "backgrounds/night/night3.png")
DAY_BACKGROUND_FOLDER = os.path.join(BASE_DIR, "backgrounds/pink")
NIGHT_BACKGROUND_FOLDER = os.path.join(BASE_DIR, "backgrounds/night")
ALARM_SOUND =  os.path.join(BASE_DIR,"audio/01_diho.mp3")
CACHE_DIR = os.path.join(BASE_DIR, "cache")

DARK_HOUR_START = 20
DARK_HOUR_END = 7

ALARM_FILE = "/tmp/walarm"

PHOTO_PERIOD_1 = 60
PHOTO_PERIOD_2 = 60
WEATHER_QUERY_PERIOD = 15*60