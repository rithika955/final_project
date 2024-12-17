from flask import Flask, jsonify
import mysql.connector

app = Flask(__name__)

# Database connection
DATABASE_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': 'SnehaJoshi92$',
    'database': 'UserRetentionDB'
}

@app.route('/user-retention', methods=['GET'])
def get_user_retention():
    try:
        db = mysql.connector.connect(
            host=DATABASE_CONFIG['host'],
            user=DATABASE_CONFIG['user'],
            password=DATABASE_CONFIG['password'],
            database=DATABASE_CONFIG['database']
        )
        cursor = db.cursor(dictionary=True)

        cursor.execute("""
            SELECT retention_period, COUNT(user_id) AS inactive_count 
            FROM user_retention_data 
            WHERE status = 'inactive' 
            GROUP BY retention_period;
        """)
        result = cursor.fetchall()

        return jsonify(result)

    except mysql.connector.Error as err:
        return jsonify({"error": str(err)})

if __name__ == '__main__':
    app.run(debug=True)

