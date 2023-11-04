import pytest

# Example of a fixture that might be used across tests
@pytest.fixture
def sample_stan_model():
    return "data { int<lower=0> N; vector[N] y; } parameters { real mu; } model { y ~ normal(mu,1); }"
