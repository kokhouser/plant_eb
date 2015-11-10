from setuptools import setup
 
setup(name='ACUArboretum',
      version='1.0',
      description='Website to display horticulture in ACU.',
      author='Houser Kok',
      author_email='hzk11a@acu.edu',
      url='',
     install_requires=['flask','flask-login','sqlalchemy','flask-sqlalchemy', 'flask-wtf', 'flask-openid', 'sqlalchemy-migrate'],
     )