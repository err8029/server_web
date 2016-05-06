import json
from flask import Flask, jsonify, abort, make_response, request
import comments
import posts
import todos
import photos
import users
import albums



app = Flask(__name__)

comments = comments.comments()
posts = posts.posts()
todos = todos.todos()
photos = photos.photos()
albums = albums.albums()
users = users.users()

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

@app.errorhandler(400)
def bad_request(error):
    return make_response(jsonify({'error': 'Bad request'}), 400)

#-----------------------------------------------------------------------------------------------------------------------------

@app.route('/posts/<int:post_id>', methods=['GET'])
def get_task(post_id):
    post = [post for post in posts if post['id'] == post_id]
    if len(post) == 0:
        abort(404)
    return jsonify({'post': post[0]})

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

@app.route('/posts/<int:post_id>', methods=['PUT'])
def update_post(post_id):
    post = [post for post in posts if post['id'] == post_id]
    if len(post) == 0:
        abort(404)
    if not request.json:
        abort(400)
    post[0]['title'] = request.json.get('title', post[0]['title'])
    post[0]['body'] = request.json.get('body', post[0]['body'])
    return jsonify({'post': post[0]})

@app.route('/posts/<int:post_id>', methods=['DELETE'])
def delete_post(post_id):
    post = [post for post in posts if post['id'] == post_id]
    if len(post) == 0:
        abort(404)
    posts.remove(post[0])
    return jsonify({'result': True})

#-----------------------------------------------------------------------------------------------------------------------------

@app.route('/comments/<int:comment_id>', methods=['GET'])
def get_task_Comments(comment_id):
    comment = [comment for comment in comments if comment['id'] == comment_id]
    if len(comment) == 0:
        abort(404)
    return jsonify({'post': comment[0]})

app.route('/comments', methods=['POST'])
def create_post_Comments():
    if not request.json or not 'title' in request.json or not 'userId' in request.json or not 'body' in request.json:
        abort(400)
    comment = {
        'id': 1,
        'id': posts[-1]['id'] + 1,
        'userId': request.json['userId'],
        'title': request.json['title'],
        'body': request.json['body'],
    }
    comments.append(comment)
    return jsonify({'post': comment}), 201

app.route('/comments/<int:comment_id>', methods=['PUT'])
def update_post_Comments(comment_id):
    comment = [comment for comment in comments if comment['id'] == comment_id]
    if len(post) == 0:
        abort(404)
    if not request.json:
        abort(400)
    comment[0]['title'] = request.json.get('title', comment[0]['title'])
    comment[0]['body'] = request.json.get('body', comment[0]['body'])
    return jsonify({'post': comment[0]})

@app.route('/comments/<int:post_id>', methods=['DELETE'])
def delete_post_Comments(comment_id):
    comment = [comment for comment in comments if comment['id'] == comment_id]
    if len(comment) == 0:
        abort(404)
    comments.remove(comment[0])
    return jsonify({'result': True})

#-----------------------------------------------------------------------------------------------------------------------------------

@app.route('/todos/<int:todo_id>', methods=['GET'])
def get_task_Todos(todo_id):
    todo = [todo for todo in todos if todo['id'] == todo_id]
    if len(todo) == 0:
        abort(404)
    return jsonify({'post': todo[0]})

app.route('/todos', methods=['POST'])
def create_post_Todos():
    if not request.json or not 'title' in request.json or not 'userId' in request.json or not 'body' in request.json:
        abort(400)
    todo = {
        'id': 1,
        'id': posts[-1]['id'] + 1,
        'userId': request.json['userId'],
        'title': request.json['title'],
        'body': request.json['body'],
    }
    todos.append(todo)
    return jsonify({'post': todo}), 201

app.route('/todos/<int:todo_id>', methods=['PUT'])
def update_post_Todos(todo_id):
    todo = [todo for todo in todos if todo['id'] == todo_id]
    if len(todo) == 0:
        abort(404)
    if not request.json:
        abort(400)
    todo[0]['title'] = request.json.get('title', todo[0]['title'])
    todo[0]['body'] = request.json.get('body', todo[0]['body'])
    return jsonify({'post': todo[0]})

@app.route('/todos/<int:todo_id>', methods=['DELETE'])
def delete_post_Todos(todo_id):
    todo = [todo for todo in todos if todo['id'] == todo_id]
    if len(todo) == 0:
        abort(404)
    comments.remove(todo[0])
    return jsonify({'result': True})

