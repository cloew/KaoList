from distutils.core import setup

setup(name='kao_list',
      version='0.1.0',
      description="List Wrapper class that provides extra convenience methods such as first and last",
      author='Chris Loew',
      author_email='cloew123@gmail.com',
      py_modules =['kao_list'],
      install_requires = ['smart_defaults',
                          'kao_decorators']
     )