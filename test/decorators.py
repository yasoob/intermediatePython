import unittest,re
from functools import wraps
class TDD_DECORATORS(unittest.TestCase):
    def test_decorators(self):
        def hi(name="yasoob"):
            return "hi " + name
        self.assertEqual(hi(), 'hi yasoob')
        # We can even assign a function to a variable like
        greet = hi
        self.assertEqual(greet, hi)
        # We are not using parentheses here because we are not calling the function hi
        # instead we are just putting it into the greet variable. Let's try to run this
        self.assertEqual(greet(), 'hi yasoob')
        # output: 'hi yasoob'
        # Let's see what happens if we delete the old hi function!
        del hi
        self.assertRaises(NameError, lambda: hi())
        self.assertEqual(greet(), 'hi yasoob')
    def test_inline_function(self):
        def hi(name="yasoob"):
            l = []
            l.append("hi() function start")
            def greet():
                return "greet() function"
            def welcome():
                return "welcome() function"
            l.append(greet())
            l.append(welcome())
            l.append("hi() function end")
            return l
        self.assertEqual(' -> '.join(hi()),
                         'hi() function start -> greet() function -> welcome() function -> hi() function end'
                         )
        # This shows that whenever you call hi(), greet() and welcome()
        # are also called. However the greet() and welcome() functions
        # are not available outside the hi() function e.g:
        self.assertRaises(NameError, lambda: greet)
    def test_return_inline_function(self):
        def hi(name="yasoob"):
            def greet():
                return "now you are in the greet() function"
            def welcome():
                return "now you are in the welcome() function"
            if name == "yasoob":
                return greet
            else:
                return welcome
        a = hi()
        self.assertTrue(callable(a))
        # This clearly shows that `a` now points to the greet() function in hi()
        # Now try this
        self.assertEqual(a(), "now you are in the greet() function")
    def test_give_argument(self):
        def hi():
            return "hi yasoob!"
        def doSomethingBeforeHi(func):
            return ("I am doing some boring work before executing hi() ")+(func())
        self.assertEqual(doSomethingBeforeHi(
            hi), "I am doing some boring work before executing hi() hi yasoob!")
    def test_decorator(self):
        def a_new_decorator(a_func):
            def wrapTheFunction():
                l = []
                l.append("before executing a_func()")
                l.append(a_func())
                l.append("after executing a_func()")
                return l
            return wrapTheFunction
        def a_function_requiring_decoration():
            return ("needs some decoration")
        self.assertEqual(a_function_requiring_decoration(),
                         'needs some decoration')
        a_function_requiring_decoration1 = a_new_decorator(
            a_function_requiring_decoration)
        s = 'before executing a_func() -> needs some decoration -> after executing a_func()'
        self.assertEqual(' -> '.join(a_function_requiring_decoration1()), s)
        @a_new_decorator
        def a_function_requiring_decoration2():
            """Hey you! Decorate me!"""
            return("needs some decoration")
        self.assertEqual(' -> '.join(a_function_requiring_decoration2()),s)
        # the @a_new_decorator is just a short way of saying:
        a_function_requiring_decoration3 = a_new_decorator(a_function_requiring_decoration)
        self.assertEqual(' -> '.join(a_function_requiring_decoration3()), s)
        self.assertEqual(a_function_requiring_decoration.__name__,'a_function_requiring_decoration')
        self.assertEqual(a_function_requiring_decoration3.__name__, 'wrapTheFunction')
    def test_wraps(self):
        def a_new_decorator(a_func):
            @wraps(a_func)
            def wrapTheFunction():
                l = []
                l.append("before executing a_func()")
                l.append(a_func())
                l.append("after executing a_func()")
                return l
            return wrapTheFunction
        @a_new_decorator
        def a_function_requiring_decoration():
            """Hey yo! Decorate me!"""
            print("needs some decoration")
        self.assertEqual(a_function_requiring_decoration.__name__,'a_function_requiring_decoration')
    def test_outer_variable(self):
        def decorator_name(f):
            @wraps(f)
            def decorated(*args, **kwargs):
                if not can_run:
                    return "Function will not run"
                return f(*args, **kwargs)
            return decorated
        @decorator_name
        def func():
            return("Function is running")
        can_run = True
        self.assertEqual(func(),"Function is running")
        can_run = False
        self.assertEqual(func(),"Function will not run")
    def test_authorization(self):
        class request():
            class Auth():
                username=''
                password = ''
            authorization = Auth
        def authenticate():
            return 5
        def check_auth(name,pwd):
            return False
        def requires_auth(f):
            @wraps(f)
            def decorated(*args, **kwargs):
                auth = request.authorization
                n=0
                if not auth or not check_auth(auth.username, auth.password):
                    n=authenticate()
                return f(n=n,*args, **kwargs)
            return decorated
        d = requires_auth(lambda x, y,three,n: n+x + y+three)(1, 2,three=6)
        self.assertEqual(d, 5 + 1 + 2 + 6)
    def test_logging(self):
        def logit(func):
            @wraps(func)
            def with_logging(*args, **kwargs):
                self.assertEqual(func.__name__ , 'addition_func')
                return func(5,*args, **kwargs)
            return with_logging
        @logit
        def addition_func(x,y):
            """Do some math."""
            return x + y
        result = addition_func(4)
        self.assertEqual(result,4+5)
    def test_nesting_decorator(self):
        def logit(logfile='out.log'):
            def logging_decorator(func):
                @wraps(func)
                def wrapped_function(*args, **kwargs):
                    log_string = func.__name__ 
                    self.assertRegex(log_string,'myfunc1|myfunc2')
                    # Open the logfile and append
                    with open(logfile, 'a') as opened_file:
                        # Now we log to the specified logfile
                        opened_file.write(log_string + '\n')
                    return func(logfile,*args, **kwargs)
                return wrapped_function
            return logging_decorator

        @logit()
        def myfunc1(fileName):
            return fileName

        self.assertEqual(myfunc1(),'out.log')
        # Output: myfunc1 was called
        # A file called out.log now exists, with the above string

        @logit(logfile='func2.log')
        def myfunc2(fileName):
            return fileName

        self.assertEqual(myfunc2(),'func2.log')
    def test_decorator_classes(self):
        class logit(object):

            _logfile = 'out.log'

            def __init__(self, func):
                self.func = func

            def __call__(self, *args):
                log_string = self.func.__name__ + " was called"
                # Open the logfile and append
                with open(self._logfile, 'a') as opened_file:
                    # Now we log to the specified logfile
                    opened_file.write(log_string + '\n')
                # Now, send a notification
                self.notify()

                # return base func
                return self.func(log_string,*args)



            def notify(self):
                # logit only logs, no more
                pass
        logit._logfile = 'out2.log' # if change log file
        @logit
        def myfunc1(s):
            return s

        self.assertEqual(myfunc1(),'myfunc1 was called')
        class email_logit(logit):
            '''
            A logit implementation for sending emails to admins
            when the function is called.
            '''
            def __init__(self, email='admin@myproject.com', *args, **kwargs):
                self.email = email
                super(email_logit, self).__init__(*args, **kwargs)

            def notify(self):
                # Send an email to self.email
                # Will not be implemented here
                return self.email
        self.assertEqual(email_logit(func=lambda x:x).notify(),'admin@myproject.com')
if __name__ == '__main__':
    unittest.main()
