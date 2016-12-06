# This file mainly exists to allow python setup.py test to work.
import os
import sys
import django
from django.db import connection
from django.test.utils import get_runner
from django.conf import settings

# Insert our ool package path, so that our test Django app can utilize it.
ool_dir = os.environ.get('OOL_DIR')
if ool_dir is None:
    ool_dir = os.path.abspath(os.path.join(
        os.path.dirname(__file__),
        '../'
    ))
sys.path.insert(0, ool_dir)


def runtests():
    django.setup()
    db_name = connection.creation.create_test_db()
    TestRunner = get_runner(settings)
    test_runner = TestRunner()
    try:
        failures = test_runner.run_tests(
            ['tests.tests.tests'], verbosity=1, interactive=True
        )
    finally:
        connection.creation.destroy_test_db(db_name)
    sys.exit(failures)

if __name__ == '__main__':
    runtests()
