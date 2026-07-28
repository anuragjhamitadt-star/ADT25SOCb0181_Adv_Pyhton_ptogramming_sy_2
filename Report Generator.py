# -------------------------------
# Decorator for Header and Footer
# -------------------------------

def report_format(function):
    def wrapper(self):
        print("=" * 40)
        print("        REPORT GENERATOR")
        print("=" * 40)

        function(self)

        print("=" * 40)
        print("          END OF REPORT")
        print("=" * 40)
    return wrapper


# -------------------------------
# Report Class
# -------------------------------

class Report:

    # Magic Method
    def __init__(self, title, sections):
        self.title = title
        self.sections = sections

    # Class Method
    @classmethod
    def sample_report(cls):
        title = "Student Performance Report"

        sections = [
            "Student Name : Rahul",
            "Marks : 89",
            "Grade : A"
        ]

        return cls(title, sections)

    # Decorator
    @report_format
    def display(self):

        print("Title :", self.title)
        print()

        for item in self.sections:
            print(item)

    # Magic Method
    def __str__(self):
        return f"Report Title : {self.title}"

    # Magic Method
    def __len__(self):
        return len(self.sections)


# -------------------------------
# Main Program
# -------------------------------

report = Report.sample_report()

print(report)

print("Total Sections :", len(report))

#print()

report.display()
