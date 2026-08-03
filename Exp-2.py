#Experiment 2
#Advanced Class Concepts – Decorators and Magic methods

def bold_text(func):
    def wrapper(report):
        return "**" + func(report) + "**"
    return wrapper

class Report:
    templates = {}  

    def __init__(self, title, content):
        self.title = title
        self.content = content

    @classmethod
    def add_template(cls, name, func):
        cls.templates[name] = func

    @classmethod
    def retrieve_template(cls, name):
        return cls.templates.get(name)

    def __call__(self, template_name):
        template = Report.retrieve_template(template_name)
        if template:
            return template(self)
        else:
            return "Template not found"

    def __str__(self):
        return f"Title: {self.title}\nContent: {self.content}"

def simple_template(report):
    return f"Title: {report.title}\nContent: {report.content}"

@bold_text
def fancy_template(report):
    return f"Title: {report.title}\nContent: {report.content}"

def main():

    Report.add_template("simple", simple_template)
    Report.add_template("fancy", fancy_template)

    my_report = Report("Montly Sales Report", "Growth increased by 15%.")

    print("Simple Report:")
    print(my_report("simple"))

    print("\nFancy Report:")
    print(my_report("fancy"))

if __name__ == "__main__":
    main()
