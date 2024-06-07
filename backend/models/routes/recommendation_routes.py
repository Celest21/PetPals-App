from flask import Blueprint, request, jsonify
from models.recommendation import Recommendation

recommendation_bp = Blueprint('recommendation', __name__)

# Route definitions for recommendation-related operations
