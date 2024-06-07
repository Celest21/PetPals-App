from flask import Blueprint, request, jsonify
from models.comment import Comment

comment_bp = Blueprint('comment', __name__)

# Route definitions for comment-related operations
