"""
Your goal is to write an Event constructor function, which can be used to make event objects.

An event object should work like this:

it has a .subscribe() method, which takes a function and stores it as its handler
it has an .unsubscribe() method, which takes a function and removes it from its handlers
it has an .emit() method, which takes an arbitrary number of arguments and calls all the stored functions with these arguments
As this is an elementary example of events, there are some simplifications:

all functions are called with correct arguments (e.g. only functions will be passed to unsubscribe)
you should not worry about the order of handlers' execution
the handlers will not attempt to modify an event object (e.g. add or remove handlers)
the context of handlers' execution is not important
each handler will be subscribed at most once at any given moment of time. It can still be unsubscribed and then subscribed again
Also see an example test fixture for suggested usage
"""
"""
# Tests
event = Event()

class Testf():
    def __init__(self):
        self.calls=0
        self.args=[]
    def __call__(self,*args):
        self.calls+=1
        self.args+=args

f=Testf()

event.subscribe(f)
event.emit(1, 'foo', True)

Test.assert_equals(f.calls, 1) #calls a handler
Test.assert_equals(f.args, [1, 'foo', True]) #passes arguments

event.unsubscribe(f)
event.emit(2)

Test.assert_equals(f.calls, 1) #no second call
"""


class Event():
    def __init__(self):
        self.func = set()

    def subscribe(self, func):
        self.func.add(func)

    def unsubscribe(self, func):
        self.func.discard(func)

    def emit(self, *args):
        for i in self.func:
            i(*args)
    #your code here
