from flask import Flask
import redis

def create_app():
    app = Flask(__name__)

    with app.app_context():
        app.redis_client = connect_redisDB()

    return app

def connect_redisDB():
    try:
        redis_client = redis.StrictRedis(
            host='localhost',
            port=6379,
            db=0,
            decode_responses=True
        )
        redis_client.ping()
        print("Connected to Redis")
    except redis.ConnectionError:
        print("Could not connect to Redis")
        redis_client = None

    return redis_client
