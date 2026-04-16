import sys
input = sys.stdin.readline
valid_month = {'January': '01', 'February': '02', 'March': '03', 'April': '04', 'May': '05', 'June': '06', \
               'July': '07', 'August': '08', 'September': '09', 'October': '10', 'November': '11', 'December': '12'}
n = int(input())
for _ in range(n):
    text = input().rstrip()
    month, day, year = text.replace(',', ' ').split()
    day = int(day)
    year = int(year) % 100

    valid = True
    if (not 0 < day < 32) or (month not in valid_month):
        valid = False

    if valid:
        if day < 10: day = '0' + str(day) 
        if year == 0: year = '00'
        elif year < 10: year = '0' + str(year)
        print(valid_month[month], '/', day, '/', year, sep="")
    else: print("Invalid") 