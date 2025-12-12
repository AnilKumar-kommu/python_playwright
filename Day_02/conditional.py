#conditional statements in python
# def conditional_statements():
#     x = 10
#     y = 20
#
#     # if statement
#     if x < y:
#         print(f"{x} is less than {y}")
#
#     # if-else statement
#     if x > y:
#         print(f"{x} is greater than {y}")
#     else:
#         print(f"{x} is not greater than {y}")
#
#     # if-elif-else statement
#     if x == y:
#         print(f"{x} is equal to {y}")
#     elif x < y:
#         print(f"{x} is less than {y}")
#     else:
#         print(f"{x} is greater than {y}")
# conditional_statements()

#nested if statements
# def nested_if_statements():
#     a = 15
#     b = 25
#     c = 35
#
#     if a < b:
#         if b < c:
#             print(f"{a} is less than {b} and {b} is less than {c}")
#         else:
#             print(f"{a} is less than {b} but {b} is not less than {c}")
#     else:
#         print(f"{a} is not less than {b}")
# nested_if_statements()

#conditional statements with logical operators
def conditional_with_logical_operators():
    p = 30
    q = 40
    r = 50

    # using 'and' operator
    if p < q and q < r:
        print(f"{p} is less than {q} and {q} is less than {r}")

    # using 'or' operator
    if p > q or q < r:
        print(f"Either {p} is greater than {q} or {q} is less than {r}")

    # using 'not' operator
    if not (p > r):
        print(f"{p} is not greater than {r}")
# conditional_with_with realtime porjects
conditional_with_logical_operators()
#conditional_with_logical_operators()
# Example: User Authentication
def authenticate_user(username, password):
    valid_username = "admin"
    valid_password = "password123"

    if username == valid_username and password == valid_password:
        return "Access Granted"
    else:
        return "Access Denied"
# print(authenticate_user("admin", "password123"))
# print(authenticate_user("user", "pass"))
# Example: Age Verification
def verify_age(age):
    if age < 0:
        return "Invalid age"
    elif age < 18:
        return "Minor"
    elif age >= 18 and age < 65:
        return "Adult"
    else:
        return "Senior Citizen"