#-----------------------------------------------------------------------------------------------------------------------------------

@app.route('/albums/<int:album_id>', methods=['GET'])
def get_task_Albums(album_id):
    album = [album for album in albums if album['id'] == album_id]
    if len(album) == 0:
        abort(404)
    return jsonify({'post': album[0]})

app.route('/albums', methods=['POST'])
def create_post_Albums():
    if not request.json or not 'title' in request.json or not 'userId' in request.json or not 'body' in request.json:
        abort(400)
    album = {
        'id': 1,
        'id': posts[-1]['id'] + 1,
        'userId': request.json['userId'],
        'title': request.json['title'],
        'body': request.json['body'],
    }
    albums.append(album)
    return jsonify({'post': album}), 201

app.route('/albums/<int:albums_id>', methods=['PUT'])
def update_post_Albums(album_id):
    album = [album for album in albums if album['id'] == album_id]
    if len(album) == 0:
        abort(404)
    if not request.json:
        abort(400)
    album[0]['title'] = request.json.get('title', album[0]['title'])
    album[0]['body'] = request.json.get('body', album[0]['body'])
    return jsonify({'post': album[0]})

@app.route('/albums/<int:album_id>', methods=['DELETE'])
def delete_post_Albums(album_id):
    album = [album for album in albums if album['id'] == album_id]
    if len(album) == 0:
        abort(404)
    albums.remove(album[0])
    return jsonify({'result': True})

#-----------------------------------------------------------------------------------------------------------------------------------

@app.route('/photos/<int:photo_id>', methods=['GET'])
def get_task_Photos(photo_id):
    photo = [photo for photo in photos if photo['id'] == photo_id]
    if len(photo) == 0:
        abort(404)
    return jsonify({'post': photo[0]})

app.route('/photos', methods=['POST'])
def create_post_Photos():
    if not request.json or not 'title' in request.json or not 'userId' in request.json or not 'body' in request.json:
        abort(400)
    photo = {
        'id': 1,
        'id': posts[-1]['id'] + 1,
        'userId': request.json['userId'],
        'title': request.json['title'],
        'body': request.json['body'],
    }
    photos.append(photo)
    return jsonify({'post': photo}), 201

app.route('/photos/<int:photo_id>', methods=['PUT'])
def update_post_Photos(photo_id):
    photo = [photo for photo in photos if photo['id'] == photo_id]
    if len(photo) == 0:
        abort(404)
    if not request.json:
        abort(400)
    photo[0]['title'] = request.json.get('title', photo[0]['title'])
    photo[0]['body'] = request.json.get('body', photo[0]['body'])
    return jsonify({'post': photo[0]})

@app.route('/photos/<int:photo_id>', methods=['DELETE'])
def delete_post_Photos(photo_id):
    photo = [photo for photo in photo if photo['id'] == photo_id]
    if len(photo) == 0:
        abort(404)
    photos.remove(album[0])
    return jsonify({'result': True})

#-----------------------------------------------------------------------------------------------------------------------------------

@app.route('/users/<int:user_id>', methods=['GET'])
def get_task_Users(user_id):
    user = [user for user in users if user['id'] == user_id]
    if len(user) == 0:
        abort(404)
    return jsonify({'post': user[0]})

app.route('/user', methods=['POST'])
def create_post_Users():
    if not request.json or not 'title' in request.json or not 'userId' in request.json or not 'body' in request.json:
        abort(400)
    user = {
        'id': 1,
        'id': posts[-1]['id'] + 1,
        'userId': request.json['userId'],
        'title': request.json['title'],
        'body': request.json['body'],
    }
    users.append(user)
    return jsonify({'post': user}), 201

app.route('/users/<int:user_id>', methods=['PUT'])
def update_post_Users(user_id):
    user = [user for user in users if user['id'] == user_id]
    if len(user) == 0:
        abort(404)
    if not request.json:
        abort(400)
    user[0]['title'] = request.json.get('title', user[0]['title'])
    user[0]['body'] = request.json.get('body', user[0]['body'])
    return jsonify({'post': user[0]})

@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_post_Users(photo_id):
    user = [user for user in user if user['id'] == user_id]
    if len(user) == 0:
        abort(404)
    users.remove(album[0])
    return jsonify({'result': True})



if __name__ == "__main__":

     app.run(debug=True)
