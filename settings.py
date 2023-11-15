import os
from dotenv import load_dotenv
dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

# Valid user
tel = os.getenv('tel')
bel_tel = os.getenv('bel_tel')
pwd = os.getenv('pwd')
user_lastname = os.getenv('user_lastname')

BASE_URL = "https://b2c.passport.rt.ru/"
DIFFERENT_URL = "https://yandex.ru/"

# 'Valid' data for registered user
reg_first_name = "Тест"
reg_last_name = "Тестов"
reg_region = "Новосибирская обл"
reg_mail = os.getenv("reg_mail")
reg_pwd = "Abracadabra123"
reg_pwd_rep = "Abracadabra123"

# Набор тестовых данных

recovery = ""

# invalid data
invalid_mail = 'пример@почта.ру'
inv_mail = 'example@@mail.ru'
test_pwd = 'abracad1'
test_pwd_chars_oly = 'prostoqqprostoqq'
different_pwd = 'Abracadabra1'
Chinese_char = 	'作曲力作早安'
Latin = 'Stiven'
Spec_char = '[]\^$.|?*+()'
oversize_login = ("Lorem ipsum dolor sit amet, consectetuer "
                  "adipiscing elit. Aenean commodo ligula eget dolor."
                  " Aenean massa. Cum sociis natoque penatibus et "
                  "magnis dis parturient montes, nascetur ridiculus mus."
                  " Donec quam felis, ultricies nec, pellentesque eu, pretium quis,"
                  " sem. Nulla consequat massa quis enim. Donec pede justo, fringilla"
                  " vel, aliquet nec, vulputate eget, arcu. In enim justo, rhoncus ut, "
                  "imperdiet a, venenatis vitae, justo. Nullam dictum felis eu pede mollis "
                  "pretium. Integer tincidunt. Cras dapibus. Vivamus elementum semper nisi."
                  " Aenean vulputate eleifend tellus. Aenean leo ligula, porttitor eu,"
                  " consequat vitae, eleifend ac, enim. Aliquam lorem ante, dapibus in,"
                  " viverra quis, feugiat a, tellus. Phasellus viverra nulla ut metus varius"
                  " laoreet. Quisque rutrum. Aenean imperdiet. Etiam ultricies nisi vel augue."
                  " Curabitur ullamcorper ultricies nisi. Nam eget dui. Etiam rhoncus. Maecenas"
                  " tempus, tellus eget condimentum rhoncus, sem quam semper libero, sit amet"
                  " adipiscing sem neque sed ipsum. Nam quam nunc, blandit vel, luctus pulvinar,"
                  " hendrerit id, lorem. Maecenas nec odio et ante tincidunt tempus. Donec vitae "
                  "sapien ut libero venenatis faucibus. Nullam quis ante. Etiam sit amet orci eget"
                  " eros faucibus tincidunt. Duis leo. Sed fringilla mauris sit amet nibh. Donec"
                  " sodales sagittis magna. Sed consequat, leo eget bibendum sodales, augue velit"
                  " cursus nunc, quis gravida magna mi a libero. Fusce vulputate eleifend sapien. "
                  "Vestibulum purus quam, scelerisque ut, mollis sed, nonummy id, metus. Nullam accumsan"
                  " lorem in dui. Cras ultricies mi eu turpis hendrerit fringilla. Vestibulum ante "
                  "ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; In ac"
                  " dui quis mi consectetuer lacinia. Nam pretium turpis")
