Now we will see how to use github to manage our code and create  versions 
it and work on it easily 

even if you are remote you can use git to get access to your code and
make changes to it

first command if you want a code from a github repo
then  

git clone <url> 
with this the whole repo is downloaded into our machine
so that you have a copy of that code 

Next command is

git add <what file> (. -> for all files)
it will take a snap shot and saves it

next is 
git commit -m "message" (what ever you can mention) -> better placing what you're changing

Even after commit the changes are not reflected online
there is another step you need to take to do it
with git commit and add one is only making changes to local repository

and for changes that needs to be reflected online you need to push em to repo

to check what status of your repo is you can use
git status

when you want to push changes to repo
git push (this will push changes to master branch)


