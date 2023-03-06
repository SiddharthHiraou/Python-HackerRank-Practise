from datetime import datetime
import calendar
date_str = input()
date = datetime.strptime(date_str, '%m %d %Y')
print ('{}'.format(calendar.day_name[date.weekday()]).upper())