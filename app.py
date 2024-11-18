from flask import Flask, request, session, jsonify
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Should be more secure in production

# In-memory storage for users and orders
users = {}
orders = {}
order_id_counter = 1

# ---------------------------------------------

@app.route('/register', methods=['POST'])
def register():
    try:
        username = request.values["username"]
        password = request.values["password"]

        if username in users:
            raise ValueError('User already exists!')

        users[username] = generate_password_hash(password)
        return jsonify({'message': 'User registered successfully!'}), 201
    
    except KeyError:
        return jsonify({'message': 'Username and password required!'}), 400
    except ValueError as ve:
        return jsonify({'message': str(ve)}), 409
    except Exception as e:
        return jsonify({'message': 'An error occurred during registration.'}), 500

# ---------------------------------------------

@app.route('/login', methods=['POST'])
def login():
    try:
        username = request.values["username"]
        password = request.values["password"]

        hashed_password = users.get(username)

        if not hashed_password or not check_password_hash(hashed_password, password):
            raise ValueError('Invalid username or password!')

        session['user'] = username
        return jsonify({'message': 'Logged in successfully!'}), 200
    
    except KeyError:
        return jsonify({'message': 'Username and password required!'}), 400
    except ValueError as ve:
        return jsonify({'message': str(ve)}), 401
    except Exception as e:
        return jsonify({'message': 'An error occurred during login.'}), 500

# ---------------------------------------------

@app.route('/logout', methods=['POST'])
def logout():
    try:
        if 'user' not in session:
            return jsonify({'message': 'User already logged out.'}), 200

        session.pop('user', None)
        return jsonify({'message': 'Logged out successfully!'}), 200

    except Exception as e:
        return jsonify({'message': 'An error occurred during logout.'}), 500

# ---------------------------------------------

@app.route('/create_order', methods=['POST'])
def create_order():
    global order_id_counter
    try:
        if 'user' not in session:
            return jsonify({'message': 'User must be logged in to create an order.'}), 401


        order_id = order_id_counter
        order_id_counter += 1

        orders[order_id] = {
            'username': session['user'],
            'order_data': request.values["order_data"],
            'status': 'active'
        }
        return jsonify({'message': 'Order created successfully!', 'order_id': order_id}), 201

    except Exception as e:
        return jsonify({'message': 'An error occurred while creating order.'}), 500

# ---------------------------------------------

@app.route('/cancel_order', methods=['POST'])
def cancel_order():
    try:
        if 'user' not in session:
            return jsonify({'message': 'User must be logged in to cancel an order.'}), 401

        # Expecting order ID to be passed in the JSON body
        order_id = int(request.values["order_data"])

        if order_id == None:
            return jsonify({'message': 'Order ID is required.'}), 400

        if order_id not in orders or orders[order_id]['username'] != session['user']:
            return jsonify({'message': 'Order not found or not authorized to cancel this order.'}), 404

        orders[order_id]['status'] = 'cancelled'
        return jsonify({'message': 'Order cancelled successfully!'}), 200

    except Exception as e:
        return jsonify({'message': 'An error occurred while cancelling order.'}), 500

# ---------------------------------------------

@app.route('/get_orders', methods=['GET'])
def get_orders():
    try:
        if 'user' not in session:
            return jsonify({'message': 'User must be logged in to view orders.'}), 401

        user_orders = {oid: details for oid, details in orders.items() if details['username'] == session['user']}
        return jsonify(user_orders), 200

    except Exception as e:
        return jsonify({'message': 'An error occurred while retrieving orders.'}), 500

# ---------------------------------------------

if __name__ == '__main__':
    app.run(debug=True)