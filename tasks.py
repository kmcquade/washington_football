#! /bin/env python3

from invoke import task, Collection
from washington_football.command.suck import suck

# Create the necessary collections (namespaces)
ns = Collection()
test = Collection('test')
ns.add_collection(test)


@task()
def reminder():
    suck(True)


@task
def security_scan(c):
    c.run('bandit -r washington_football/')
    c.run('safety check')


@task
def run_linter(c):
    c.run('autopep8 -r --in-place washington_football/')
    c.run('pylint washington_football/')


@task
def run_tests(c):
    c.run('nosetests -v')


test.add_task(reminder, 'reminder')
test.add_task(security_scan, 'security')
test.add_task(run_linter, 'lint')
test.add_task(run_tests, 'unit')
