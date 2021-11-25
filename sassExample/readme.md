In this project i am using Sass which is a css preprocessor but to use it you have to generate a css file from that sass file
if you don't have sass installed into your system then install it using
npm i -g sass
then write command
sass variables.scss:variables.css
and mention the generated css file in the html you wanna use
You can't always compile the sass so you can automate it such that whenever there is a change in sass it will automatically convert the css
code for it is
sass --watch variables.scss:variables.css