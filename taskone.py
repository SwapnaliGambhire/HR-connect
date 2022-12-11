import csv


class HandleCSV:
    filename = "employees.csv"

    @classmethod
    def read_entire_csv(cls):
        with open(cls.filename, "r") as foo:
            return foo.readlines()

    @classmethod
    def read_csv_line_by_line(cls):
        with open(cls.filename) as bar:
            yield bar.readlines()

    @classmethod
    def read_csv_employees_details(cls):
        salary = {}
        with open(cls.filename, encoding="utf8") as bar:
            csv_reader = csv.DictReader(bar)
            for lines1 in csv_reader:
                if int(lines1["SALARY"]) > 9000:
                    first_name = lines1["FIRST_NAME"]
                    last_name = lines1["LAST_NAME"]
                    name = f"{first_name} {last_name}"
                    email = lines1["EMAIL"]
                    phone_number = lines1["PHONE_NUMBER"]
                    salary.update({"name": name})
                    salary.update({"email": email})
                    salary.update({"Phone_Number": phone_number}, )
                    print(salary)


csvfile = HandleCSV()

file = csvfile.read_entire_csv()
print("entire file details \n ", file)
print("#"*100)

csvfile1 = csvfile.read_csv_line_by_line()
print("line by line details")

for lines in csvfile1:
    print(lines)

print("###"*50,"\n")

print("Salary is Greater than 9000 Employees: \n ",)
csvfile.read_csv_employees_details()
