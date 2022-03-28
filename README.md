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
      * I rearranged the if statement in the start game function. Instead of the correct answer being checked first and the user getting a notice to say it was in the work, I changed it so the program checked if the letter had been picked already first, then if it wasn't in the word and then if it was. This solved the issue of being about to guess a correct letter over and over again.
1. The correct letter would go into the answer_area servel times:
      * Once I had figured out that I needed to use .join() to add the correct letters to the answer area, I began to encounter another problem, that being the letter would appear several times in the answer area. I decided to use a debugger and see if I could locate the issue. I had put the wrong variable into the .join() method, which I did not pick up on at first glance.
1. Colors not working:
      * I initially tried to use "from colorama import Fore, Back, Style" this working in the github enviroment but when I looked at it in Hekoku it was throwing up an error. I solved this by creating a class called Colors in a seperate python file and then imported that classes into the main game file. This soloved the problem and the colors worked correctly in Heruko. 


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

### Heroku 
* Heroku was used to delpoy the project. Please see below for deployment method. 

*** 
[Back to top](#Hangman)



***
## Deployment:
This project was developed using [GitPod](https://gitpod.io/), committed and pushed to [GitHub](https://github.com/) using a GitPod terminal.

Deploying on Heroku
To deploy this page to [Heroku](https://id.heroku.com/login) from its GitHub repository, the following steps were taken:

1. Create a new app in Heroku.
1. Select "New" and "Create new app".
1. Name the new app and click "Create new app".
1. Click on the "Settings" tab at the top of the page
1. Open the "Reveal Config Vars" section and input the following information -  KEY: PORT, VALUE: 8000. 
      * Nothing else is needed here for this project
1. Under the Config Vars section in "Settings" select "BuildPack" and select Python and Nodejs, 
      * Making sure they are in this order.
1. Now go to the "Deploy" tab at the top of the page and select your deploy method and repository.
1. In "Delpoyment Method" click on "GitHub" to connect them. 
1. Once they are connected search for the repository you want and hit "connect".
1. Either choose "Enable Automatic Deploys" or "Deploy Branch" in the manual deploy section. 
      * *Note, if you click on Automatic Deploys, you will still need to hit deploy branch to build the site* 
1. Heroku will now deploy the site.

***
## Credits:

### Acknowledgements:

1. I would like to start by thanking Brian O’Hare for being my mentor for this project. 

### Code:

1. The clear console function was taken from [www.delfstack.com](https://www.delftstack.com/howto/python/python-clear-console/)
1. I used various coder forums at times when I had difficulty with aspects of the code. The use of sites such as [Geeks for Geeks](https://www.geeksforgeeks.org/) and [Stack Overflow](https://stackoverflow.com/) was hugely helpful.
1. I also used [YouTube](https://www.youtube.com/) vidoes from [CBT Nuggets](https://www.youtube.com/watch?v=JNXmCOumNw0&t=782s) for the hangman game and [Scratch Tutorials](https://www.youtube.com/watch?v=u4QmAIoo4i0&t=81s) for the colors, *(however I did not go ahead with this method of using colors.)*
*** 
[Back to top](#Hangman) 