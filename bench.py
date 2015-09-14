import pymysql
import timeit
import numpy
import urllib
import requests

start = timeit.default_timer()
connection = pymysql.connect(host='localhost',user='root',db='benchmark',cursorclass=pymysql.cursors.DictCursor)
c = connection.cursor()
c.execute('select sid from students')
results = []
rets = c.fetchall()
for c, i in enumerate(rets[0:3000:3]):
    t = timeit.default_timer()
    url = urllib.quote_plus(i['sid'].lower())
    r = requests.get('http://localhost:5000/student/{}'.format(url))
    if c % 50 == 0:
        print(c)
        print(r.json())
    results.append(timeit.default_timer() - t)

print(timeit.default_timer() - start)
a = numpy.array(results)
print(a.mean())
