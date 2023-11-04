import dask
from ray.util.dask import ray_dask_get

def setup_ray_scheduler():
    """
    Set up Dask to use the Ray scheduler.
    This allows Dask tasks to be executed on a Ray cluster.
    """
    dask.config.set(scheduler=ray_dask_get)

def reset_default_scheduler():
    """
    Reset Dask to use the default scheduler.
    """
    dask.config.set(scheduler='threads')  # Or whatever the default is.
