try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'name':'it-ebook-dl',
    'version':'0.0.3',
    'py_modules':['get_pdfs'],
    'install_requires':[
         'mechanize==0.2.5',
         'twill==0.9',
    ],
    'entry_points':{
        'console_scripts':
            ['find-pdfs = get_pdfs:main']
    },
}

setup(**config)
