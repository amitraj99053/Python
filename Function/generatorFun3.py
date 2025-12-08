# You can manually iterate through a generator using the next() function

def simple_gen():
    yield 'Amit'
    yield 'Sachin'
    yield 'Rohit'
    
gen = simple_gen()
print(next(gen))
print(next(gen))
print(next(gen))