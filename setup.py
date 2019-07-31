from setuptools import setup

setup(
   name='growcontroller',
   version='0.1',
   author='lump',
   packages=['growcontroller'],
   install_requires=['kivy', 'RPi.GPIO'],
   tests_require=['pytest', 'pytest-runner', 'fake-rpi'],
   entry_points={
        'console_scripts': [
            'growcontroller = growcontroller:main'
        ]
    }
)
