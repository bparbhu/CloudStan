from dask import delayed
from dask.distributed import Client
import ray
from ray.util.dask import ray_dask_get

class StanRayExecutor:
    def __init__(self):
        # Initialize Ray and set it as the Dask scheduler
        ray.init()
        dask.config.set(scheduler=ray_dask_get)
        # Initialize Dask client, which will use Ray under the hood
        self.client = Client()

    def execute(self, stan_model_func, data, **kwargs):
        # Wrap the Stan model execution function with Dask's delayed
        lazy_task = delayed(stan_model_func)(data, **kwargs)
        # Compute the task using Dask, which will use Ray as the execution backend
        future_result = self.client.compute(lazy_task)
        return future_result

    def shutdown(self):
        # Shut down the Ray cluster and the Dask client
        self.client.shutdown()
        ray.shutdown()
