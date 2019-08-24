# - [Instructor] Hi, and welcome back.

# In this video, we're going to create

# our first flask application.

# Flask applications are built around requests and responses.

# Now, we're going to look very in detail

# at what requests and responses are

# and how the web works in the next couple of videos.

# But I want to give you a quick introduction (pause) now.

# Apologies for that.

# A request is what your browser does.

# So, for example, safari,

# or google chrome, or internet explorer.

# Whenever you go to a website, you're making a request.

# And there is a computer somewhere on the internet

# that is receiving that request.

# And that computer has something

# like a flask application in it.

# So that flask application receives that request

# from your browser, and then decides what to do with it,

# and then returns back a response.

# For example, one request may be

# to ask for a certain page's home page.

# Another request may be to ask

# for something called hello.html for an html file.

# Another request may be to ask

# for user number three, for example.

# So requests can be really anything.

# But the server, the flask application,

# has to be created to be able to understand those requests.

# So that's the key here.

# In order to start with our flask application,

# the first thing we have to do

# is to tell python that we want to use flask.

# That kind of makes sense.

# So the first thing to do is to say from flask, lowercase f,

# import Flask, with an uppercase F.

# Also let's use this opportunity to save this as app.py.

# Once again, you can call this whatever you want,

# but normally flask applications are called app.py.

# And we will look at why in a few video's time, really.

# Now that we've imported flask,

# we've imported something called Flask with a capital F

# from a package called flask with a lowercase f.

# You may not have noticed, but classes in python,

# such as our student and our working student classes

# from last section, classes always start with a capital F.

# And packages always start with a lowercase f,

# although we've not really seen this in practise.

# We can therefore safely assume that Flask

# with a capital F is a class.

# And indeed it is.

# So the first thing we want to do

# is create an app from that Flask class.

# So we're going to say app equals flask.

# And here comes something a bit newer,

# which is underscore underscore name, underscore underscore.

# So that's two underscores in front and two behind.

# And the underscore underscore name, underscore underscore

# is a special python variable.

# It essentially gives each file a unique name.

# And that's really all that we have to worry about.

# So when we start the Flask application,

# in order for Flask to know that this application

# is running in a specific unique place,

# we tell it this underscore underscore name

# underscore underscore.

# Don't worry much about it.

# Then, the first thing we have to say

# is to tell our app what requests it's going to understand.

# Remember, earlier I said that sometimes

# you may request the homepage of an application.

# Other times you may request something like a hello.html.

# Other times you may request the third user,

# or things like that.

# So we have to tell our app exactly

# what request it will understand.

# And it can understand many requests, of course,

# but we're going to start with just one.

# In order to do that, we're going to use a decorator.

# So now we know what those are.

# It's going to say @app.route and here is going to go

# the route or the endpoint or the request

# that it is going to understand.

# In our case, it is going to be a forward slash

# within a string.

# And what this means is,

# for example, http://www.google.com/.

# So when you access a webpage such as google.com,

# really what you're accessing is google.com/.

# And the forward slash there just means

# this is the homepage of the site.

# You can also do things like google.com/maps, I think.

# And this would be a separate route.

# You can do google.com/plus, I think.

# I'm not really familiar with google's end points.

# But this would be a separate end point, slash plus.

# Because they are supposed to do different things

# in a server.

# So if you leave it just as a forward slash,

# that is the home page of the application.

# And as we know, a decorator always has to act on a method,

# so what's going to come after is going to be a method.

# In this case I'm calling the method home.

# But the name of the method in Flask does not matter,

# so you can call it whatever you want.

# All that matters is this route.

# So now we've got our home method,

# we can make it do things.

# And whatever it does,

# it has to return a response back to our browser

# so that our browser receives something back

# and it can show something on the website.

# So for example, we're going to return "Hello, world!".

# So what's going to happen now

# is that when we access our end point with our browser,

# what we should see is "Hello, world!" coming back.

# And then we also, of course, have to tell the app

# to start running.

# So let's do that, app.run.

# And here we can tell it a specific port.

# A port is just a sort of area of the computer

# where your app is going to be receiving your requests

# and returning your responses through.

# Computers have many of these areas,

# and in my case I'm going to use port 5000.

# If you do receive an error when you run the app,

# saying address already in use,

# that's because some other application in your computer

# is already using this port.

# So all you have to do is just change it

# for something else, like 4999, for example.

# Okay, once that's done, let's go into the terminal.

# I'm going to clear this.

# And making sure that you are in the correct folder,

# which in my case, I don't think I am,

# so I'm going to go in it,

# code, section three, video code.

# Making sure you're in the correct folder,

# then do python3.5 app.py.

# And what you should see is something like this.

# Running on and here is the interesting part,

# http://127.0.0.1:5000/,

# and the forward slash is important

# because that's the home page of our app.

# The 5000, as you can imagine,

# is the port that we've selected,

# and 127.0.0.1, for those of you who are

# experienced programmers, you'll know what that is,

# but for those of you that don't,

# that is your computer.

# So 127.0.0.1 is a special IP address

# that is reserved for your computer, specifically.

# So whenever you access this address in your browser,

# what you're accessing is your own computer.

# Because we're accessing using http,

# that means that our browser is able to access this page.

# So just copy that and go into chrome, for example.

# And then let's paste it in.

# And what we see is "Hello world!" coming back

# because that's what our end point returns.

# Notice how google chrome strips

# the trailing slash from the end.

# But that's always present there,

# and some other browsers will not remove it.

# So just because google chrome removes it,

# doesn't mean we're not accessing the home page.

# And that's our hello, world.

# And this was your first flask application.

# And you've managed to create an end point

# that returns some data.

# So going back to atom, all that we've done

# is imported Flask, created an object of Flask

# using a unique name, and then created a route,

# which was for the home page of our application,

# just the forward slash,

# assigned a method to it, which has to return something,

# and whatever it returns will go to the browser.

# And finally we've ran the app.

# Of course, these methods don't have

# to return strings only.

# That would be quite boring.

# But normally in rest API's they do return strings,

# and it is a Javascript application

# that deals with displaying things nicely.

# Flask can also display things nicely if we want,

# but that's not the purpose of this course.

# There is many, not many,

# but there are a couple other courses, one of them mine,

# that deals with creating web sites and web apps with Flask.

# This course is concerned with rest APIs.

# And rest APIs usually return text in a specific format.

# So we're going to be looking at more of that

# in the next coming sections.

# But in this section we are going to give you a bit

# of insight into how you might use a rest API

# from within a Javascript application.

# For those of you that are interested

# in using your API from within Javascript,

# that will be very useful.

# So the next couple of videos are going to be

# more about how the web works,

# how rest works, and things like that.

# And then we'll move on to creating

# the Javascript programme that will use this API

# just for your convenience.

# So hopefully all that's okay,

# and I'll see you in the very next video.

from flask import Flask
app = Flask(__name__)

# So we have to tell our app exactly

# what request it will understand.

# And it can understand many requests, of course,

# but we're going to start with just one.

# In order to do that, we're going to use a decorator.
@app.route("/")  # http://www.google.com/
def home():
    return "Hello, Flask!"


app.run(port=5000)