# print(verify_age(15))
# print(verify_age(30))
# print(verify_age(70))
# print(verify_age(-5))
# Example: Grade Classification
def classify_grade(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"
# print(classify_grade(95))
# print(classify_grade(85))
# print(classify_grade(75))
# print(classify_grade(65))
# print(classify_grade(50))
# print(classify_grade(110))
# Example: Traffic Light System
def traffic_light_action(color):
    if color == "red":
        return "Stop"
    elif color == "yellow":
        return "Caution"
    elif color == "green":
        return "Go"
    else:
        return "Invalid color"
# print(traffic_light_action("red"))
# print(traffic_light_action("yellow"))
# print(traffic_light_action("green"))
# print(traffic_light_action("blue"))
# Example: Discount Calculation
def calculate_discount(price, is_member):
    if is_member:
        if price > 100:
            discount = 0.20
        else:
            discount = 0.10
    else:
        if price > 100:
            discount = 0.10
        else:
            discount = 0.05

    final_price = price - (price * discount)
    return final_price
# print(calculate_discount(150, True))
# print(calculate_discount(80, True))
# print(calculate_discount(150, False))
# print(calculate_discount(80, False))
# Example: Loan Eligibility
def check_loan_eligibility(age, income):
    if age >= 18:
        if income >= 30000:
            return "Eligible for Loan"
        else:
            return "Not Eligible for Loan: Insufficient Income"
    else:
        return "Not Eligible for Loan: Underage"
# print(check_loan_eligibility(25, 40000))
# print(check_loan_eligibility(17, 40000))
# print(check_loan_eligibility(25, 25000))
# print(check_loan_eligibility(16, 20000))
# Example: Event Ticket Pricing
def ticket_price(age, is_weekend):
    if is_weekend:
        if age < 12:
            return 8.00  # Child weekend price
        elif age >= 12 and age < 60:
            return 12.00  # Adult weekend price
        else:
            return 10.00  # Senior weekend price
    else:
        if age < 12:
            return 5.00  # Child weekday price
        elif age >= 12 and age < 60:
            return 10.00  # Adult weekday price
        else:
            return 7.00  # Senior weekday price
# print(ticket_price(10, True))
# print(ticket_price(30, False))
# print(ticket_price(65, True))
# print(ticket_price(8, False))
# Example: Shipping Cost Calculation
def calculate_shipping_cost(weight, is_expedited):
    if is_expedited:
        if weight <= 5:
            return 15.00  # Expedited cost for <= 5kg
        else:
            return 25.00  # Expedited cost for > 5kg
    else:
        if weight <= 5:
            return 5.00  # Standard cost for <= 5kg
        else:
            return 10.00  # Standard cost for > 5kg
# print(calculate_shipping_cost(3, True))
# print(calculate_shipping_cost(7, False))
# print(calculate_shipping_cost(4, False))
# print(calculate_shipping_cost(6, True))
# Example: Movie Rating System
def movie_rating(age):
    if age < 0:
        return "Invalid age"
    elif age < 13:
        return "Rated G"
    elif age >= 13 and age < 17:
        return "Rated PG-13"
    else:
        return "Rated R"
# print(movie_rating(10))
# print(movie_rating(15))
# print(movie_rating(20))
# print(movie_rating(-3))
# Example: Fitness Level Assessment
def assess_fitness_level(age, exercise_hours_per_week):
    if age < 0:
        return "Invalid age"
    elif exercise_hours_per_week >= 5:
        return "Excellent Fitness Level"
    elif exercise_hours_per_week >= 3:
        return "Good Fitness Level"
    elif exercise_hours_per_week >= 1:
        return "Average Fitness Level"
    else:
        return "Poor Fitness Level"
# print(assess_fitness_level(25, 6))
# print(assess_fitness_level(30, 2))
# print(assess_fitness_level(40, 0))
# print(assess_fitness_level(-5, 3))
# Example: Weather Advisory
def weather_advisory(temperature, is_raining):
    if is_raining:
        if temperature < 15:
            return "Carry an umbrella and wear warm clothes"
        else:
            return "Carry an umbrella"
    else:
        if temperature < 15:
            return "Wear warm clothes"
        else:
            return "Enjoy your day"
# print(weather_advisory(10, True))
# print(weather_advisory(20, False))
# print(weather_advisory(12, False))
# print(weather_advisory(25, True))
# Example: Online Shopping Cart Discount
def shopping_cart_discount(total_amount, is_first_time_buyer):
    if is_first_time_buyer:
        if total_amount > 200:
            discount = 0.25
        else:
            discount = 0.15
    else:
        if total_amount > 200:
            discount = 0.10
        else:
            discount = 0.05

    final_amount = total_amount - (total_amount * discount)
    return final_amount
# print(shopping_cart_discount(250, True))
# print(shopping_cart_discount(150, True))
# print(shopping_cart_discount(250, False))
# print(shopping_cart_discount(150, False))

# Example: Restaurant Bill Tip Calculation
def calculate_tip(bill_amount, service_quality):
    if service_quality == "excellent":
        tip_percentage = 0.20
    elif service_quality == "good":
        tip_percentage = 0.15
    elif service_quality == "average":
        tip_percentage = 0.10
    else:
        tip_percentage = 0.05

    tip_amount = bill_amount * tip_percentage
    total_amount = bill_amount + tip_amount
    return total_amount
# print(calculate_tip(100, "excellent"))
# print(calculate_tip(100, "good"))
# print(calculate_tip(100, "average"))
# print(calculate_tip(100, "poor"))
# Example: Gym Membership Eligibility
def gym_membership_eligibility(age, bmi):
    if age >= 16:
        if bmi < 25:
            return "Eligible for Gym Membership"
        else:
            return "Not Eligible: BMI too high"
    else:
        return "Not Eligible: Underage"
print(gym_membership_eligibility(20, 22))
print(gym_membership_eligibility(15, 20))
print(gym_membership_eligibility(25, 28))
# Example: College Admission Criteria
def college_admission_criteria(marks, extracurriculars):
    if marks >= 85:
        if extracurriculars >= 3:
            return "Admitted with Scholarship"
        else:
            return "Admitted"
    elif marks >= 70:
        return "Admitted on Probation"
    else:
        return "Not Admitted"
# print(college_admission_criteria(90, 4))
# print(college_admission_criteria(80, 2))
# print(college_admission_criteria(65, 5))
# Example: Car Rental Eligibility
def car_rental_eligibility(age, has_license):
    if age >= 21:
        if has_license:
            return "Eligible to Rent a Car"
        else:
            return "Not Eligible: No Driver's License"
    else:
        return "Not Eligible: Underage"
# print(car_rental_eligibility(25, True))
# print(car_rental_eligibility(19, True))
# print(car_rental_eligibility(30, False))
# Example: Health Insurance Premium Calculation
def health_insurance_premium(age, smoker):
    if age < 18:
        premium = 100.00
    elif age >= 18 and age < 45:
        premium = 200.00
    elif age >= 45 and age < 65:
        premium = 300.00
    else:
        premium = 400.00

    if smoker:
        premium += 150.00

    return premium
# print(health_insurance_premium(25, False))
# print(health_insurance_premium(50, True))
# print(health_insurance_premium(70, False))
# Example: Vacation Eligibility
def vacation_eligibility(years_of_service, has_pending_tasks):
    if years_of_service >= 1:
        if not has_pending_tasks:
            return "Eligible for Vacation"
        else:
            return "Not Eligible: Pending Tasks"
    else:
        return "Not Eligible: Insufficient Service Years"
# print(vacation_eligibility(2, False))
# print(vacation_eligibility(0.5, False))
# print(vacation_eligibility(3, True))

# Example: Smartphone Purchase Decision
def smartphone_purchase_decision(budget, needs_high_end_features):
    if budget >= 800:
        if needs_high_end_features:
            return "Purchase High-End Smartphone"
        else:
            return "Purchase Mid-Range Smartphone"
    elif budget >= 400:
        return "Purchase Budget Smartphone"
    else:
        return "Insufficient Budget for Smartphone"
# print(smartphone_purchase_decision(900, True))
# print(smartphone_purchase_decision(600, False))
# print(smartphone_purchase_decision(300, True))
# Example: Home Loan Interest Rate Calculation
def home_loan_interest_rate(credit_score, down_payment):
    if credit_score >= 750:
        if down_payment >= 20:
            return 3.5  # Low interest rate
        else:
            return 4.0  # Standard interest rate
    elif credit_score >= 600:
        return 5.0  # Higher interest rate
    else:
        return 6.5  # Highest interest rate
# print(home_loan_interest_rate(780, 25))
# print(home_loan_interest_rate(720, 15))
# print(home_loan_interest_rate(580, 10))

