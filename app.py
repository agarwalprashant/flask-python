# - [Narrator] Hi, and welcome back to the course.

# Remember our simple Flask application?

# Now, we're going to extend that to show the endpoints

# that we looked at in the very last presentation.

# We're going to simulate an online store using Flask.

# There were a couple of things that we discussed.

# Net post was used to receive data,

# and the get was used to, essentially, send data back only.

# Remember, from the browser's perspective,

# this is the opposite.

# The browser will use post to send us data.

# And it will use get to receive data.

# But here, we are not a browser, we are a server.

# So, when we receive a post request,

# that means we are receiving some data,

# and therefore we have to deal with it.

# And when we receive a get request,

# that means that we have to send data back.

# For example, when we receive post store,

# and that means that we have to probably create a store.

# We may receive get store, and that means

# we have to send back a list of stores.

# So, the endpoints that we're gonna create

# are post for store, and this is,

# the data that we're gonna receive is a name.

# We're gonna create get of store,

# slash string name.

# Get for stores, we're gonna create post

# for a store string, oh, apologies,

# string name item.

# And also get for store string name item.

# So, what these endpoints are gonna do

# is, the first one is gonna create a new store

# with a given name.

# The second one is going to get a store for a given name,

# and it's gonna return some data about it.

# The third one is going to return a list of all the stores.

# The fourth one is going to create an item

# inside a specific store, with a given name.

# And the last one is gonna get all the items

# in a specific store.

# This one will also have a name and a price, for example.

# OK.

# So, I'll create an example of a post request

# and a get request for you,

# and then we, I'll expect you to create the rest.

# So, for the first port request.

# Well, we know how to create an endpoint.

# It is @app.root, and here, before we put a forward slash,

# that was the root of our application, the home page,

# now we wanna put it as slash store,

# because that is what this endpoint is.

# Therefore, our browser, or our web application,

# or our m, whoever is really calling our API

# is going to call this endpoint.

# However, it has to be a post.

# By default, when you use app.route,

# that is a get request.

# And browsers, by default, only do get requests.

# So, we're gonna need to say comma methods equal post.

# So, this defines our route as being slash store,

# and as being accessible only via a post request.

# If we want it to be accessible via a get request, as well,

# then we could do post and get.

# So then, this endpoint could be called

# either via post or via get.

# We will look at how that works later on in the course.

# Then, we have to associate a method with it.

# And in this case, I'm gonna call the method create store.

# And it's not going to do anything for now,

# but we will make it do stuff later on.

# To get the store, well, fairy simple.

# I'm sure you can do it yourself.

# So, if you think you can, pause the video now

# and give it a go.

# And if not, just keep watching and I will implement it here.

# To get a store, we'll have app.route slash store,

# slash string name.

# This is a special Flask bit of syntax,

# which means that when we get store,

# when we create our method,

# our method can have a parameter, which is name.

# This name here has to match this one here.

# And therefore, when we receive a request

# such as an http://107.0.0.1/5000/store/some_name,

# some name is going to be this name here.

# So, the name variable will contain some name.

# If we have a store that has that name,

# we're gonna be able to return it, using that as a key.

# OK.

# So, this is also going to pass.

# And then, you know, this is just going to apply

# for, really, the rest of them.

# And this one is only store, so it doesn't

# need the string name.

# And also, it's not gonna have a parameter.

# For the post, we're going to copy this one here,

# and it's gonna have string name slash item.

# Make sure to not forget any of these little bit

# of syntax there, because that can be quite confusing

# for Flask if you do that.

# And finally, we're going to have something like this,

# down here.

# Remember to change the method names, as well,

# because they have to be unique.

# So, I'm gonna call this method get item store,

# because that's essentially what this is going to do.

# This is going to retrieve all the items

# in a specific store.

# For this one, it's going to be create item in store.

# For this one, it is gonna get stores,

# and this one is gonna be get store.

# This one is gonna be create store.

# So, these are our endpoints.

# So, we've got our five endpoints now,

# as we discussed in the last presentation.

# And all we have to do now is really implement them.

# So, how do we implement them?

# Well, we, first of all, need a way to store our stores.

# So, that can be, for example, something like a list.

# And our stores can be an empty list initially,

# and then it can have a dictionary in it,

# and the dictionary is gonna have a name,

# and the name's gonna be, for example,

# My Wonderful Store.

# And there's also gonna have a list of items,

# and each item is going to have a name,

# such as My Item and a price, such as 15.99.

# OK.

# So, hopefully this makes sense.

# I'm just gonna clean this up a bit for you,

# so it's a bit easier to understand or to know.

# OK.

# So, our store's list is going to contain a list

# of dictionaries.

# So, here we've got one dictionary, but we could have many.

# Each dictionary has a name, such as our stores do,

# and the name, in this case, is My Wonderful Store.

# And it also has a list of items.

# And in this case, items is a list.

# So, we can have many other dictionaries in here,

# and each dictionary is going to have a name

# and a price.

# We could do this with object oriented programming,

# if we wanted, and we're gonna explore

# how to do that later on, of course.

# And also, normally, we would be storing these things

# to a database, but in order to simplify things

# and just teach you the basics of RS API,

# we're gonna stick to having a dictionary here, in memory.

# So, hopefully that's all right.

# And in the next video, we're going to look

# into implementing these endpoints.

# So, I'll see you there.



from flask import Flask
app = Flask(__name__)

stores = [
  {
    'name':'My wonderfull store',
    'items':[
      {
        'item': 'my item',
        'price':15.99
      }
    ]
  }
  ]

# POST - used to receive data
# GET  - used to send data back only


# POST /store data: {name:}
@app.route('/store',methods=['POST'])
def create_store():
  pass

# get /store/<string:name>
@app.route('/store/<string:name>') # https://127.0.0.1:5000/store/some_name
def get_store(name):
  pass

# get /store
@app.route('/store') 
def get_stores(name):
  pass

# post /store/<string:name>/item {name:,price:}
@app.route('/store',methods=['POST'])
def create_item_in_store():
  pass

# get /store/<string:name>/item
@app.route('/store/<string:name>/item') 
def get_items_in_store(name):
  pass

app.run(port=5000)
