# twitter
Sample twitter program to demonstrate the twitter API.  
Use it as a guide for your programming assignment: writing a twitter sentiment analysis program

You will create a Python program named *sentiment.py*.  The program will

1. Prompt the user to enter two search terms.  
2. Search the twitter stream for the first 1000 tweets that contain the first search term.  
3. Calculate a sentiment score for the first search term  
4. Search the twitter stream for the first 1000 tweets that contain the second search term.   
5. Calculate a sentiment score for the second search term.  
6. Determine which search term currently has the most positive sentiment on twitter and print the results.   

To search the twitter stream you will have to get OAuth authentication credentials to use in your program.
The steps are outlined in the Day 12 class notes.  

For the Sentiment Analysis project, we will use the industry standard practice of 
* Creating a branch of the master 
* Developing code in the branch
* Committing and pushing changes to the branch in github
* Issuing a Pull request
* Merging the pull request with the master branch
* Removing the branch that we used for developing the code     

Here are more detailed instructions:

Use *pip* to install the libraries in the *"requirements.txt"* file.  
      
Edit the *sentiment.py* file by editing the documentation comments at the top and editing the lines:

CONSUMER_KEY = 'xxxxxxxxxxxxxxxxxxxxxxxxxxx'   
CONSUMER_SECRET = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxx'   
ACCESS_TOKEN = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'   
ACCESS_TOKEN_SECRET = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'   

by replacing the "XXX" strings with the values you got from the twitter development site.

Use flake8 to check the style compliance of the program by typing

> flake8 sentiment.py

run the example program by typing

> python sentiment.py

Then type the following commands to:  
            
* Update the index using the current content found in the working directory and prepare the content staged for the next commit.
* Store the current contents of the index in a new commit along with a log message from the user describing the changes.
* Upload the changed files to the repository

> git add sentiment.py    
> git commit -m "adds new file sentiment.py"    
> git push origin mybranch    

Go to the github page for your *"mybranch"* branch and issue a pull request by clicking the 'New pull request' button.

Select your repo, and *not the class repo*, as the 'base repository' and click the green "Create Pull request' button.

Click the green "Merge Pull Request" button and then click the green "Confirm Merge" button

Create a Jenkins job named *"sentiment-yourusername"* where "yourusername" is your Chapman username

Configure the Jenkins job to run flake8 on your sentiment.py program and to run the program with input from the sentiment.input file. 

Your build commands should be:

flake8 sentiment.py
python3 sentiment.py < sentiment.input

Replace this README.md file with one  that describes your project (and not the assignment) and contains all the standard fields that you have seen in the README.md file from the email project.

Continue editing your program to meet the requirements specification and repeat these steps to push your code to your branch on github, issue pull requests to merge your code with the master branch, and accpet youe own pull requests to merge your code.  

When your program runs, is documented properly, and Jenkins does not report any errors or warnings, post the URL for your GitHub repo to Canvas

Delete the branch that you used for development by typing   

> git branch -d mybranch

