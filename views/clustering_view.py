from flask import Blueprint, request, jsonify
from controllers.clustering_controller import ClusteringController

clustering_view = Blueprint('clustering_view', __name__)

@clustering_view.route('/cluster', methods=['POST'])
def cluster():
    data = request.json.get('data')
    eps = request.json.get('eps', 0.01)
    min_samples = request.json.get('min_samples', 2)
    response = ClusteringController.cluster(data, eps, min_samples)
    return jsonify(response)

@clustering_view.route('/cluster', methods=['GET'])
def check():
    response = ClusteringController.check_status()
    return jsonify(response)
