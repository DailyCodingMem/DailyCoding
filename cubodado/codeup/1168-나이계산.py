year, tell = input().split(' ')
slice_year = year[0:2]
if tell == '1' or tell == '2':
    minus_year = '19' + slice_year
    print(2012-int(minus_year)+1)
else:
    minus_year = '20' + slice_year
    print(2012-int(minus_year)+1)    