from selenium import webdriver

url = 'https://nid.naver.com/nidlogin.login?url=http%3A%2F%2Fmail.naver.com%2F'

#.bash_profile path or PATH parameter
browser = webdriver.PhantomJS()

browser.implicitly_wait(3)

browser.get(url)
#browser.save_screenshot('website_start.png')

user = ''
e = browser.find_element_by_id('id')
e.clear()
e.send_keys(user)
#browser.save_screenshot('website_id.png')

pw = ''
e = browser.find_element_by_id('pw')
e.clear()
e.send_keys(pw)
#browser.save_screenshot('website_pw.png')

form = browser.find_element_by_css_selector('input.btn_global[type=submit]')
form.submit()
#browser.save_screenshot('website_login.png')

browser.get('https://mail.naver.com/?n=1509348766758&v=l')
for element in browser.find_elements_by_class_name('mTitle'):
    sender = element.find_element_by_css_selector('.name').text
    subject = element.find_element_by_css_selector('.mail_title').text
    print('{0} -> {1}'.format(sender, subject))

browser.quit()