# -*- coding: utf-8 -*-
def coroutine(func):
    def inner(*args, **kwargs):
        g = func(*args, **kwargs)
        g.send(None)
        return g
    return inner


class CustomException(Exception):
    pass


@coroutine
def subgen():
    while True:
        try:
            message = yield
        except CustomException:
            print('Exception')
        else:
            print('...', message)


@coroutine
def delegator(g):
    while True:
        try:
            data = yield
            g.send(data)
        except CustomException as e:
            g.throw(e)
