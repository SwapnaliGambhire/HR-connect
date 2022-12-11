import csv
from utils.csv import add_value


class HandleCSV:
    filename = "employees.csv"

    @classmethod
    def read_entire_csv(cls):
        with open(cls.filename, "r") as foo:
            print(foo.readlines())

    @classmethod
    def read_csv_line_by_line(cls):
        with open(cls.filename) as bar:
            yield bar.readlines()

    @classmethod
    def read_csv_employees_hire(cls):
        hire = {}

        with open(cls.filename, encoding="utf8") as bar:
            csv_reader = csv.DictReader(bar)

            for lines in csv_reader:
                if int(lines["DEPARTMENT_ID"]) > 30 \
                        and int(lines["SALARY"]) > 4200:

                    hire_date = lines["HIRE_DATE"]
                    first_name = lines["FIRST_NAME"]
                    last_name = lines["LAST_NAME"]
                    name = f"{first_name} {last_name}"

                    add_value(hire, hire_date, name)
        print(hire)


hires = HandleCSV()

print("\nHIRE DATE of employee who is department is within range 30"
      "to 110 AND who is salary is > 4200.\n")
hires.read_csv_employees_hire()