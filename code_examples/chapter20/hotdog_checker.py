import astroid

from pylint.checkers import BaseChecker
from pylint.interfaces import IAstroidChecker

class PreparedHotDogChecker(BaseChecker):
    __implements__ = IAstroidChecker

    name = 'unverified-prepared-hotdog'
    priority = -1
    msgs = {
        'W0001': (
            'PreparedHotDog created outside of hotdog.create_hot_dog.',
            'unverified-prepared-hotdog',
            'Only create a PreparedHotDog through hotdog.create_hot_dog.'
        ),
    }

    def __init__(self, linter=None):
        super(PreparedHotDogChecker, self).__init__(linter)
        self._is_in_create_hot_dog = False

    def visit_functiondef(self, node):
        if (node.name == "create_hot_dog" and
            node.parent.name =="hotdog" and
            isinstance(node.parent, astroid.scoped_nodes.Module)):
            self._is_in_create_hot_dog = True

    def leave_functiondef(self, node):
        self._is_in_create_hot_dog = False

    def visit_call(self, node):
        if node.func.name != 'PreparedHotDog':
            return

        if self._is_in_create_hot_dog: 
            return

        self.add_message(
            'unverified-prepared-hotdog', node=node,
        )

def register(linter):
    linter.register_checker(PreparedHotDogChecker(linter))
