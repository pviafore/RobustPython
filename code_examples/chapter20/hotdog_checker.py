import astroid

from pylint.checkers import BaseChecker
from pylint.interfaces import IAstroidChecker

class ServableHotDogChecker(BaseChecker):
    __implements__ = IAstroidChecker

    name = 'unverified-ready-to-serve-hotdog'
    priority = -1
    msgs = {
        'W0001': (
            'ReadyToServeHotDog created outside of hotdog.prepare_for_serving.',
            'unverified-ready-to-serve-hotdog',
            'Only create a PreparedHotDog through hotdog.prepare_for_serving.'
        ),
    }

    def __init__(self, linter=None):
        super(ServableHotDogChecker, self).__init__(linter)
        self._is_in_prepare_for_serving = False

    def visit_functiondef(self, node):
        if (node.name == "prepare_for_serving" and
            node.parent.name =="hotdog" and
            isinstance(node.parent, astroid.scoped_nodes.Module)):
            self._is_in_prepare_for_serving = True

    def leave_functiondef(self, node):
        self._is_in_prepare_for_serving = False

    def visit_call(self, node):
        if node.func.name != 'ReadyToServeHotDog':
            return

        if self._is_in_prepare_for_serving: 
            return

        self.add_message(
            'unverified-ready-to-serve-hotdog', node=node,
        )

def register(linter):
    linter.register_checker(ServableHotDogChecker(linter))
