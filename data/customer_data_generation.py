import csv
from faker import Faker
import datetime


def datagenerate(records, headers):
    fake = Faker('en_US')
    fake1 = Faker('en_GB')   # To generate phone numbers
    with open("wallabymart_customer_data.csv", 'wt') as csvFile:
        writer = csv.DictWriter(csvFile, fieldnames=headers)
        id_number = 1111
        tags = ['website', 'in-store', 'event']
        writer.writeheader()
        for i in range(records):
            customer_id = id_number
            id_number += 1
            full_name = fake.name()
            FLname = full_name.split(" ")
            Fname = FLname[0]
            Lname = FLname[1]
            domain_name = "@email.com"
            userId = Fname[0].lower() + Lname.lower() + domain_name

            writer.writerow({
                "Customer ID": customer_id,
                "Email": userId,
                "Prefix": fake.prefix(),
                "Name": full_name,
                "Birth Date": fake.date(pattern="%d-%m-%Y", end_datetime=datetime.date(2000, 1, 1)),
                "Phone Number": fake1.phone_number(),
                "Zip Code": fake.zipcode(),
                "City": fake.city(),
                "State": fake.state(),
                "Market Tag": tags[id_number % 3],
            })


if __name__ == '__main__':
    records = 1000
    headers = ['Customer ID', 'Email', 'Prefix', 'Name', 'Birth Date',
               'Phone Number', 'Zip Code', 'City', 'State', 'Market Tag']
    datagenerate(records, headers)
    print("Fake Customer CSV complete!")
