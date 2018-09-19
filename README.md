# Point Of Sales POS Ecommerce
 Python Django

Merupakan website POS sederhana yang dibangun dengan framework django


# Requirement
* XAMPP
* python 3
* pip
* virtualenvwrapper-win
* django
* mysqlclient
* reportlab


# Installation (windows)
1. Intall python 3
2. Install pip
3. Open Command Prompt, and type
  
	* `pip  install virtualenvwrapper-win`
	* `mkvirtualenv academic`
	* `workon akademic`
	* `pip  install  mysqlclient`
	* `pip  install  reportlab`

4. Extract & Copy folder ("Point-Of-Sales-POS-Ecommerce-master") to C:/Users/(userpc)/
5. Activate XAMMP MySQL, Create database "djangopenjualan" 
6. Open Command Prompt, and type
 
	* `cd Point-Of-Sales-POS-Ecommerce-master`
	* `python manage.py migrate`
	* `python manage.py createsuperuser`
	* `python manage.py runserver`

Back-End = http://localhost:8000/admin (Login with username & password)

Front-End = http://localhost:8000/

# Installation (linux)

Untuk installasi linux tidak perlu saya jelaskan lagi, kurang lebih sama dengan windows, bahkan lebih mudah
