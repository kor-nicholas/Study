# pip install selenium
# pip install msedge-selenium-tools selenium==3.141
# pip install fake-useragent
# pip install seleniumwire
# https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/
# https://chromedriver.storage.googleapis.com/index.html
# https://peter.sh/experiments/chromium-command-line-switches/ - options
# https://intoli.com/blog/not-possible-to-block-chrome-headless/chrome-headless-test.html - detect webdriver

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# from seleniumwire import webdriver # for proxy with login:pass
# from msedge.selenium_tools import Edge,EdgeOptions
from fake_useragent import UserAgent
from time import sleep
import pickle # cookie
from multiprocessing import Pool

url = 'https://instagram.com'

useragent = UserAgent()
options = webdriver.ChromeOptions()
# options.add_argument(f'user-agent={useragent.ie}') # Internet Explorer
# options.add_argument(f'user-agent={useragent.msie}')
# options.add_argument(f'user-agent={useragent.opera}')
# options.add_argument(f'user-agent={useragent.chrome}')
# options.add_argument(f'user-agent={useragent.google}')
# options.add_argument(f'user-agent={useragent.firefox}')
# options.add_argument(f'user-agent={useragent.ff}')
# options.add_argument(f'user-agent={useragent.safari}')
# options.add_argument(f'user-agent={useragent.random}')

# -------------------------------------------------------------------------------

# turn off webdriver mode under version 79.0.3945.16
# options.add_experimental_option('excludeSwitches', ['enable-automation'])
# options.add_experimental_option('useAutomationExtension', False)
# turn off webdriver mode in version 79.0.3945.16 and over
options.add_argument('--disable-blink-features=AutomationControlled')

# -------------------------------------------------------------------------------

# headless mode - фоновый режим
# options.add_argument('--headless')

# -------------------------------------------------------------------------------

# options.add_argument(f'--proxy-server=ip:port')

# proxy_options = {
# 	'proxy': {
# 		'https': f'http://{login}:{pass}@{ip}:{port}'
# 	}
# }

driver = webdriver.Chrome('chromedriver.exe', options=options)
# driver = webdriver.Chrome('chromedriver.exe', seleniumwire_options=proxy_options) # for proxy with login:pass

# -------------------------------------------------------------------------------

try:
	# driver.get(url)
	# driver.refresh()
	# driver.get_screenshot_as_file('screen.png')
	# driver.save_screenshot('screen2.png')

	# -------------------------------------------------------------------------------

	# driver.get(url)
	# sleep(5)

	# username = driver.find_element_by_name('username')
	# username.clear()
	# username.send_keys('viktorshcherban526')

	# password = driver.find_element_by_name('password')
	# password.clear()
	# password.send_keys('I3aLTYMNymfE')
	# sleep(3)

	# # button = driver.find_element_by_type('submit').click()
	# password.send_keys(Keys.ENTER) # other variant to enter in account
	# driver.send_keys(Keys.CTRL + Keys.T)
	# driver.send_keys('some text' + Keys.ENTER)
	# sleep(5)

	# # save cookie
	# pickle.dump(driver.get_cookies(), open(f'cookie', 'wb'))
	# sleep(3)

	# -------------------------------------------------------------------------------

	# load cookie
	# driver.get(url)
	# sleep(5)

	# for cookie in pickle.load(open('cookie', 'rb')):
	# 	driver.add_cookie(cookie)

	# sleep(5)
	# driver.refresh()
	# sleep(10)

	# -------------------------------------------------------------------------------

	# driver.get('https://intoli.com/blog/not-possible-to-block-chrome-headless/chrome-headless-test.html')
	# sleep(3)

	# driver.get('https://google.com')
	# print(driver.window_handles) # вкладки browser
	# print(driver.window_handles[0]) # first вкладка
	# print(driver.window_handles[2]) # third вкладка

	# driver.switch_to.window(driver.window_handles[2])
	# print(driver.current_url)

	# driver.close()
	# driver.switch_to.window(driver.window_handles[0])
	# sleep(3)

	# driver.implicitly_wait(5) # if element find before 5 sec, code continue

	# -------------------------------------------------------------------------------

except Exception as e:
	print(e)
finally:
	driver.close()
	driver.quit()

# -------------------------------------------------------------------------------
# Multiprocessing/Trhreads (open some browsers)

# def get_data(url):
# 	try:
# 		driver = webdriver.Chrome('chromedriver.exe')
# 		driver.get(url)
# 		driver.implicitly_time(10)
# 		driver.get_screenshot_as_file(f'media/{url.split('/')[1]}.png')
# 	except Exception as e:
# 		print(e)
# 	finally:
# 		driver.close()
# 		driver.quit()

# if __name__ == '__main__':
# 	url_list = ['https://google.com', 'https://instagram.com', 'https://tiktok.com']
# 	p = Pool(processes=3) # 3 - count process, 3 browsers
# 	p.map(get_data, url_list)

# -------------------------------------------------------------------------------
# VPS/VDS (comments)

# **Команды на сервере**
# Очистить окно терминала: clear
# Перемещение по директориям: cd dirname
# Список файлов в директории: ls
# Создать директорию: mkdir dirname
# Установка sudo: apt install sudo
# Обновление пакетов: sudo apt update && sudo apt upgrade
# Установка виртуального окружения: sudo apt install python3-venv
# Создание виртуального окружения: python3 -m venv venvName
# Запуск виртуального окружения: source venvName/bin/activate
# Обновление pip пакетов: pip install -U package_name

# Установка необходимых для корректной работы google-chroma пакетов:
# sudo apt install -y libxss1 libappindicator1 libindicator7

# Скачать google-chrome:
# sudo wget https://dl.google.com/linux/direct/go...

# Установка:
# sudo dpkg -i google-chrome*.deb

# Фиксим/подтягиваем зависимости:
# sudo apt install -y -f

# Проверить версию:
# google-chrome --version

# Установка screen: sudo apt install screen
# Создаст новый screen: screen
# Свернуть screen: CRTL + A, после чего нажмаем D
# Что-бы посмотреть список запущенных screen: screen -ls
# Что-бы вернуться к свёрнутому screen: screen -r
# Что-бы завершить сессию/закрыть screen: exit

