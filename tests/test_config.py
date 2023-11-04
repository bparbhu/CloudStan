from src.stan_dask_cloud.utils.config import Config

def test_config_defaults():
    config = Config()
    assert config.cloud_storage_path == 'path/to/default/storage', "Default storage path should be set."

# Add more tests to validate different aspects of your Config class
