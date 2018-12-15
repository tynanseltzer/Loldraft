# lolDraft
Program to assist pro teams in Lol drafting


# Things to do:
Game tree: This should be pretty standard stuff, and has been done before 
(famous last words).

Evaluation function: This is the hard part. I think, given how few games are 
played at the pro level, we're gonna have to do some tricks to get the convergence
to happen in any ML method for some function. 

We ask a team to label the following:
For each roll, all champions playable in that roll, and say a number 0-100 which
is power for that roll

The same for whomever they are playing

And then perhaps a table to represent lane matchups or otherwise  relations 
between two champions. 

And then, from this we get some basic evaluation function, which we then suggest
teams for the human to label, and use those new training examples to make the
function better. 


Features later added:
Be able to switch between teams without losing all of the previous data

patch updates

Champion reworks.