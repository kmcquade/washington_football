#! /bin/env python3
import logging
import sys
import os
from invoke import task, Collection, UnexpectedExit, Failure
# from washington_football.command.suck import suck

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), os.path.pardir + "/washington_football/")
    )
)

logger = logging.getLogger(__name__)

# Create the necessary collections (namespaces)
ns = Collection()
test = Collection('test')
ns.add_collection(test)

build = Collection('build')
ns.add_collection(build)

unit = Collection('unit')
ns.add_collection(unit)

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
def version_check(c):
    """Print the version"""
    try:
        c.run('./washington_football/bin/washington_football --version', pty=True)
    except UnexpectedExit as u_e:
        logger.critical(f"FAIL! UnexpectedExit: {u_e}")
        sys.exit(1)
    except Failure as f_e:
        logger.critical(f"FAIL: Failure: {f_e}")
        sys.exit(1)


@task
def run_nosetests(c):
    c.run('nosetests -v')


@task
def run_pytest(c):
    """Unit testing: Runs unit tests using `pytest`"""
    c.run('echo "Running Unit tests"')
    try:
        c.run('python -m coverage run -m pytest -v')
        c.run('python -m coverage report -m')
    except UnexpectedExit as u_e:
        logger.critical(f"FAIL! UnexpectedExit: {u_e}")
        sys.exit(1)
    except Failure as f_e:
        logger.critical(f"FAIL: Failure: {f_e}")
        sys.exit(1)


build.add_task(build_package, 'build-package')
build.add_task(install_package, 'install-package')

test.add_task(security_scan, 'security')
test.add_task(run_linter, 'lint')

unit.add_task(run_nosetests, 'nose')
unit.add_task(run_pytest, 'pytest')

integration.add_task(version_check, "version")
