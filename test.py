from flask import Flask, request, jsonify
import mysql.connector
from mysql.connector import Error
from werkzeug.security import generate_password_hash

app = Flask(__name__)


# Database connection function
def create_connection():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='',  # Replace with your database password
        database='your_database_name'  # Replace with your database name
    )


# Route for handling registration
@app.route('/register', methods=['POST'])
def register():
    try:
        email = request.form['email']
        password = request.form['password']

        # Hash the password
        hashed_password = generate_password_hash(password, method='bcrypt')

        # Insert data into the database
        connection = create_connection()
        cursor = connection.cursor()
        query = "INSERT INTO users (email, password) VALUES (%s, %s)"
        cursor.execute(query, (email, hashed_password))
        connection.commit()

        return jsonify({"message": "User registered successfully!"}), 201

    except Error as e:
        print(f"Error: {e}")
        return jsonify({"message": "An error occurred!"}), 500

    finally:
        if (connection.is_connected()):
            cursor.close()
            connection.close()


if __name__ == '__main__':
    app.run(debug=True)
