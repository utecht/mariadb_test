import pymysql
import timeit
import requests
import urllib
import numpy

start = timeit.default_timer()
connection = pymysql.connect(host='localhost',user='root',db='benchmark',cursorclass=pymysql.cursors.DictCursor)
c = connection.cursor()
c.execute('select id from class')
results = []
rets = c.fetchall()
for c, i in enumerate(rets[0:3000:3]):
    t = timeit.default_timer()
    url = urllib.quote_plus(i['id'].lower())
    r = requests.get('http://localhost:5000/class/{}'.format(url))
    if c % 50 == 0:
        print(c)
        print(r.json())
    results.append(timeit.default_timer() - t)

print(timeit.default_timer() - start)
a = numpy.array(results)
print(a.mean())
