import ray

def init_ray_cluster(address=None, **kwargs):
    """
    Initialize a Ray cluster.
    Can connect to an existing cluster or start a new one.
    """
    ray.init(address=address, **kwargs)

def shutdown_ray_cluster():
    """
    Shut down the Ray cluster.
    """
    if ray.is_initialized():
        ray.shutdown()

def get_ray_cluster_resources():
    """
    Retrieve information about the resources available in the Ray cluster.
    """
    return ray.cluster_resources()

def get_ray_available_resources():
    """
    Retrieve information about the available resources in the Ray cluster.
    """
    return ray.available_resources()
