from flask import Flask, request, jsonify
from engine.database import Database
from models.user import User
from models.user_profile import UserProfile
from models.friend_connection import FriendConnection
from models.message import Message
from models.media import Media
from models.pet_health import PetHealth
from models.lost_found import LostFound
from models.forum_post import ForumPost
from models.comment import Comment
from models.recommendation import Recommendation

app = Flask(__name__)
db = Database('petpals')

@app.route('/register', methods=['POST'])
def register():
    data = request.json
    user = User.from_dict(data)
    user_id = db.insert_one('users', user.to_dict())
    return jsonify({'message': 'User registered successfully', 'user_id': str(user_id)}), 201

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    user_doc = db.find_one('users', {'username': data['username']})
    if user_doc and user_doc['password'] == data['password']:
        return jsonify({'message': 'Login successful'}), 200
    return jsonify({'error': 'Invalid username or password'}), 401

# Routes for other features...

@app.route('/add_recommendation', methods=['POST'])
def add_recommendation():
    data = request.json
    recommendation = Recommendation(
        user_id=data['user_id'],
        pet_id=data['pet_id'],
        recommendation_type=data['recommendation_type'],
        recommendation_text=data['recommendation_text']
    )
    db.insert_one('recommendations', recommendation.to_dict())
    return jsonify({'message': 'Recommendation added successfully'}), 201

@app.route('/recommendations/<user_id>', methods=['GET'])
def get_recommendations(user_id):
    recommendations = db.find('recommendations', {'user_id': user_id})
    recommendation_list = [Recommendation.from_dict(doc).to_dict() for doc in recommendations]
    return jsonify({'recommendations': recommendation_list}), 200

if __name__ == '__main__':
    app.run(debug=True)








