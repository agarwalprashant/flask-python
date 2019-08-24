
from flask import Flask, jsonify, request, render_template

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


@app.route('/')
def home():
    return render_template('index.html')

# POST - used to receive data
# GET  - used to send data back only


# POST /store data: {name:}
@app.route('/store', methods=['POST'])
def create_store():
    request_data = request.get_json()
    new_store = {
        'name': request_data['name'],
        'items': []
    }
    stores.append(new_store)
    return jsonify(new_store)

# get a specific store by name
# get /store/<string:name>
@app.route('/store/<string:name>')  # https://127.0.0.1:5000/store/some_name
def get_store(name):
    # iterate over stores
    # if the store name matches,return it
    # if none match , return an error message
    for store in stores:
        if store['name'] == name:
            return jsonify(store)
    return jsonify({'message': 'store not found'})

# get /store
@app.route('/store')
def get_stores():
    return jsonify({'stores': stores})

# post /store/<string:name>/item {name:,price:}
@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store(name):
    request_data = request.get_json()

    for store in stores:
        if store['name'] == name:
            new_item = {
                'name': request_data['name'],
                'price': request_data['price']
            }
            store['items'].append(new_item)
            # totally up to you what you want to return in the next line
            return jsonify(new_item)
    return jsonify({'message': 'store not found'})

# get /store/<string:name>/item
@app.route('/store/<string:name>/item')
def get_items_in_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify({'items': store['items']})
    return jsonify({'message': 'store not found'})


app.run(port=5000, debug=True)
