from rdflib import Graph

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

insert_students = """
insert into students values ({}, {}, {}, {}, {})
"""
for b in g.query(grad_students).bindings:
    print(insert_students.format(b['?sid'], b['?name'], b['?email'], b['telephone'], b['advisor'])
