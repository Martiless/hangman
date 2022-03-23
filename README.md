# Hangman 

This website has been created as the thrid Milestone project for Code Institute's Full Stack Software Development Diploma. It was built using Python. GitPod was used for writing the code for this website, as well as committing and pushing to GitHub. Once all the code had been written, Heroku was then used to deploy the website. 


### View the live website [here]()
***



## Table of content: 
 1. [Site Goals](#Site-Goals)
 1. [How to play](#How-to-play)
 1. [Features](#Features)
 1. [Testing](#Testing)
 1. [Bugs](#Bugs)
 1. [Unfixed Bugs](#Unfixed-bugs)
 1. [Technologies Used](#Technologies-Used)
 1. [Deployment](#Deployment)
 1. [Credits](#Credits)
      1. [Code](#Code)
***
  

## Site Goals:

The goals for this site are as follows:
* 

[Please see the live site here]()

*** 

## How to play:

***

## Features:

***

## Bugs:
1. Pick word function was not working correctly:
      * When importing the list of words to the run.py file I had incorrectly written the line of code that imports the data. import and from where in the wrong places. Once I corrected this error the pick_word function worked as intended. 
1. Welcome message was instantly dissapearing when the game was run:
      * Add a new function that allowed the used to interact more with the game, which inturn keeps the rules on the screen until they are ready to play. 
1.  Clear screen function was not working:
      * As this was a new concept to me I was unsure of what the correct paramaters should be. I troubleshooted and found a solution that allows the program to check what os is being used. 
1. Getting the correct letters to add to the answer_area:
      * I added a line of code into the start game function that included the .join() method. This did work to add the correctly guessed letter to the answer area but it also created more problems as stated below.  
1. The guessed letters could be guessed over and over again:
      * 
1. The correct letter would go into the answer_area servel times:
      * 

## Unfixed Bugs: 
1. 
***
[Back to top](#Hangman) 

## Technologies Used:
For this project, the following technologies were used.  

### Languages:
* Python

### Frameworks, Libraries, Programs & Applications Used:

#### GitPod
* GitPod was used for writing all the code for this project. It was also used to commit and push to GitHub.  

#### GitHub 
* GitHub was used to store this project.

*** 
[Back to top](#Hangman)



***
## Deployment:
This project was developed using [GitPod](https://gitpod.io/), committed and pushed to [GitHub](https://github.com/) using a GitPod terminal.

Deploying on Heroku
To deploy this page to Heroku from its GitHub repository, the following steps were taken:

1. 

***
## Credits:

### Acknowledgements:

1. I would like to start by thanking Brian O’Hare for being my mentor for this project. 

### Code:

1. 

*** 
[Back to top](#Hangman) 