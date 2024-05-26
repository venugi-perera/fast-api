def individual_serial(todo) -> dict:
    return {
        'id': str(todo["_id"]),
        'REC_ID': todo.get("REC_ID"),
        'YEAR': todo.get("YEAR"),
        'MONTH': todo.get("MONTH"),
        'CONTRACT_NO': todo.get("CONTRACT_NO"),
        'LOANMASTER_ID': todo.get("LOANMASTER_ID"),
        'ME_USERNAME': todo.get("ME_USERNAME"),
        'ME_AD': todo.get("ME_AD"),
        'MONTH_START_STATUS': todo.get("MONTH_START_STATUS"),
        'MONTH_END_STATUS': todo.get("MONTH_END_STATUS"),
        'LOAN_EXPIRE_DATE': todo.get("LOAN_EXPIRE_DATE"),
        'LOAN_START_DATE': todo.get("LOAN_START_DATE"),
        'LOAN_AMOUNT': todo.get("LOAN_AMOUNT"),
        'PRODUCT_ID': todo.get("PRODUCT_ID"),
        'PRODUCT_NAME': todo.get("PRODUCT_NAME"),
        'LOAN_PRODUCT_ID': todo.get("LOAN_PRODUCT_ID"),
        'LOAN_PRODUCT_NAME': todo.get("LOAN_PRODUCT_NAME"),
        'MONTH_START_DPD_DATE': todo.get("MONTH_START_DPD_DATE"),
        'MONTH_START_DPD': todo.get("MONTH_START_DPD"),
        'MONTH_MAX_DPD': todo.get("MONTH_MAX_DPD"),
        'MONTH_END_DPD_DATE': todo.get("MONTH_END_DPD_DATE"),
        'MONTH_END_DPD': todo.get("MONTH_END_DPD"),
        'MONTH_START_ARR': todo.get("MONTH_START_ARR"),
        'MONTH_MAX_ARR': todo.get("MONTH_MAX_ARR"),
        'MONTH_END_ARR': todo.get("MONTH_END_ARR")
    }

def list_serial(todos) -> list:
    print(todos)
    return [individual_serial(todo) for todo in todos]
