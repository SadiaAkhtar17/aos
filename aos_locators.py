from faker import Faker
fake = Faker(locale='en_CA')
aos_url = 'https://advantageonlineshopping.com/#/'
aos_title = '\xa0Advantage Shopping'
aos_register_url = 'https://advantageonlineshopping.com/#/register'
username = f'{fake.user_name()[:12]}{fake.pyint(11,999)}'
password = fake.password()[:12]
new_username = fake.user_name()
first_name = fake.first_name()
last_name = fake.last_name()
full_name = f'{first_name} {last_name}'
email = fake.email()
city = fake.city()
province = fake.province_abbr()
phone = fake.phone_number()
postalcode = fake.postalcode_in_province()
country = fake.current_country()
new_user_url = 'https://advantageonlineshopping.com/#/myAccount'
address = f'{fake.street_address()}'




