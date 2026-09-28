from typing import List, Dict, Any

class RiskEngineVaRCVaR:
    @staticmethod
    def calculate_var_cvar(returns: List[float], portfolio_value: float = 1000000.0, alpha: float = 0.95) -> Dict[str, Any]:
        if not returns:
            return {"error": "Returns cannot be empty"}
        sorted_ret = sorted(returns)
        cutoff_idx = int((1.0 - alpha) * len(sorted_ret))
        var_pct = -sorted_ret[cutoff_idx]
        tail_losses = [-r for r in sorted_ret[:cutoff_idx + 1]]
        cvar_pct = sum(tail_losses) / len(tail_losses) if tail_losses else var_pct
        return {
            "confidence_level": f"{int(alpha * 100)}%",
            "var_percentage": round(var_pct * 100, 3),
            "var_dollar_loss": round(var_pct * portfolio_value, 2),
            "cvar_expected_shortfall_pct": round(cvar_pct * 100, 3),
            "cvar_dollar_loss": round(cvar_pct * portfolio_value, 2)
        }

    def benchmark_var_cvar_analysis(self) -> Dict[str, Any]:
        sample_returns = [-0.035, -0.02, -0.015, -0.01, 0.005, 0.012, 0.025, -0.028, 0.003, -0.008, 0.018]
        return self.calculate_var_cvar(sample_returns, 1000000.0)
