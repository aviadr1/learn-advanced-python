class SuperObject:        
    def __init__(self, **kwargs):
        mro = type(self).__mro__
        assert mro[-1] is object
        if mro[-2] is not SuperObject:
            raise TypeError(
                'all top-level classes in this hierarchy must inherit from SuperObject',
                'the last class in the MRO should be SuperObject',
                f'mro={[cls.__name__ for cls in mro]}'
            )

        # super().__init__ is guaranteed to be object.__init__        
        init = super().__init__
        init()
        
    def super_call(self, super_, funcname, **kwargs):
        """
        cooperatively calls a function on super. 
        usage:
            self.super_call(super(), 'my_method_name', param1='example', param2='whatever')
        """
        super_func = getattr(super_, funcname, None)
        if super_func is not None:
            return super_func(**kwargs)
