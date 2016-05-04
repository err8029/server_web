import flask

from flask import Flask, jsonify, abort, make_response

posts = [
 {
    "userId": 1,
    "id": 1,
    "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
    "body": "quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto"
  },
  {
    "userId": 1,
    "id": 2,
    "title": "qui est esse",
    "body": "est rerum tempore vitae\nsequi sint nihil reprehenderit dolor beatae ea dolores neque\nfugiat blanditiis voluptate porro vel nihil molestiae ut reiciendis\nqui aperiam non debitis possimus qui neque nisi nulla"
  },
  {
    "userId": 1,
    "id": 3,
    "title": "ea molestias quasi exercitationem repellat qui ipsa sit aut",
    "body": "et iusto sed quo iure\nvoluptatem occaecati omnis eligendi aut ad\nvoluptatem doloribus vel accusantium quis pariatur\nmolestiae porro eius odio et labore et velit aut"
  },
]


app = Flask(__name__)

@app.route('/posts/<int:post_id>', methods=['GET'])
def get_task(post_id):
    post = [post for post in posts if post['id'] == post_id]
    if len(post) == 0:
        abort(404)
    return jsonify({'post': post[0]})

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

@app.errorhandler(400)
def bad_request(error):
    return make_response(jsonify({'error': 'Bad request'}), 400)

@app.route('/posts', methods=['POST'])
def create_post():
    if not request.json or not 'title' in request.json or not 'userId' in request.json or not 'body' in request.json:
        abort(400)
    post = {
        'id': posts[-1]['id'] + 1,
        'userId': request.json['userId'],
        'title': request.json['title'],
        'body': request.json['body'],
    }
    posts.append(post)
    return jsonify({'post': post}), 201

if __name__ == "__main__":
     app.run('0.0.0.0')
