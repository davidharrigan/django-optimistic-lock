TESTS=tests
SETTINGS=tests.tests.sqlite_settings
COVERAGE=coverage


test:
	DJANGO_SETTINGS_MODULE=${SETTINGS} python setup.py test

coverage:
	DJANGO_SETTINGS_MODULE=${SETTINGS} ${COVERAGE} run --source="./ool" setup.py test
	${COVERAGE} report

.PHONY: test

clean:
	rm -rf dist build *.egg-info .eggs/;
