import ray
from ray.util.dask import ray_dask_get
from dask.distributed import Client

class StanRayExecutor:
    def __init__(self, address='auto', **ray_kwargs):
        # Store Ray initialization arguments
        self.address = address
        self.ray_kwargs = ray_kwargs
        self.client = None

    def start(self):
        # Initialize Ray only if it hasn't been initialized yet
        if not ray.is_initialized():
            ray.init(address=self.address, **self.ray_kwargs)
        # Create a Dask client that uses Ray as the execution backend
        self.client = Client()
        self.client.get = ray_dask_get  # Override Dask's default scheduler with Ray's

    def execute(self, stan_model_func, data, **kwargs):
        # Wrap the Stan model execution function with Dask's delayed
        lazy_task = delayed(stan_model_func)(data, **kwargs)
        # Compute the task using Dask, which will use Ray as the execution backend
        future_result = self.client.compute(lazy_task)
        return future_result

    def shutdown(self):
        # Shut down the Dask client if it's been started
        if self.client:
            self.client.shutdown()
        # Shut down the Ray cluster if it's been initialized
        if ray.is_initialized():
            ray.shutdown()

    # The __enter__ and __exit__ methods allow StanRayExecutor to be used as a context manager
    def __enter__(self):
        self.start()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.shutdown()
