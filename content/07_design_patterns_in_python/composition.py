class Composition:
    COMPOSITE = '_composite_'
    
    @staticmethod
    def __get_composed_attr(self, arg):
        split = arg.split('_')
        if len(split) < 2:
            return None

        action_name, component_name = split[0], Composition.COMPOSITE + split[1]
        if component_name in self.__dict__:
            # we are directly composed of this component
            component = getattr(self, component_name)
            action = getattr(component, action_name)
            return action
        else:
            # search for component in our components
            for attr_name in self.__dict__:
                if not attr_name.startswith(Composition.COMPOSITE):
                    continue

                attr = getattr(self, attr_name)
                # recursively try to get this action from our composed objects
                action = getattr(attr, arg, None)
                if action is None:
                    continue
                return action
    
    @staticmethod
    def get_composed_attr(self, arg, super_=None):
        result = Composition.__get_composed_attr(self, arg)
        if result is not None:
            return result
        elif super_ is not None:
            return getattr(super_, arg)
        

    @staticmethod
    def compose(self, obj, super_=None, as_name=None):
        if as_name is None:
            as_name = type(obj).__name__.lower()

        return setattr(self, Composition.COMPOSITE + as_name, obj)
         
