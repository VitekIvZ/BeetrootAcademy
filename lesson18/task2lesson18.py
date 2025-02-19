#task2lesson18.py


"""
  Implement 2 classes, the first one is the Boss and the second one is the Worker.

Worker has a property 'boss', and its value must be an instance of Boss.

You can reassign this value, but you should check whether the new value is Boss. 
Each Boss has a list of his own workers. You should implement a method that allows you to add workers 
to a Boss. You're not allowed to add instances of Boss class to workers list directly via access to 
attribute, use getters and setters instead!

You can refactor the existing code.

'''

id_ - is just a random unique integer

 

class Boss:

    def __init__(self, id_: int, name: str, company: str):

        self.id = id_

        self.name = name

        self.company = company

        self.workers = []

 

class Worker:

    def __init__(self, id_: int, name: str, company: str, boss: Boss):

        self.id = id_

        self.name = name

        self.company = company

        self.boss = boss

'''  
"""


class Boss:
    def __init__(self, id_: int, name: str, company: str):
        self.id = id_
        self.name = name
        self.company = company
        self._workers = []

    @property
    def workers(self):
        return self._workers

    def add_worker(self, worker):
        if isinstance(worker, Worker):
            self._workers.append(worker)
        else:
            raise ValueError("Only instances of Worker can be added.")


class Worker:
    def __init__(self, id_: int, name: str, company: str, boss: Boss):
        self.id = id_
        self.name = name
        self.company = company
        self._boss = None
        self.boss = boss  

    @property
    def boss(self):
        return self._boss

    @boss.setter
    def boss(self, new_boss):
        if isinstance(new_boss, Boss):
            if self._boss is not None:
                self._boss.workers.remove(self)
            self._boss = new_boss
            new_boss.add_worker(self)
        else:
            raise ValueError("Boss must be an instance of Boss class.")


if __name__ == "__main__":
    boss1 = Boss(1, "John Doe", "TechCorp")
    boss2 = Boss(2, "Jane Smith", "InnovateInc")

    worker1 = Worker(1, "Alice", "TechCorp", boss1)
    worker2 = Worker(2, "Bob", "TechCorp", boss1)

    print(boss1.workers)  
    print(worker1.boss.name)  

    worker1.boss = boss2  
    print(boss1.workers)  
    print(boss2.workers)  
    print(worker1.boss.name)  
