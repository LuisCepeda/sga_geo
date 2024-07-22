from models.clustering import ClusteringModel

class ClusteringController:
    @staticmethod
    def cluster(data, eps, min_samples):
        try:
            labels = ClusteringModel.perform_clustering(data, eps, min_samples)
            return {'clusters': labels}
        except Exception as e:
            return {'error': str(e)}

    @staticmethod
    def check_status():
        return {'status': 'OK'}
