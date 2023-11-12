from dask import delayed
from cmdstanpy import CmdStanModel, CmdStanMCMC, CmdStanGQ, CmdStanMLE, CmdStanVB
from cmdstanpy.stanfit.runset import RunSet


@delayed
def delayed_sample(stan_file, data=None, chains=4, parallel_chains=None, iter_warmup=1000,
                   iter_sampling=1000, **kwargs):
    model = CmdStanModel(stan_file=stan_file)
    fit = model.sample(data=data, chains=chains, parallel_chains=parallel_chains, iter_warmup=iter_warmup,
                       iter_sampling=iter_sampling, **kwargs)
    return fit

@delayed
def delayed_optimize(stan_file, data=None, algorithm='LBFGS', init_alpha=0.001, iter=2000, **kwargs):
    model = CmdStanModel(stan_file=stan_file)
    optimized = model.optimize(data=data, algorithm=algorithm, init_alpha=init_alpha, iter=iter, **kwargs)
    return optimized


@delayed
def delayed_variational(stan_file, data=None, algorithm='meanfield', iter=10000, grad_samples=1,
                        elbo_samples=100, eta=1.0, adapt_engaged=True, adapt_iter=50, **kwargs):
    model = CmdStanModel(stan_file=stan_file)
    variational_fit = model.variational(data=data, algorithm=algorithm, iter=iter,
                                        grad_samples=grad_samples, elbo_samples=elbo_samples,
                                        eta=eta, adapt_engaged=adapt_engaged, adapt_iter=adapt_iter, **kwargs)
    return variational_fit


@delayed
def delayed_cmdstanmcmc(*args, **kwargs):
    return CmdStanMCMC(*args, **kwargs)



@delayed
def delayed_cmdstanmle(*args, **kwargs):
    return CmdStanMLE(*args, **kwargs)



@delayed
def delayed_cmdstangq(*args, **kwargs):
    return CmdStanGQ(*args, **kwargs)


@delayed
def delayed_cmdstanvb(*args, **kwargs):
    return CmdStanVB(*args, **kwargs)



@delayed
def delayed_runset(*args, **kwargs):
    return RunSet(*args, **kwargs)
