class PersonalData:
    def __init__(self, name, age, gender, birthdate, fb, ig, twt, linkedin):
        self.name = name
        self.age = age 
        self.gender = gender
        self.birthdate = birthdate 
        self.fb = fb
        self.ig = ig
        self.twt = twt
        self.linkedin = linkedin
        

class LoginData:
    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email

class EmployeeData:
    def __init__(self, salary, tax, occupation, title):
        self.monthly_salary = salary - (salary * (tax / 100))