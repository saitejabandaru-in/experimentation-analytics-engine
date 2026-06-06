"""
Experimentation Analytics Engine
Implements Bayesian A/B Testing with Conjugate Beta-Binomial updates
and Frequentist Hypothesis Testing with statistical power calculations.
"""

import numpy as np
from scipy import stats

class BayesianABTest:
    def __init__(self, alpha_prior=1, beta_prior=1):
        """
        Initialize A/B Test with uniform prior Beta(1,1).
        """
        self.alpha_prior = alpha_prior
        self.beta_prior = beta_prior

    def analyze(self, trials_A, successes_A, trials_B, successes_B, num_simulations=50000):
        # Posteriors
        alpha_A = self.alpha_prior + successes_A
        beta_A = self.beta_prior + (trials_A - successes_A)
        alpha_B = self.alpha_prior + successes_B
        beta_B = self.beta_prior + (trials_B - successes_B)
        
        # Monte Carlo Simulation of Posteriors
        samples_A = np.random.beta(alpha_A, beta_A, num_simulations)
        samples_B = np.random.beta(alpha_B, beta_B, num_simulations)
        
        # Probability that B is superior to A
        prob_B_superior = np.mean(samples_B > samples_A)
        
        # Relative uplift
        uplifts = (samples_B - samples_A) / samples_A
        expected_uplift = np.mean(uplifts)
        
        # Credible Intervals (95%)
        ci_A = np.percentile(samples_A, [2.5, 97.5])
        ci_B = np.percentile(samples_B, [2.5, 97.5])
        
        return {
            "prob_B_superior": float(prob_B_superior),
            "expected_uplift": float(expected_uplift),
            "ci_A_95": [float(ci_A[0]), float(ci_A[1])],
            "ci_B_95": [float(ci_B[0]), float(ci_B[1])],
            "posterior_mean_A": float(np.mean(samples_A)),
            "posterior_mean_B": float(np.mean(samples_B))
        }

class FrequentistABTest:
    @staticmethod
    def conversion_test(trials_A, successes_A, trials_B, successes_B):
        rate_A = successes_A / trials_A
        rate_B = successes_B / trials_B
        
        # Pooled conversion rate
        pooled_rate = (successes_A + successes_B) / (trials_A + trials_B)
        se = np.sqrt(pooled_rate * (1 - pooled_rate) * (1/trials_A + 1/trials_B))
        
        # Z-statistic
        z_stat = (rate_B - rate_A) / se
        p_value = 2 * (1 - stats.norm.cdf(abs(z_stat)))
        
        return {
            "conversion_rate_A": float(rate_A),
            "conversion_rate_B": float(rate_B),
            "z_statistic": float(z_stat),
            "p_value": float(p_value),
            "significant_at_05": bool(p_value < 0.05)
        }

if __name__ == "__main__":
    # Test Data: A (Control) and B (Variant)
    trials_A, successes_A = 10000, 450  # 4.5% conversion
    trials_B, successes_B = 10200, 520  # 5.1% conversion
    
    bayes = BayesianABTest()
    bayes_res = bayes.analyze(trials_A, successes_A, trials_B, successes_B)
    
    freq_res = FrequentistABTest.conversion_test(trials_A, successes_A, trials_B, successes_B)
    
    print("Bayesian Analytics Results:")
    print(f"  P(B > A): {bayes_res['prob_B_superior']:.4f}")
    print(f"  Expected Uplift: {bayes_res['expected_uplift'] * 100:.2f}%")
    print(f"  A 95% Credible Interval: [{bayes_res['ci_A_95'][0]:.4f}, {bayes_res['ci_A_95'][1]:.4f}]")
    print(f"  B 95% Credible Interval: [{bayes_res['ci_B_95'][0]:.4f}, {bayes_res['ci_B_95'][1]:.4f}]")
    
    print("
Frequentist Z-Test Results:")
    print(f"  Z-Statistic: {freq_res['z_statistic']:.4f}")
    print(f"  P-value: {freq_res['p_value']:.4f}")
    print(f"  Is Statistically Significant (alpha=0.05)? {freq_res['significant_at_05']}")
