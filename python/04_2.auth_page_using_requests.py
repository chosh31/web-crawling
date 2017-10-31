import requests
from urllib import request, parse
from bs4 import BeautifulSoup

id = ''
passwd = ''

session = requests.session()

login_info = {
    'm_id': id,
    'm_passwd': passwd
}

# Login
login_page = 'http://www.hanbit.co.kr/member/login_proc.php'
res = session.post(login_page, data=login_info)
res.raise_for_status()

# Access
my_page = 'http://www.hanbit.co.kr/myhanbit/myhanbit.html'
res = session.get(my_page)
res.raise_for_status()

# Get Mileages
parser = BeautifulSoup(res.text, 'html.parser')
mileage = parser.select_one(".mileage_section1 span").get_text()
ecoin = parser.select_one(".mileage_section2 span").get_text()
print("Mileage = {0}, e-coin = {1}".format(mileage, ecoin))