import os
import shutil


class Directory:
    """ Manage directory """

    def __init__(self, *args, init=True):
        """ Define main directory """
        if args[0] == "working_dir":
            self.directory = os.getcwd()
        else:
            self.directory = args[0]

        # In case of sub directory
        if len(args) == 2:
            self.directory = self.path(args[1])

        # If needed initialization, directory removed before create it
        if init:
            self.create_dir(self.directory, do_remove=True)

    def create_dir(self, directory, do_remove=False):
        """ Remove / (re)create main directory. """
        if do_remove:
            shutil.rmtree(directory, ignore_errors=True, onerror=None)
        os.makedirs(directory, exist_ok=True)

    def path(self, *args):
        """ Give absolute path of the children """
        return os.path.join(self.directory, *args)

    def listdir(self):
        return os.listdir(self.directory)
