import datetime
import time 
import sys

date=datetime.datetime.now()
current_year = date.strftime('%Y')
current_day = date.strftime('%d')
current_mon = date.strftime('%m')

if current_day =='17' and current_mon == '03':
    print(f'Happy St Patricks Day, {current_year}')
elif current_day =='01' and current_mon == '01':
    print(f'Happy Newyaers Day, {current_year}. Lest hope ita good one')
elif current_day =='15' and current_mon == '12':
    print(f'Merry Chrsitmas, {current_year}. Hope  Santa was good to you all')
else:
    sys.exit





