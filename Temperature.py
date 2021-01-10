daily_temps = {'sun': 68.8,'mon': 70.2,'tue':67.2,'wed':71.8,
                'thur':73.2,'fri':75.6,'sat':74.0}

daynames = {'sun': 'Sunday', 'mon': 'Monday', 'tue':'Tuesday',
            'wed':'Wednesday','thur':'Thursday','fri':'Friday','sat':'Saturday'}

print('This program will display the average temperature for a given day ')
day = input("Enter 'sun','mon','tue','wed','thur','fri','sat': ")
print('The average temperature for',daynames[day],'was',daily_temps[day],'degrees') 
print('sun' in daily_temps)
print('Sun' in daily_temps)
           