from flask import Flask, request,jsonify
from clustering import perform_clustering
app = Flask(__name__)

@app.route('/cluster', methods=['POST'])
def cluster():    
    try:
        data = request.json['data']
        eps = request.json.get('eps', 0.01)  # Ajustar el parámetro eps
        min_samples = request.json.get('min_samples', 2)
        
        labels = perform_clustering(data, eps, min_samples)
        
        return jsonify({'clusters': labels})
    except Exception as e:
        return jsonify({'error': str(e)})
    
    
if __name__ == '__main__':
    app.run(debug=True)