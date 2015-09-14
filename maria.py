from rdflib import Graph
import pymysql

g = Graph()
g.parse('all.turtle', format='turtle')

grad_students = """
select ?id ?student where { ?id rdf:type ub:GraduateCourse . ?student ub:takesCourse ?id . }
"""

under_students = """
select ?id ?student where { ?id rdf:type ub:Course . ?student ub:takesCourse ?id . }
"""
connection = pymysql.connect(host='localhost',user='root',db='benchmark',cursorclass=pymysql.cursors.DictCursor)
c = connection.cursor()
insert_students = """
insert into classes values ("{}", "{}")
"""
for b in g.query(grad_students).bindings:
    sid, name, email, telephone, advisor = '', '', '', '', ''
    try:
        sid = b['?id'].lower()
    except:
        pass
    try:
        name = b['?student'].lower()
    except:
        pass
    c.execute(insert_students.format(sid, name))
    connection.commit()

for b in g.query(under_students).bindings:
    sid, name, email, telephone, advisor = '', '', '', '', ''
    try:
        sid = b['?id'].lower()
    except:
        pass
    try:
        name = b['?student'].lower()
    except:
        pass
    c.execute(insert_students.format(sid, name))
    connection.commit()
