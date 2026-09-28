from client import RiskEngineVaRCVaR

def run_example():
    print("=== GenPark VaR & CVaR Risk Engine Example ===")
    engine = RiskEngineVaRCVaR()
    print("Risk Analytics:", engine.benchmark_var_cvar_analysis())

if __name__ == "__main__":
    run_example()
