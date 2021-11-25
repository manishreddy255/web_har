Now we will see how to use github to manage our code and create  versions 
it and work on it easily 

even if you are remote you can use git to get access to your code and
make changes to it

first command if you want a code from a github repo
then  

git clone url

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

Now we will see how pull works and a scenario for it
if there is someone who made a change in the code in the repository 
and you want to get those changes to your local machine
  then you'll use 
  to get all the changes to the local repo so that you can work with that updated thing
  
  git pull 

it'll just get whatever is updated in the repo and sets it in the local machine


* Another thing is when you and your co-worker are working on a project and both did the changes to the same code and same line
then we have merge conflicts

then it will give to a conflict eroor and you can try to fix it

as git operates on adding lines and deleting line
when you chnage something in the same line then a conflict arises
when you pull the conflict then it will show something like this
  
<<<<<<< HEAD
    <h1>welcome home my boy !!</h1>
=======
    <h1 style="color: white">welcome home my boy !</h1>
>>>>>>> ad84adf89a0ad6328298453dc84c9eda4512258b


and it will show like this 
then what you need to do is
just change in however way you want of the code and then push it to the repo


Other commands which are useful are 

git log

to see what ever you have done in the repository

Now if you want to revert it back to old state old commit you can use

git reset --hard <commit> 
(it's the commit # you'll get in git log) 
to get back to commit which you want

if you want to reset back to the file that is online you can use

git reset --hard origin/main
(your code will be resetted)

with this you will get back to previous commit


Now we will see branching

consider a scenario where you're working on the code and added a new feature and then you're doing some changes witht he new feature tooo
but you goot to know that there is a bug in the code which was before adding feature

so now you need to work on the bug but not disturbing this feature
This is where branching comes in

instead of working on a new feature int eh main code
create a branch and work on it in the branch 
even if there is a bug in the main branch you can solve it
and after that you can develop your new feature 
then when you're satisfied with both of these you can merge both the branches to one

git branch -> it will show you  what branch you're in

now if you want to create a new branch and work on it

git checkout -b style( in place of style you can place any thing you want)

and if you wanna merge both

then return to main branch by
git checkout main

then 

git merge style(style is branch name)

then you'll have a merged file


Now forking if you want to get any open source project and want to contribute to it
just do a fork and then it'll get into your repo
then when you did a major change you can make a pull req 
if satisfactory they'll accept

