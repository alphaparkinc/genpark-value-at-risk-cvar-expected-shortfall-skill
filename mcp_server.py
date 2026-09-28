import sys, json
from client import RiskEngineVaRCVaR

risk = RiskEngineVaRCVaR()

def handle_jsonrpc(line):
    global risk
    try:
        req = json.loads(line)
        req_id = req.get("id")
        method = req.get("method")
        if method == "initialize":
            return {"jsonrpc": "2.0", "id": req_id, "result": {"protocolVersion": "2024-11-05", "serverInfo": {"name": "genpark-value-at-risk-cvar-expected-shortfall-skill", "version": "1.0.0"}, "capabilities": {"tools": {}}}}
        elif method == "tools/list":
            return {"jsonrpc": "2.0", "id": req_id, "result": {"tools": [
                {"name": "calculate_var", "description": "Compute VaR & CVaR.", "inputSchema": {"type": "object", "properties": {"returns": {"type": "array"}, "portfolio_value": {"type": "number"}, "alpha": {"type": "number"}}, "required": ["returns"]}},
                {"name": "benchmark_var_cvar_analysis", "description": "Run VaR benchmark.", "inputSchema": {"type": "object", "properties": {}}}
            ]}}
        elif method == "tools/call":
            params = req.get("params", {})
            tool = params.get("name")
            args = params.get("arguments", {})
            if tool == "calculate_var":
                res = risk.calculate_var_cvar(args.get("returns", []), args.get("portfolio_value", 1000000.0), args.get("alpha", 0.95))
            elif tool == "benchmark_var_cvar_analysis":
                res = risk.benchmark_var_cvar_analysis()
            else:
                return {"jsonrpc": "2.0", "id": req_id, "error": {"code": -32601, "message": "Method not found"}}
            return {"jsonrpc": "2.0", "id": req_id, "result": {"content": [{"type": "text", "text": json.dumps(res, indent=2)}]}}
        return {"jsonrpc": "2.0", "id": req_id, "result": {}}
    except Exception as e:
        return {"jsonrpc": "2.0", "id": None, "error": {"code": -32603, "message": str(e)}}

def main():
    for line in sys.stdin:
        if line.strip():
            print(json.dumps(handle_jsonrpc(line.strip())), flush=True)

if __name__ == "__main__":
    main()
