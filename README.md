# washington_football

I love Washington DC Football but the team is complete trash. As such, I'm using this garbage repository for testing Python delivery things. This way I'm not fiddling with important repositories and I can learn what happens when pushing various things to master.

![](docs/images/this-team-makes-me-drink.jpg)


#### Build badges for another project - just trying this

[![TravisCI Build Status](https://travis-ci.org/kmcquade/washington_football.svg?branch=master)](https://travis-ci.org/kmcquade/washington_football/)


## Installation

* Homebrew:

```bash
brew tap kmcquade/washington_football https://github.com/kmcquade/washington_football
brew install washington_football
```

* pip3

```bash
pip3 install washington_football
```


## Other

### Updating Homebrew formula

* Run this from the main directory:

```bash
./utils/update-brew.sh
```

It will update the `HomebrewFormula/washington_football.rb`.

Note:
* As of right now, it will just create that formula based on what is already in PyPi. I.e., the package dependencies and what it downloads will only match what is in PyPi, not what is currently in Git. I'll need to allow TravisCI to update Git master to ensure the Homebrew formula matches the most current version of PyPi.
* It's interesting that Homebrew pretty much just points to a git repository - by default, GitHub.
* `brew tap`, by default, would look for a repository titled `homebrew-washington_football`. To avoid needing this, we supply the Git repository after the brew tap command. Because the repository has a folder titled `HomebrewFormula`, it will install the formula from there.


### Creating a blank branch for stashing release artifacts

https://stackoverflow.com/a/34100189/17544707

First, create an empty branch with no history:

```bash
# Create an empty branch with no history
git switch --orphan artifacts
git commit --allow-empty -m "Initial commit on orphan branch"
git push -u origin artifacts
```

Then you can push all subsequent commits to that branch.

```bash
# Build the artifact
# Pipenv
pipenv install
pipenv shell
pipenv run python setup.py sdist bdist_wheel

# requirements.txt
python3 -m venv ./venv && source venv/bin/activate
python3 -m pip install -r requirements.txt
python3 -m pip install --upgrade setuptools wheel
python3 -m setup -q sdist bdist_wheel

git checkout artifacts
old_tar_file=$(ls *.tar.gz)
old_wheel_file=$(ls *.whl)
rm -f $old_tar_file
rm -f $old_wheel_file
cp dist/* ./

# Get the latest version
prefix=washington_football-
suffix=.tar.gz
version=$(ls *tar.gz | sed -e "s/^$prefix//" -e "s/$suffix$//")

git add *.tar.gz *.whl
git commit -m "Publish version ${version}"  *.tar.gz *.whl || echo "No changes to commit"
git push origin artifacts
```

