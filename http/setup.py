from distutils.core import setup
import py2exe

setup(console=[r'main.py'],
      options={
          'py2exe': {
              'packages': ["googlemaps", "queuelib"]
          }
      })
