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