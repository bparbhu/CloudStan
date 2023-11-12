import dask
from ray.util.dask import ray_dask_get
import cmdstanpy

# Ensure Ray is initialized in your environment
import ray
ray.init()

def dask_on_ray_wrapper(func, *args, **kwargs):
    """
    Generic wrapper for cmdstanpy functions to be used with dask_on_ray.
    """
    @dask.delayed
    def delayed_func(*args, **kwargs):
        return func(*args, **kwargs)

    return delayed_func(*args, **kwargs)

# Specific function wrappers

def ray_sample(model, data, chains=4, **kwargs):
    return dask_on_ray_wrapper(cmdstanpy.CmdStanModel.sample, model, data, chains, **kwargs)

def ray_optimize(model, data, **kwargs):
    return dask_on_ray_wrapper(cmdstanpy.CmdStanModel.optimize, model, data, **kwargs)

def ray_diagnose(csv_files, **kwargs):
    return dask_on_ray_wrapper(cmdstanpy.diagnose, csv_files, **kwargs)

# CmdStanMCMC Wrapper
def ray_cmdstanmcmc_summary(mcmc_result, **kwargs):
    return dask_on_ray_wrapper(mcmc_result.summary, **kwargs)

def ray_cmdstanmcmc_diagnose(mcmc_result, **kwargs):
    return dask_on_ray_wrapper(mcmc_result.diagnose, **kwargs)

# CmdStanMLE Wrapper
def ray_cmdstanmle_summary(mle_result, **kwargs):
    return dask_on_ray_wrapper(mle_result.summary, **kwargs)

# CmdStanGQ Wrapper
def ray_cmdstangq_summary(gq_result, **kwargs):
    return dask_on_ray_wrapper(gq_result.summary, **kwargs)

# CmdStanVB Wrapper
def ray_cmdstanvb_summary(vb_result, **kwargs):
    return dask_on_ray_wrapper(vb_result.summary, **kwargs)

# RunSet Wrapper
def ray_runset_summary(runset, **kwargs):
    return dask_on_ray_wrapper(runset.summary, **kwargs)

