from math import radians, sqrt, cos
import pandas as pd

dates = pd.date_range(start="1997-12-14", end="2015-01-01")
phases = []



TIME_PERIOD = 29.5
RADIUS = 100


def turn_angle_finder(days_num):
    angle = (360 / TIME_PERIOD) * days_num
    if angle < 360:
        return angle
    else:
        return angle % 360


def phase_teller(angle):
    if 0 <= angle <= 5 or 355 <= angle <= 360:
        return "New Moon"
    elif 85 <= angle <= 95:
        return "First Quarter"
    elif 175 <= angle <= 185:
        return "Full Moon"
    elif 265 <= angle <= 275:
        return "Last Quarter"
    elif 5 < angle < 85:
        return "Waxing Crescent"
    elif 95 < angle < 175:
        return "Waxing Gibbous"
    elif 185 < angle < 265:
        return "Waning Gibbous"
    elif 275 < angle < 355:
        return "Waning Crescent"


for i in range(len(dates)):
    angle = turn_angle_finder(i)
    phase = phase_teller(angle)
    phases.append(phase)

data = {'Date': dates,
        'Phase': phases
        }

df = pd.DataFrame(data, columns = ['Date', 'Phase'])

df.to_excel (r'C:\Users\Reuben\Desktop\export_moon_phases.xlsx', index = False, header=True)