
class secret():
    def __init__(self, agent):
        self.agent = agent

    def spot(self):
        return "His secret name is Agent " + self.agent


class person():

    def __init__(self, name, last_name, age):
        self.name = name
        self.last_name = last_name
        self.age = age

class employee(person):

    def __init__(self, name, last_name, age, id, salary):
        self.id = id
        self.salary = salary
        person.__init__(self, name, last_name, age)

    def did(self):
        return self.id*2

    def dsalary(self):
        return self.salary*1000000000000000

class perf(employee, secret):
    def __init__(self, name, last_name, age, id, salary, perf, agent):
        self.perf = perf
        employee.__init__(self, name, last_name, age, id, salary)
        secret.__init__(self, agent)

    def review(self):
        return 'his performance was the ' + self.perf

joao = perf('joao', 'paulo', 36, 777, 95, 'Best', 'Jornada')
# print(joao.dsalary())
print(joao.name)
print(joao.last_name)
print(joao.did(), joao.spot(), joao.review())
# print(joao.salary)
# print(joao.perf)
# print(joao.review())
# print(joao.agent)
# print(joao.spot())
