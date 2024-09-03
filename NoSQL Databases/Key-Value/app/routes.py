from flask import request, jsonify

def register_routes(app):
    @app.route('/user', methods=['POST'])
    def add_user():
        if not request.json or 'username' not in request.json:
            return jsonify({'error': 'Invalid data, username is required'}), 400
        
        username = request.json['username']
        user_data = request.json.get('data', {})
        
        redis_client = app.redis_client
        if redis_client:
            redis_key = f"user:{username}"
            redis_client.hset(redis_key, mapping=user_data)
            return jsonify({'message': f'User {username} added successfully.'}), 201
        else:
            return jsonify({'error': 'Failed to connect to Redis'}), 500
    
    @app.route('/user/<username>', methods=['GET'])
    def get_user(username):
        redis_client = app.redis_client
        if redis_client:
            redis_key = f"user:{username}"
            user_data = redis_client.hgetall(redis_key)
            
            if not user_data:
                return jsonify({'error': 'User not found'}), 404
            
            return jsonify({'username': username, 'data': user_data}), 200
        else:
            return jsonify({'error': 'Failed to connect to Redis'}), 500
