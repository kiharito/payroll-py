from datetime import date
from enum import StrEnum
from typing import Annotated, Literal

from pydantic import BaseModel, Field


class PaymentType(StrEnum):
    HOURLY = "hourly"
    SALARIED = "salaried"
    COMMISSIONED = "commissioned"


class CreateEmployeeParamsBase(BaseModel):
    id: str
    name: str
    address: str


class CreateHourlyEmployeeParams(CreateEmployeeParamsBase):
    payment_type: Literal[PaymentType.HOURLY] = PaymentType.HOURLY
    hourly_rate: int


class CreateSalariedEmployeeParams(CreateEmployeeParamsBase):
    payment_type: Literal[PaymentType.SALARIED] = PaymentType.SALARIED
    monthly_salary: int


class CreateCommissionedEmployeeParams(CreateEmployeeParamsBase):
    payment_type: Literal[PaymentType.COMMISSIONED] = PaymentType.COMMISSIONED
    monthly_salary: int
    commission_rate: int


CreateEmployeeParams = Annotated[
    CreateHourlyEmployeeParams
    | CreateSalariedEmployeeParams
    | CreateCommissionedEmployeeParams,
    Field(discriminator="payment_type"),
]


class CreateTimeCardParams(BaseModel):
    date: date
    hours: int


class CreateSalesReceiptParams(BaseModel):
    date: date
    amount: int


class CreateServiceChargeParams(BaseModel):
    amount: int


class EditEmployeeType(StrEnum):
    NAME = "name"
    ADDRESS = "address"
    HOURLY = "hourly"
    SALARIED = "salaried"
    COMMISSIONED = "commissioned"
    HOLD = "hold"
    DIRECT = "direct"
    MAIL = "mail"
    MEMBER = "member"
    NO_MEMBER = "no_member"


class EditEmployeeNameParams(BaseModel):
    type: Literal[EditEmployeeType.NAME] = EditEmployeeType.NAME
    name: str


class EditEmployeeAddressParams(BaseModel):
    type: Literal[EditEmployeeType.ADDRESS] = EditEmployeeType.ADDRESS
    address: str


class EditEmployeeHourlyParams(BaseModel):
    type: Literal[EditEmployeeType.HOURLY] = EditEmployeeType.HOURLY
    hourly_rate: int


class EditEmployeeSalariedParams(BaseModel):
    type: Literal[EditEmployeeType.SALARIED] = EditEmployeeType.SALARIED
    salary: int


class EditEmployeeCommissionedParams(BaseModel):
    type: Literal[EditEmployeeType.COMMISSIONED] = EditEmployeeType.COMMISSIONED
    salary: int
    rate: int


class EditEmployeeHoldParams(BaseModel):
    type: Literal[EditEmployeeType.HOLD] = EditEmployeeType.HOLD


class EditEmployeeDirectParams(BaseModel):
    type: Literal[EditEmployeeType.DIRECT] = EditEmployeeType.DIRECT
    bank: str
    account: str


class EditEmployeeMailParams(BaseModel):
    type: Literal[EditEmployeeType.MAIL] = EditEmployeeType.MAIL
    address: str


class EditEmployeeMemberParams(BaseModel):
    type: Literal[EditEmployeeType.MEMBER] = EditEmployeeType.MEMBER
    member_id: str
    rate: int


class EditEmployeeNoMemberParams(BaseModel):
    type: Literal[EditEmployeeType.NO_MEMBER] = EditEmployeeType.NO_MEMBER


EditEmployeeParams = Annotated[
    EditEmployeeNameParams
    | EditEmployeeAddressParams
    | EditEmployeeHourlyParams
    | EditEmployeeSalariedParams
    | EditEmployeeCommissionedParams
    | EditEmployeeHoldParams
    | EditEmployeeDirectParams
    | EditEmployeeMailParams
    | EditEmployeeMemberParams
    | EditEmployeeNoMemberParams,
    Field(discriminator="type"),
]


class ExecPeymentParams(BaseModel):
    date: date
