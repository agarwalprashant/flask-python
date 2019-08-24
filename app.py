# - [Instructor] Hi and welcome back to the course.

# In this video we're going to be creating new stores,

# using our API.

# However, we're not going to be able to test

# the creation of stores,

# using our JavaScript application,

# because, that gets slightly more complicated,

# and this is not a JavaScript course.

# However,

# there is another way of testing the API

# and we are gonna do that

# the right way really.

# We normally wouldn't test the API

# using JavaScript,

# we would test it using a specific API testing tool,

# but we will still look at using the API

# from within JavaScript

# and then we will look at testing the API afterwards.

# Anyway, for this video,

# we're going to create a new store.

# And the first thing we have to do,

# is to be able to access the data that is coming back

# to us from the request.

# So the browser,

# or the API testing tool,

# is gonna send us some data,

# the name of the store,

# and we have to be able to access that data.

# So the first thing we have to do

# is go up to our first line of code,

# and we're going to import something else.

# We're gonna import flask,

# JSONify,

# and also request.

# Request without an s at the end.

# There's also a thing called requests.

# And that's a different package.

# So from flask we want to import request.

# And then in the create store,

# what we wanna do is say

# request data is equal to request dot get JSON.

# This request is the request that was made

# to this endpoint.

# So when the browser sends us the request

# to create a new store,

# this request is that one.

# And the browser will also send us some

# JSON data.

# Which is the name of the store.

# So this is going to allow us to get that data back.

# Then we're gonna create a new store,

# which is gonna be a dictionary

# with a name,

# where the name is request data name,

# because that's gonna be the JSON.

# When we do get JSON,

# and this method already converts the JSON string

# into a python dictionary,

# so we can access it like that.

# And also it's going to have a set of items

# which is going to be an empty list.

# We're then going to do stores that dot append,

# and append our new store.

# And finally we're going to return

# the new store that we've created.

# Just so the browser can understand that we

# have indeed created this store.

# So how would we return the new store.

# I'm sure you got it.

# Return, JSONify,

# of new store.

# It's important to include JSONify,

# because if not,

# we will try to return a dictionary

# and that will fail because we have to return a string.

# Okay, so this is how we would create a new store.

# And as I said,

# over the next few videos we're going to be testing

# this out with JavaScript,

# but we will not be able to test the

# creation of stores with JavaScript,

# that gets too complicated,

# so we're going to test it with a different tool,

# and that tool is what we use

# professionally very very often.

# So it's good for you to learn that as well.

# To retrieve a specific store,

# well, all we wanna do is go over the stores,

# finding the one that matches this name,

# and return that one.

# So I will write a wee comment here,

# iterate over stores,

# if the store name matches,

# return that one.

# If none matches, return an error message.

# And I think you can pause the video at this point

# and give this a go.

# Because you know how to iterate,

# you know how to check using an if statement,

# and you know how to return a store.

# So go ahead and do that,

# I would definitely recommend that you try that now.

# Hopefully you gave it a go,

# and what I would do is to iterate over stores,

# for store in stores, stores remember is our variable,

# and then I would say,

# if the store name is equal to name,

# which is the one that we're receiving here,

# then return the store,

# return JSONify of store.

# Remember, store is a dictionary,

# so we can just return that store directly,

# and if no store matches,

# we want to return some sort of error message,

# such as message, store not found.

# That's just to tell whoever's calling the API,

# that there was indeed some sort of error.

# Okay, now you can do the same thing

# for the get store slash name slash item.

# I'm sure you can go ahead and implement this now

# yourself, now that you know how the other one works.

# Hopefully you managed,

# the way I would do it is actually very similar,

# for store in stores, if the stores name matches,

# then we're going to return the items in that store,

# so we're going to return a JSONify of items.

# Where that's the stores items.

# And also if we don't find anything,

# we're going to return the appropriate error message.

# Like so.

# Finally, the most challenging in point,

# is the create item.

# I'm sure that you can do this as well.

# If you give it a bit of thought

# and you look at how we've created a store above,

# in a create store method,

# you can do a very similar thing

# to create an item.

# Once again I would recommend pausing the video

# and giving this a go.

# But then I always recommend that,

# so you may be ignoring this recommendation by now,

# hopefully not.

# So pause the video and give it a go

# and then we'll do it here.

# Hopefully you were successful,

# and what I would do is,

# once again,

# for store in stores,

# if the store name matches our name,

# then we're going to create a new item,

# that item is going to be one with a name

# which is going to be the request data name,

# and with a price which is going to be the request.

# Oh, sorry,

# price like that, and request data.

# Price.

# Naturally, you may have already realised the request data

# doesn't exist in this method,

# so we have to create it.

# Request data,

# equal request dot get JSON.

# Like so.

# So this is our new item there,

# and what we wanna do is append it,

# so store, items, dot append new item.

# And then at the end,

# new item,

# at the end we can return a JSONify,

# of the store,

# or if you prefer, you can return JSONify

# if new item that may be also an option.

# It's totally up to you what you want to return

# or up to your API rather.

# Also at the end,

# we wanna return an error message,

# if we didn't find the store.

# Something to keep in mind

# is that if we return an item here,

# that terminates the method

# and we don't return this message.

# We will only return this message

# if we go through every store,

# and we never return anything.

# So if we start on our first store,

# and the name does not match,

# we will just skip all of this code,

# and we will move onto the next store.

# And if the name doesn't match,

# we will skip all of that code

# and we will go on to the next one,

# and eventually if none of them match,

# we will never have ran this code here,

# so we will just exit the loop,

# and return this error message at the end.

# Okay.

# Perfect.

# So these are our end points,

# now in the next video,

# I've got an HTML file for you to download,

# that has some boiler plate code,

# and then we're gonna use that

# to kinda test this out a bit and

# look at how you can run

# some JavaScript code in this API,

# and after that we're going to,

# properly test this API using a professional tool.

# Which is free as well.

# So don't worry about paying anything.

# So without further ado,

# I'll see you in the next video, with some JavaScript.


# --------------------------------------


# Fortunately, Flask really helps us out here

# with a method called jsonify, which takes in a dictionary

# and converts it JSON, which is a string in this format.
from flask import Flask, jsonify,request

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
    request_data = request.get_json()
    new_store = {
      'name':request_data['name'],
      'items':[]
    }
    stores.append(new_store)
    return jsonify(new_store)

#get a specific store by name
# get /store/<string:name>  
@app.route('/store/<string:name>')  # https://127.0.0.1:5000/store/some_name
def get_store(name):
    # iterate over stores
    # if the store name matches,return it
    # if none match , return an error message
    for store in stores:
      if store['name'] == name
        return jsonify(store)
    return jsonify({'message':'store not found'})

# get /store
@app.route('/store')
def get_stores():
    return jsonify({'stores': stores})

# post /store/<string:name>/item {name:,price:}
@app.route('/store', methods=['POST'])
def create_item_in_store(name):
    request_data = request.get_json()
    
    for store in stores:
      if store['name'] == name
        new_item = {
            'name':request_data['name']
            'price':request_data['price']
        }
        store['items'].append(new_item)
        # totally up to you what you want to return in the next line
        return jsonify(new_item)
    return jsonify({'message':'store not found'})

# get /store/<string:name>/item
@app.route('/store/<string:name>/item')
def get_items_in_store(name):
  for store in stores:
    if store['name'] == name
      return jsonify({'items':store['items']}) 
  return jsonify({'message':'store not found'})


app.run(port=5000)
