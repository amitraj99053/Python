# A reference of all the legal format codes

import datetime

x = datetime.datetime.now()

print(x.strftime("%a"))  # Short version  (Wed)
print(x.strftime("%A"))  # Full version   (Wednesday)
print(x.strftime("%w"))  # Weekday as a number 0-6, 0 is Sunday
print(x.strftime("%d"))  # Day of month 01-31   
print(x.strftime("%b"))  # Short version   (Dec)
print(x.strftime("%B"))  # Full version    (December)
print(x.strftime("%m"))  # Month as a number 01-12
print(x.strftime("%y"))  # Year, short version, without century  (18)
print(x.strftime("%Y"))  # Year, full version  (2018)
print(x.strftime("%H"))  # Hour 00-23
print(x.strftime("%I"))  # Hour 00-12
print(x.strftime("%p"))  # AM/PM
print(x.strftime("%M"))  # Minute 00-59
print(x.strftime("%S"))  # Second 00-59 
print(x.strftime("%f"))  # Microsecond 000000-999999
print(x.strftime("%z"))  # UTC offset
print(x.strftime("%Z"))  # Timezone
print(x.strftime("%j"))  # Day number of year 001-366
print(x.strftime("%U"))  # Week number of year, Sunday as the first day of
print(x.strftime("%W"))  # Week number of year, Monday as the first day of
print(x.strftime("%c"))  # Local version of date and time
print(x.strftime("%x"))  # Local version of date
print(x.strftime("%X"))  # Local version of time
print(x.strftime("%%")) # A % character
print(x.strftime("%G"))  # ISO 8601 year
print(x.strftime("%u"))  # ISO 8601 weekday (1-7,
print(x.strftime("%V"))  # ISO 8601 week number (01-53)
print(x.strftime("%C"))  # Century (20)
print(x.strftime("%D"))  # Same as %m/%d/%y
print(x.strftime("%F"))  # Same as %Y-%m-%d
print(x.strftime("%R"))  # Same as %H:%M
print(x.strftime("%T"))  # Same as %H:%M:%S
