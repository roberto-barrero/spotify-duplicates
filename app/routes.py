"""Route definitions for the Flask application."""
from flask import Blueprint, jsonify

main_bp = Blueprint('main', __name__)


@main_bp.route('/')
def index():
    """Root endpoint returning basic API information."""
    return jsonify({
        'name': 'Spotify Duplicates API',
        'version': '1.0.0',
        'description': 'A service that detects duplicates in Spotify playlists'
    })


@main_bp.route('/health')
def health():
    """Health check endpoint."""
    return jsonify({
        'status': 'healthy'
    })
