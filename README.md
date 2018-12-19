# lolDraft
Program to assist pro teams in Lol drafting

# Dependencies:
This requires some standard libraries, including numpy, pandas, and scikit-learn.
We also required xgboost, which can be installed with pip install xgboost.

Finally, we require the author's version of an MCTS library, found at 
https://github.com/tynanseltzer/mcts. This cannot be installed with pip, so you 
must download the zipfile of the repo from Github, unzip it, and then from 
within the unzipped directory, running 'python setup.py install'

# Usage
To use, run either mctsPlay.py, or minimaxPlay.py. You will be asked to choose
your heuristic, and other parameters, and what team(s) the AI should play.




