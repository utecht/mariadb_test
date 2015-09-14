from rdflib import Graph
import pymysql

g = Graph()
g.parse('all.turtle', format='turtle')

grad_students = """
select
    ?sid ?name ?email ?advisor ?telephone
where {
    ?sid rdf:type ub:GraduateStudent .
    ?sid ub:name ?name .
    optional { ?sid ub:email ?email } .
    optional { ?sid ub:telephone ?telephone } .
    optional { ?sid ub:advisor ?advisor }
}"""

under_students = """
select
    ?sid ?name ?email ?advisor ?telephone
where {
    ?sid rdf:type ub:UndergraduateStudent .
    ?sid ub:name ?name .
    optional { ?sid ub:email ?email } .
    optional { ?sid ub:telephone ?telephone } .
    optional { ?sid ub:advisor ?advisor }
}"""
connection = pymysql.connect(host='localhost',user='root',db='benchmark',cursorclass=pymysql.cursors.DictCursor)
c = connection.cursor()
insert_students = """
insert into students values ("{}", "{}", "{}", "{}", "{}")
"""
for b in g.query(grad_students).bindings:
    sid, name, email, telephone, advisor = '', '', '', '', ''
    try:
        sid = b['?sid'].lower()
    except:
        pass
    try:
        name = b['?name'].value
    except:
        pass
    try:
        email = b['?email'].value
    except:
        pass
    try:
        telephone = b['?telephone'].value
    except:
        pass
    try:
        advisor = b['?advisor'].value
    except:
        pass
    c.execute(insert_students.format(sid, name, email, telephone, advisor))
    connection.commit()

for b in g.query(under_students).bindings:
    sid, name, email, telephone, advisor = '', '', '', '', ''
    try:
        sid = b['?sid'].lower()
    except:
        pass
    try:
        name = b['?name'].value
    except:
        pass
    try:
        email = b['?email'].value
    except:
        pass
    try:
        telephone = b['?telephone'].value
    except:
        pass
    try:
        advisor = b['?advisor'].value
    except:
        pass
    c.execute(insert_students.format(sid, name, email, telephone, advisor))
    connection.commit()
