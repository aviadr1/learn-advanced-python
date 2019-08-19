def make_singleton(class_):
    def __new__(cls, *args, **kwargs):
        raise Exception('class', cls.__name__, 'is a singleton')
        
    class_.__new__ = __new__
