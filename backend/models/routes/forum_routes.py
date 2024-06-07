from flask import Blueprint, request, jsonify
from models.forum import Forum, Thread, Post

forum_bp = Blueprint('forum', __name__)

# Route definitions for forum-related operations
