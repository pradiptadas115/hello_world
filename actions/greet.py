import sys

from st2common.runners.base_action import Action


class PrintPythonHelloWorldAction(Action):
    def run(self):
        print("This is test python script of hello world")
        print('Using Python executable: %s' % (sys.executable))
        print('Using Python version: %s' % (sys.version))