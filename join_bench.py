import pymysql
import timeit
import numpy

start = timeit.default_timer()
connection = pymysql.connect(host='localhost',user='root',db='benchmark',cursorclass=pymysql.cursors.DictCursor)
c = connection.cursor()
c.execute('select id from class')
results = []
rets = c.fetchall()
for c, i in enumerate(rets[0:3000:3]):
    t = timeit.default_timer()
    connection2 = pymysql.connect(host='localhost',user='root',db='benchmark',cursorclass=pymysql.cursors.DictCursor)
    c2 = connection2.cursor()
    if c % 50 == 0:
        print(c)
    c2.execute('select * from students join classes on student = sid where id = %s', i['id'])
    a = c2.fetchall()
    results.append(timeit.default_timer() - t)

print(timeit.default_timer() - start)
a = numpy.array(results)
print(a.mean())
