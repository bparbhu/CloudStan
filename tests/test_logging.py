from stan_dask_cloud.utils import setup_logger

def test_logger_setup():
    logger = setup_logger('test_logger')
    assert logger.name == 'test_logger', "Logger should be correctly named."
    assert logger.level == 20, "Default logging level should be INFO (20)."

# Add more tests to validate different configurations and logging outputs
