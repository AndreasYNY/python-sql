from fastapi import APIRouter
from util.connection import conn
from faker import Faker
from pydantic import BaseModel
from datetime import date

import random

router = APIRouter(prefix='/employees')
fake = Faker()

# generate some random data from faker
@router.get("/generate/{generate_number}")
async def generate(generate_number: int):
    connection = conn()
    with connection:
        with connection.cursor() as cursor:
            try:
                for data in range(generate_number):
                    sql = "INSERT into `Employees` (`Name`, `Age`, `Address`, `Gender`, `DOB`, `Email`, `Role`, `pet_owned`, Country) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
                    cursor.execute(sql, (fake.name(), random.randint(18, 58), fake.address(), random.choice(["M", "F"]), fake.date(), fake.ascii_safe_email(), fake.job(), random.randint(0, 10), fake.country() ))
                    employee_id = cursor.lastrowid  # Get the ID of the inserted employee
                    sql1 = "INSERT into `bank_details` (Bank_country, Bank_Number, employee_id) VALUES (%s, %s, %s)"
                    cursor.execute(sql1, (fake.bank_country(), fake.aba(), employee_id))
            except Exception as e:
                return e
        
        with connection.cursor() as cursor:
            try:
                sql = "SELECT * from `Employees`"
                cursor.execute(sql)
                result = cursor.fetchall()
                return {"Employees": [result[0] for _ in result[0]]}
            except Exception as e:
                return e
            
@router.get("/getAll")
async def getAll():
    connection = conn()
    with connection:
        with connection.cursor() as cursor:
            try:
                sql = "SELECT * from `Employees`"
                cursor.execute(sql)
                result = cursor.fetchall()
                return {"Employees": [result[0] for _ in result[0]]}
            except Exception as e:
                return e
  
@router.get("/getById/{id}")
async def getByID(id):
    connection = conn()
    try:
        with connection:
            with connection.cursor() as cursor:
                sql = "SELECT * FROM `Employees` where id=%s"
                cursor.execute(sql, ({id}))
                result = cursor.fetchone()
                return result
    except Exception as e:
        return e
        
@router.get("/averageAge")
async def averageAge():
    connection = conn()
    try:
        with connection:
            with connection.cursor() as cursor:
                sql="SELECT AVG(Age) FROM Employees"
                cursor.execute(sql)
                result = cursor.fetchone()
                return result
    except Exception as e:
        return e
        
@router.get("/countEmployees")
async def countEmployees():
    connection = conn()
    try:
        with connection:
            with connection.cursor() as cursor:
                sql="SELECT COUNT(*) FROM Employees"
                cursor.execute(sql)
                result = cursor.fetchone()
                return result
    except Exception as e:
        return e
        
@router.get("/getYoungest")
async def getYoungest():
    connection = conn()
    try:
        with connection:
            with connection.cursor() as cursor:
                # for demonstration purposes
                sql="SELECT MIN(Age) FROM Employees"
                cursor.execute(sql)
                result = cursor.fetchone()
                return result
    except Exception as e:
        return e
    
@router.get("/getOldest")
async def getOldest():
    connection = conn()
    try:
        with connection:
            with connection.cursor() as cursor:
                # for demonstration purposes
                sql="SELECT MAX(Age) FROM Employees"
                cursor.execute(sql)
                result = cursor.fetchone()
                return result
    except Exception as e:
        return e
        
@router.get("/getTotalPets")
async def getYoungest():
    connection = conn()
    try:
        with connection:
            with connection.cursor() as cursor:
                # for demonstration purposes
                sql="SELECT SUM(pet_owned) FROM Employees"
                cursor.execute(sql)
                result = cursor.fetchone()
                return result
    except Exception as e:
        return e
        
@router.get("/search/{search}")
async def search(search):
    connection = conn()
    try:
        with connection:
            with connection.cursor() as cursor:
                sql="SELECT * FROM Employees WHERE Name REGEXP %s OR Address REGEXP %s OR Email REGEXP %s"
                cursor.execute(sql, ({search}, {search} , {search}))
                result = cursor.fetchall()
                return result
    except Exception as e:
        return e
    
@router.get("/getBankDetails/{id}")
async def bankDetails(id):
    connection = conn()
    try:
        with connection:
            with connection.cursor() as cursor:
                sql="SELECT * FROM bank_details LEFT JOIN Employees ON Employees.id = bank_details.employee_id WHERE Employees.id=%s"
                cursor.execute(sql, ({id}))
                result = cursor.fetchone()
                return result
    except Exception as e:
        return e

# im not making another model file
class Employee(BaseModel):
    Name: str
    Age: int
    Address: str
    Gender: str
    DOB: date
    Email: str
    Role: str
    pet_owned: int
    Country: str
    
class BankDetails(BaseModel):
    Bank_country: str
    Bank_Number: int
    employee_id: int
    
@router.post("/addEmployee")
async def addEmployee(employee: Employee):
    connection = conn()
    try:
        with connection:
            with connection.cursor() as cursor:
                sql = "INSERT into `Employees` (`Name`, `Age`, `Address`, `Gender`, `DOB`, `Email`, `Role`, `pet_owned`, Country) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
                cursor.execute(sql, (employee.Name, employee.Age, employee.Address, employee.Gender, employee.DOB, employee.Email, employee.Role, employee.pet_owned, employee.Country))
                return "Employee added"
    except Exception as e:
        return e

@router.post("/addBankDetails")
async def addBankDetails(bank_details: BankDetails):
    connection = conn()
    try:
        with connection:
            with connection.cursor() as cursor:
                sql = "INSERT into `bank_details` (Bank_country, Bank_Number, employee_id) VALUES (%s, %s, %s)"
                cursor.execute(sql, (bank_details.Bank_country, bank_details.Bank_Number, bank_details.employee_id))
                return "Bank Details added"
    except Exception as e:
        return e
    
@router.delete("/deleteEmployee/{id}")
async def deleteEmployee(id):
    connection = conn()
    try:
        with connection:
            with connection.cursor() as cursor:
                sql = "DELETE FROM Employees WHERE id = %s"
                cursor.execute(sql, ({id}))
                return "Employee deleted"
    except Exception as e:
        return e
    
@router.delete("/deleteBankDetails/{id}")
async def deleteBankDetails(id):
    connection = conn()
    try:
        with connection:
            with connection.cursor() as cursor:
                sql = "DELETE FROM bank_details WHERE id = %s"
                cursor.execute(sql, ({id}))
                return "Bank Details deleted"
    except Exception as e:
        return e
