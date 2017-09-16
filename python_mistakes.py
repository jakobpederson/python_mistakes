from random import randint, choice


class thing():
    def has_condition_one(self):
        x = randint(1, 9)
        if x % 2 == 0:
            return True
        return False
    
    def has_condition_two(self):
        x = randint(1, 9)
        if x % 2 == 0:
            return True
        return False
    
    def has_condition_three(self):
        x = randint(1, 9)
        if x % 2 == 0:
            return True
        return False
        
    def has_conditions(self):
        x = randint(1, 9)
        if x % 2 == 0:
            return 'condition3'
        return 'condition4'
        
    def has_condition_forty_two(self):
        x = randint(1, 9)
        if x % 2 == 0:
            return True
        return False
    
    def which_one(self):
        return choice([
            'condition1',
            'condition2',
            'condition3',
            'condition4',
            'condition5',
        ])

def do_awesome_stuff(thing):
    if thing.has_condition_one():
        print('condition one')
    elif thing.has_condition_two():
        print('condition two')
    elif thing.has_condition_three():
        print('condition three')
    elif thing.has_conditions() in ['condition3', 'condition4']:
        print('condition three or four')
    elif thing.has_condition_forty_two():
        print('condition forty two')
    else:
        print('else')

something = thing()
do_awesome_stuff(something)


def strategy1():
    x = randint(1, 9)
    if x % 2 == 0:
        print('condition one')
        return True
    return False

def strategy2():
    x = randint(1, 9)
    if x % 2 == 0:
        print('condition two')
        return True
    return False   

def strategy3():
    x = randint(1, 9)
    if x % 2 == 0:
        print('condition three')
        return True
    return False
    
def strategy4():
    x = randint(1, 9)
    if x % 2 == 0:
        print('condition three or four')
        return 'condition3'
    print('condition one')
    return 'condition4'

def strategy5():
    x = randint(1, 9)
    if x % 2 == 0:
        print('condition forty-two')
        return True
    return False   
    
strategies = {
    'condition1': strategy1,
    'condition2': strategy2,
    'condition3': strategy3,
    'condition4': strategy4,
    'condition5': strategy5,
}

def new_do_awesome_stuff(thing):
    which_one = thing.which_one()
    strategy = strategies[which_one]
    return strategy()

new_do_awesome_stuff(something)
