from fastapi import FastAPI

from app.schema import (
    CreateEmployeeParams,
    CreateSalesReceiptParams,
    CreateServiceChargeParams,
    CreateTimeCardParams,
    EditEmployeeParams,
    ExecPeymentParams,
)

app = FastAPI()


@app.get("/")
def root():
    return {"Hello": "World"}


@app.post(
    "/employees",
)
async def create_employee(params: CreateEmployeeParams):
    pass


@app.delete(
    "/employees/{employee_id}",
)
async def delete_employee(employee_id: str):
    pass


@app.post(
    "/employees/{employee_id}/time_cards",
)
async def create_time_card(employee_id: str, params: CreateTimeCardParams):
    pass


@app.post(
    "/employees/{employee_id}/sales_receipts",
)
async def create_sales_receipt(employee_id: str, params: CreateSalesReceiptParams):
    pass


@app.post(
    "/members/{member_id}/service_charges",
)
async def create_service_charge(member_id: str, params: CreateServiceChargeParams):
    pass


@app.patch(
    "/employees/{employee_id}",
)
async def edit_employee(employee_id: str, params: EditEmployeeParams):
    pass


@app.post(
    "/paydays",
)
async def exec_payment(params: ExecPeymentParams):
    pass
