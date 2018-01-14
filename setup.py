from setuptools import setup

setup(
    name='flaskblog',
    version='0.0.1',
    packages=['flaskblog'],
    description='personal blog_bp developed with Flask and SQlite3',
    include_package_data=True,
    install_requires=[
        'flask',
        'psycopg2',
        'flask-sqlalchemy'
    ],
    setup_requires=[
        'pytest-runner',
    ],
    tests_require=[
        'pytest',
    ],
)
