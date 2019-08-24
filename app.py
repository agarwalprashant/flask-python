# - [Instructor] Hi and welcome back to the course.

# I'm really excited to get started with

# creating this REST API.

# In order to create the REST API, we're gonna have

# to go though a couple of steps.

# Remember we've got a list of stores

# and we're starting this list with a single store in it

# and that's for a specific reason.

# Creating a store is slightly more complicated

# than retrieving a store.

# So, what we're gonna do is we're gonna start

# with retrieving all our stores

# and that's gonna be the first endpoint we're going

# to implement and that we're gonna test here in this video.

# Then, we're gonna move on to the others.

# The first thing we have to do is to understand one thing,

# which is what JSON is.

# Now, for those of you that are more experienced,

# I'm sure you already know what JSON is,

# but I'll just quickly explain it.

# JSON is, essentially, a dictionary.

# Something like this.

# So, JSON is a set of key value pairs,

# just like a dictionary is and it's really useful

# to send data from one application to another.

# For example, our Javascript application might request a list

# of stores and they come back as a JSON

# and then we can sort of look at each dictionary

# and retrieve some data from it, just like we do in Python.

# So, JSON is really useful

# to send data between applications

# and it looks pretty much just exactly like this.

# However, JSON is not a dictionary.

# JSON is text.

# It is a long string.

# So, our application has to return a string

# in this format.

# And then Javascript has to read that and deal with it,

# as a string, maybe convert it

# to a Javascript, sort of, dictionary, between quotes,

# and then deal with it like that.

# So, there has to be some sort of conversion

# between a dictionary, which is a Python thing,

# and a string, which is something

# that we can send over the internet.

# So, we cannot send a Python dictionary to Javascript,

# because Javascript wouldn't understand it,

# but Javascript does understand what text is

# and it can do its own conversion there.

# Fortunately, Flask really helps us out here

# with a method called jsonify, which takes in a dictionary

# and converts it JSON, which is a string in this format.

# All we have to do is go to the very top of our file

# and say from flask import flask, jsonify.

# And that is a method that we're gonna need.

# Notice how it's lower-case, because it's not a class.

# It is a method.

# So, let's go down into our stores.

# This get_stores method that is going

# to return all our stores.

# And what we're going to do is

# we're gonna say return jsonify(stores).

# Remember, what this is gonna do is it's going

# to convert the stores variable into JSON.

# There is one last small problem,

# which is that JSON is a dictionary

# and our stores variable is not a dictionary.

# It is a list.

# JSON cannot be a list.

# But we wanna return not a single store,

# but a dictionary with all our stores.

# So, what we do is we say jsonify

# and we make this into a dictionary.

# Stores is stores, like that.

# So this is now our dictionary, which has one key only,

# which is stores and that key has a value associated with it,

# which is our list of stores.

# This is our variable that we declared up there.

# And that's all in our dictionary, so we jsonify that

# and we return that to the person making the request.

# So, let's save the app.py.

# Let's go over to our terminal.

# Make sure that we're in the right place.

# So, in my case, the folder is up here.

# /user/jslvtr/code/section3/video_code

# So, let's go there.

# And then let's do python3.5 app.py.

# So now notice we are running.

# Copy that.

# Go over to your browser of choice.

# Paste it in and make sure to say /store.

# So, what do you think is gonna happen, when we press enter?

# What are we going to see on our page?

# Try to create a mental image as to what's gonna come out.

# So, this is what we see.

# A JSON representation of our stores.

# Remember, we've got a dictionary with one key called stores

# and that is a list.

# This is our variable.

# And that list has one element in it, one dictionary,

# and that has a name down here and a list of items.

# Remember dictionaries are not ordered,

# because they are sets.

# So, the items in this case has appeared first,

# even though in our code, the name is first.

# So this is what a REST API really, really does.

# It returns JSON, after doing some processing.

# So, for example, the REST API we're developing will allow us

# to create stores, create items, and return them,

# and things like that.

# It would, for example, be very useful for a mobile app

# that has been created to represent a store.

# The mobile app could call our API and store stores

# and items, so that the mobile app can then retrieve them

# and so on.

# So, what we've got here is something very specific,

# which is the list of stores that we started our programme with

# and also they're in JSON format and we can tell that they're

# in JSON format, as opposed to a Python dictionary,

# because of the double quotes.

# JSON always uses double quotes and never single quotes.

# That's a very important thing in JSON, so remember that.

# Always double quotes, never single quotes.

# And it always has to start with a dictionary,

# so you cannot return a list only.

# So, that's everything for this video.

# We've implemented our first endpoint and,

# in the next video, we're gonna implement the rest

# and that's gonna include creating the stores and the items.

# It's not gonna be too challenging, so you can give it a go

# if you want and, if not, then I'll see you

# in the very next video.


# --------------------------------------


# Fortunately, Flask really helps us out here

# with a method called jsonify, which takes in a dictionary

# and converts it JSON, which is a string in this format.
from flask import Flask, jsonify

app = Flask(__name__)

stores = [
    {
        'name': 'My wonderfull store',
        'items': [
            {
                'item': 'my item',
                'price': 15.99
            }
        ]
    }
]

# POST - used to receive data
# GET  - used to send data back only


# POST /store data: {name:}
@app.route('/store', methods=['POST'])
def create_store():
    pass

# get /store/<string:name>
@app.route('/store/<string:name>')  # https://127.0.0.1:5000/store/some_name
def get_store(name):
    pass

# get /store
@app.route('/store')
def get_stores():
    return jsonify({'stores': stores})

# post /store/<string:name>/item {name:,price:}
@app.route('/store', methods=['POST'])
def create_item_in_store():
    pass

# get /store/<string:name>/item
@app.route('/store/<string:name>/item')
def get_items_in_store(name):
    pass


app.run(port=5000)
