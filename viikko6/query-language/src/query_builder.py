from matchers import And, HasAtLeast, Or, HasFewerThan, PlaysIn, All, Not

class QueryBuilder:
    def __init__(self, query = All()):
        self.query = query

    def build(self):
        return self.query

    def playsIn(self, team):
        return QueryBuilder(And(self.query, PlaysIn(team)))

    def hasAtLeast(self, value, attr):
        return QueryBuilder(And(self.query, HasAtLeast(value, attr)))
    
    def hasFewerThan(self, value, attr):
        return QueryBuilder(And(self.query, HasFewerThan(value, attr)))
    
    def oneOf(self, query1, query2):
        return QueryBuilder(Or(query1, query2))
