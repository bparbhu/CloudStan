# stan_dask_cloud/__init__.py

"""
stan_dask_cloud: A Python package for running Stan models using Dask on cloud infrastructure.
"""

# Version of the stan_dask_cloud package
__version__ = '0.1.0'

# Import main functionality
from src.dask_integration.dask_client import DaskClient
from src.dask_integration.distributed_models import DistributedStanModel
from src.models.stan_model import StanModel
from src.cloud_integration.cloud_setup import CloudSetup
from src.data_management.data_handlers import DataHandler
from src.utils.config import Configuration
from src.utils.logging import get_logger

# Set up logging for the package
logger = get_logger()


# stan_dask_cloud/__init__.py

# ... other imports and initializations ...

def setup_model(stan_model_code, data, cloud_config, dask_config, model_config=None):
    """
    Entry point for setting up a Stan model to run with a Dask cluster in the cloud.

    Parameters:
    - stan_model_code (str): Stan model code or file path to .stan file.
    - data (dict): Data to be used in fitting the Stan model.
    - cloud_config (dict): Configuration for cloud resources.
    - dask_config (dict): Configuration for the Dask cluster.
    - model_config (dict, optional): Additional model configuration options.

    Returns:
    - DistributedStanModel: A model object ready to be fitted using the Dask cluster.
    """

    # Step 1: Set up the cloud environment (e.g., AWS, GCP, Azure)
    cloud_setup = CloudSetup(cloud_config)
    cloud_setup.initialize_resources()

    # Step 2: Initialize the Dask client to interact with the cluster
    dask_client = DaskClient(dask_config)
    dask_client.create_cluster()

    # Step 3: Load the Stan model, which could be from a file or code string
    stan_model = StanModel(stan_model_code, model_config)

    # Step 4: Handle data preparation and potentially upload to cloud storage
    data_handler = DataHandler(data, cloud_config)
    prepared_data = data_handler.prepare_data()

    # Step 5: Create a distributed Stan model that can run on the Dask cluster
    distributed_model = DistributedStanModel(stan_model, dask_client, prepared_data)

    # Step 6: Return the prepared distributed model ready for fitting
    return distributed_model


# Optionally, any initialization code needed for the package can go here

# Make sure to handle imports that should be exposed to the user
__all__ = [
    'DaskClient',
    'DistributedStanModel',
    'StanModel',
    'CloudSetup',
    'DataHandler',
    'Configuration',
    'setup_model',
]
