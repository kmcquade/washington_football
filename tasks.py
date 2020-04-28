#! /bin/env python3

from invoke import task, Collection
# from washington_football.command.suck import suck

# Create the necessary collections (namespaces)
ns = Collection()
test = Collection('test')
ns.add_collection(test)

build = Collection('build')
ns.add_collection(build)

integration = Collection('integration')
ns.add_collection(integration)


# BUILD
@task
def build_package(c):
    """Build the policy_sentry package from the current directory contents for use with PyPi"""
    c.run('python -m pip install --upgrade setuptools wheel')
    c.run('python setup.py -q sdist bdist_wheel')


@task(pre=[build_package])
def install_package(c):
    """Install the policy_sentry package built from the current directory contents (not PyPi)"""
    c.run('pip3 install -q dist/washington_football-*.tar.gz')


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


build.add_task(build_package, 'build-package')
build.add_task(install_package, 'install-package')

test.add_task(security_scan, 'security')
test.add_task(run_linter, 'lint')
test.add_task(run_tests, 'unit')
