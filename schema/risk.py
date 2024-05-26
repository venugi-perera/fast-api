def risk_serial(todo) -> dict:
    return {
        'id': str(todo["_id"]),
    'KEPT_RATE': todo.get("KEPT_RATE"),
    'NRPC_RATE': todo.get("NRPC_RATE"),
    'MONTH_END_DPD':  todo.get("MONTH_END_DPD"),
    'Total_Score': todo.get("Total_Score"),
    'Risk_Level': todo.get("Risk_Level"),
    }

def risk_list_serial(todos) -> list:
    print(todos)
    return [risk_serial(todo) for todo in todos]
