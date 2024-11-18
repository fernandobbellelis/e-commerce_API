from flask import Flask, request, session, jsonify
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

# Secret key for werkzeug hash encryption
app.secret_key = 'supersecretkey'  

# In-memory storage for users
users = {}

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
    





if __name__ == '__main__':
    app.run(debug=True)