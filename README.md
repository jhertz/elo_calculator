elo_calculator
==============

An ELO calculator that uses challonge brackets

Setting up:
elo_calculator is a very simple python script. All you should need installed are:
- A copy of python 2.7.X (https://www.python.org/download/releases/2.7.7/)
- The pychallonge library (https://github.com/russ-/pychallonge)

Once you've sucessfully installed those both, open a command prompt / terminal window and run:
python elo_calculator.py

That's it!

How To Use:

This program expects two files in the same directory as it runs out of:


-creds.txt: This file will contain your username and api_key to your challonge account.
    It should be in the following format:
    
    username
    api-key
    
Yup thats it, a plain text file with two seperate lines! Make sure there's a line break between the two!!!
    
-brackets.txt: This file will contain the names of the brackets you want to use. The format is also very simple. One bracket name per line. For instance, if you have two brackets, one at  http://challonge.com/Fox, and the other at http://challonge.com/Falco
    then brackets.txt should look like this:
    
    Fox
    Falco
    

Again, both of these should be plain text files, with each entry on a seperate line.
  
  
Super easy and simple! Now go make power-rankings without everyone whining!


