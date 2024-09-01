from flask import jsonify, request, current_app

def register_routes(app):

    @app.route('/api', methods=['POST'])
    def post_movies():
        db = current_app.config['db']
        data = request.get_json()
        new_movie = {
            "title": data["title"],
            "author": data['author'],
            "published_year": data['published_year'],
            "genre": data['genre'],
            "description": data['description']
        }
        movie = db.movies
        result = movie.insert_one(new_movie)
        inserted_movie_id = result.inserted_id
        
        inserted_movie = movie.find_one({"_id": inserted_movie_id})

        inserted_movie["_id"] = str(inserted_movie["_id"])

        return jsonify(inserted_movie), 201
