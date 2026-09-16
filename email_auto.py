import csv


class EmailAutomation:

    def __init__(self):
        self.results = []

    @staticmethod
    def read_students(filename):
        records = []

        try:
            with open(filename, "r", newline="", encoding="utf-8") as file:
                csv_reader = csv.DictReader(file)

                for row in csv_reader:
                    records.append(row)

            return records

        except FileNotFoundError:
            print("Error: students.csv file not found.")
            return []

    @staticmethod
    def is_valid_email(email_address):
        return "@" in email_address and "." in email_address

    @staticmethod
    def create_email(student_name, receiver_email):

        message = f"""
-----------------------------------
To: {receiver_email}
Subject: Python Assignment Reminder
-----------------------------------

Hello {student_name},

This is a personalized email from our
Python Email Automation System.

This is a reminder regarding your Python
assignment. Please complete and submit
your assignment on time.

Thank you,
Python Automation System
-----------------------------------
"""

        return message

    def send_emails(self, records):

        print("\nStarting email automation...\n")

        for record in records:

            student_name = record["name"]
            receiver_email = record["email"]

            if not self.is_valid_email(receiver_email):

                print(
                    f"Invalid email: {receiver_email}"
                )

                self.results.append({
                    "name": student_name,
                    "email": receiver_email,
                    "status": "Invalid"
                })

                continue

            email_message = self.create_email(
                student_name,
                receiver_email
            )

            print(email_message)

            print(
                f"✓ Email sent successfully to "
                f"{student_name}"
            )

            self.results.append({
                "name": student_name,
                "email": receiver_email,
                "status": "Sent"
            })

    def create_report(self, output_filename):

        with open(
                output_filename,
                "w",
                newline="",
                encoding="utf-8"
        ) as report_file:

            column_names = [
                "name",
                "email",
                "status"
            ]

            csv_writer = csv.DictWriter(
                report_file,
                fieldnames=column_names
            )

            csv_writer.writeheader()
            csv_writer.writerows(self.results)

        print(
            f"\n✓ Report created: {output_filename}"
        )


# ==========================================
# MAIN PROGRAM
# ==========================================

print("===================================")
print("   SMART EMAIL AUTOMATION SYSTEM")
print("===================================")

email_automation = EmailAutomation()

records_from_csv = email_automation.read_students(
    "students.csv"
)

print(
    f"\nNumber of students found: "
    f"{len(records_from_csv)}"
)

if records_from_csv:

    email_automation.send_emails(
        records_from_csv
    )

    email_automation.create_report(
        "email_report.csv"
    )

else:

    print("\nNo student data found.")

print("\n===================================")
print("       PROGRAM COMPLETED")
print("===================================")