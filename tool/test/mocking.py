#******************************************************************************
# Copyright (c) 2011 Pason Systems Corp.
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#
#******************************************************************************

import unittest

# A token used when mocking an attribute that didn't previously exist
_NO_SUCH_ATTR = object()

class InstrumentedMethod(object):
    """
    A method that has been instrumented to be queried after the body
    of the test is complete.

    The calledArgs attribute contains a list of call argument tuples
    of the form (args, kwargs).
    """

    def __init__(self, realMethod):
        """
        Create a new instrumented method.

        @param realMethod    the method we are instrumenting
        """
        self.realMethod = realMethod
        self.callArgs = []

    def __call__(self, *args, **kwargs):
        """
        Push the call arguments onto a call list and return the result
        of the real method.
        """
        self.callArgs.append((args, kwargs))
        return self.realMethod(*args, **kwargs)

    def _wasCalled(self):
        return bool(self.callArgs)
    called = property(_wasCalled, doc="True if the method was called")

    def calledWithArgs(self, args=[], kwargs={}, call_index=0):
        """
        Return true if the function was called with the given arguments.

        @param args   arguments
        @param kwargs keyword arguments
        `call_index` which call to check (e.g. -1 for last call)
        """
        return (self.called
                and self.callArgs[call_index][0] == tuple(args)
                and self.callArgs[call_index][1] == kwargs)

    def _getArgs(self):
        return self.callArgs[0][0]
    args = property(_getArgs)

    def _getKwArgs(self):
        return self.callArgs[0][1]
    kwargs = property(_getKwArgs)

class Mock(InstrumentedMethod):
    """
    A generic mock object. Any unset attribute got from this object will
    return a new mock object.
    """
    def __init__(self):
        def returnNone(*args, **kwargs):
            return None
        super(Mock, self).__init__(returnNone)

    def __getattribute__(self, attrName):
        try:
            attr = super(Mock, self).__getattribute__(attrName)
        except AttributeError:
            attr = Mock()
            setattr(self, attrName, attr)
        return attr

class Mockery(object):
    """
    An object that keeps track of mocks and stubbed. Calling unmockAll()
    will revert all changes made with mock(), stub(), or instrument().
    """

    def __init__(self):
        self._mocks = []

    def mock(self, context, attrName, newValue):
        """
        Mock the given attribute of the context object by replacing it with
        newValue.

        @param context      the object on which we will mock an attribute
        @param attrName     the name of the attribute to mock out
        @param newValue     the object to replace the mocked object with
        """
        self._mocks.append((context, attrName,
                            context.__dict__.get(attrName, _NO_SUCH_ATTR)))
        setattr(context, attrName, newValue)
        return newValue

    def instrument(self, context, attrName):
        """
        Mock out a method with an instrumented method wrapping it.
        """
        return self.mock(
            context, attrName,
            InstrumentedMethod(getattr(context, attrName)))

    def stub(self, context, attrName, returnVal=None, exception=None):
        """
        Replace a method with an instrumented method that raises the given
        exception or returns the given return value (default None).

        @param context    the object to stub
        @param attrName   the name of the attribute to stub
        @param returnVal  the return value of the stubbed method
        @param exception  the exception to raise (if None, do not raise an exception)
        """
        def stubMethod(*args, **kwargs):
            if (exception):
                raise exception
            return returnVal
        return self.mock(context, attrName, InstrumentedMethod(stubMethod))

    def unmockAll(self):
        """
        Undo all the mocks we set up.
        """
        while self._mocks:
            context, attrName, oldValue = self._mocks.pop()
            if (oldValue is _NO_SUCH_ATTR):
                try:
                    delattr(context, attrName)
                except:
                    # It is highly unlikely someone else will try to call
                    # a function/object that wasn't there before. Ignore
                    # the case when we can't delete the mocked thing.
                    pass
            else:
                setattr(context, attrName, oldValue)


class MockingTestMixin(object):
    """
    A mixin for unit tests that want mock, stub, and instrument methods.
    Don't forget to call setUp and tearDown.
    """

    def setUp(self):
        self._mockery = Mockery()

    def tearDown(self):
        self._mockery.unmockAll()

    def mock(self, context, attrName, newValue):
        return self._mockery.mock(context, attrName, newValue)

    def instrument(self, context, attrName):
        return self._mockery.instrument(context, attrName)

    def stub(self, context, attrName, returnVal=None, exception=None):
        return self._mockery.stub(context, attrName, returnVal, exception)

class BasicMockingTestCase(unittest.TestCase, MockingTestMixin):
    ''' A basic unittest class that allows mocking '''
    def setUp(self):
        unittest.TestCase.setUp(self)
        MockingTestMixin.setUp(self)
    def tearDown(self):
        MockingTestMixin.tearDown(self)
        unittest.TestCase.tearDown(self)

class ReturnList(object):
    """
    A callable object that returns elements from its return value list
    and throws an exception when the list is exhausted.
    """
    def __init__(self, *returnVals):
        """
        Create a new return list callable. Arguments to this constructor
        are put into the list of return values.
        """
        self.returnVals = list(returnVals)
    def __call__(self, *args, **kwargs):
        """
        Return the next value from the return list or raise Exception if
        the list is empty.
        """
        if (self.returnVals):
            return self.returnVals.pop(0)
        else:
            raise Exception("Return list exhausted.")
