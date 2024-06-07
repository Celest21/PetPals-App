from flask import Flask
from models.engine.database import Database
from models.routes import user_routes
from models.routes import friend_routes
from models.routes import message_routes
from models.routes import media_routes
from models.routes import pet_routes
from models.routes import lost_found_routes
from models.routes import forum_routes
from models.routes import comment_routes
from models.routes import recommendation_routes

app = Flask(__name__)
db = Database('petpals')

# Registering blueprints
app.register_blueprint(user_routes.user_bp)
app.register_blueprint(friend_routes.friend_bp)
app.register_blueprint(message_routes.message_bp)
app.register_blueprint(media_routes.media_bp)
app.register_blueprint(pet_routes.pet_bp)
app.register_blueprint(lost_found_routes.lost_found_bp)
app.register_blueprint(forum_routes.forum_bp)
app.register_blueprint(comment_routes.comment_bp)
app.register_blueprint(recommendation_routes.recommendation_bp)

if __name__ == "__main__":
    app.run(debug=True)









