# T'Keyah <Your Last Name>
# Date: <MM/DD/YYYY>
# Assignment: P3HW2_Salary_LastnameFirstname.py
# Brief: Prompt for employee name, hours worked, and pay rate. Compute overtime,
#        regular pay, and gross pay. Display a formatted pay summary.

"""
PSEUDOCODE
1. Set constants:
   - OT_THRESHOLD = 40
   - OT_RATE = 1.5

2. Prompt user:
   - employee_name (string)
   - hours_worked (float)
   - pay_rate (float)

3. Determine overtime:
   - if hours_worked > OT_THRESHOLD:
       overtime_hours = hours_worked - OT_THRESHOLD
       regular_hours  = OT_THRESHOLD
     else:
       overtime_hours = 0
       regular_hours  = hours_worked

4. Compute pay components:
   - regular_pay  = regular_hours * pay_rate
   - overtime_pay = overtime_hours * pay_rate * OT_RATE
   - gross_pay    = regular_pay + overtime_pay

5. Display results (with two decimal places for money and hours):
   - Employee name
   - Pay rate
   - Hours worked
   - Overtime hours
   - Overtime pay
   - Regular pay
   - Gross pay
"""

# ---------- Constants ----------
OT_THRESHOLD = 40.0
OT_RATE = 1.5

# ---------- Inputs ----------
employee_name = input("Enter employee name: ").strip()
hours_worked = float(input("Enter number of hours worked this week: "))
pay_rate = float(input("Enter employee's hourly pay rate: "))

# ---------- Overtime Logic ----------
if hours_worked > OT_THRESHOLD:
    overtime_hours = hours_worked - OT_THRESHOLD
    regular_hours = OT_THRESHOLD
else:
    overtime_hours = 0.0
    regular_hours = hours_worked

# ---------- Calculations ----------
regular_pay = regular_hours * pay_rate
overtime_pay = overtime_hours * pay_rate * OT_RATE
gross_pay = regular_pay + overtime_pay

# ---------- Output ----------
print("\n" + "-" * 50)
print(f"Employee Name  : {employee_name}")
print(f"Pay Rate       : ${pay_rate:,.2f}")
print(f"Hours Worked   : {hours_worked:,.2f}")
print(f"Overtime Hours : {overtime_hours:,.2f}")
print(f"Overtime Pay   : ${overtime_pay:,.2f}")
print(f"Regular Pay    : ${regular_pay:,.2f}")
print("-" * 50)
print(f"Gross Pay      : ${gross_pay:,.2f}")
print("-" * 50)
