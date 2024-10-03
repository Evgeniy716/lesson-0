from inspect import getmodule


def introspection_info(obj):
        return {
        "type": type(obj).__name__,
        "attributes": obj.__dict__,
        "methods": dir(obj),
        "module": getmodule(obj)
        }

class MyIntro:
        def __init__(self):
            self.name = "MyIntro"
            self.value = 100
            self.private_attribute = "private"


obj = MyIntro()


number_info = introspection_info(obj)
print(number_info)



