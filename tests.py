from datetime import time

def check_time(current_time):
    if time(hour=22) <= current_time or current_time < time(hour=6):
        return True
    else:
        return False



def test_dark_theme_by_time():
    """
    Протестируйте правильность переключения темной темы на сайте в зависимости от времени
    """
    current_time = time(hour = 22)
    is_dark_theme = check_time(current_time)

    assert is_dark_theme is True

def dark_theme_with_user(current_time, dark_theme_enabled_by_user):
    if dark_theme_enabled_by_user is True:
        return True
    elif dark_theme_enabled_by_user is False:
        return False
    else:
        if time(hour=22) <= current_time or current_time < time(hour=6):
            return True
        else:
            return False


def test_dark_theme_by_time_and_user_choice():
    """
    Протестируйте правильность переключения темной темы на сайте
    в зависимости от времени и выбора пользователя
    dark_theme_enabled_by_user = True - Темная тема включена
    dark_theme_enabled_by_user = False - Темная тема выключена
    dark_theme_enabled_by_user = None - Пользователь не сделал выбор (используется переключение по времени системы)
    """
    current_time = time(hour=23)
    dark_theme_enabled_by_user = None

    is_dark_theme = dark_theme_with_user(current_time, dark_theme_enabled_by_user)
    assert is_dark_theme is True

def find_user_olga(users):
    for user in users:
        if user["name"] == "Olga":
            user_find = user
    return user_find

def find_user_under_20(users):
    users_find = [user for user in users if user["age"] < 20]
    return users_find

def test_find_suitable_user():
    """
    Найдите нужного пользователя по условиям в списке пользователей
    """
    users = [
        {"name": "Oleg", "age": 32},
        {"name": "Sergey", "age": 24},
        {"name": "Stanislav", "age": 15},
        {"name": "Olga", "age": 45},
        {"name": "Maria", "age": 18},
    ]

    # TODO найдите пользователя с именем "Olga"
    suitable_users = find_user_olga(users)
    assert suitable_users == {"name": "Olga", "age": 45}

    # TODO найдите всех пользователей младше 20 лет
    suitable_users = find_user_under_20(users)
    assert suitable_users == [
        {"name": "Stanislav", "age": 15},
        {"name": "Maria", "age": 18},
    ]


# Сделайте функцию, которая будет печатать
# читаемое имя переданной ей функции и значений аргументов.
# Вызовите ее внутри функций, описанных ниже
# Подсказка: Имя функции можно получить с помощью func.__name__
# Например, вызов следующей функции должен преобразовать имя функции
# в более читаемый вариант (заменить символ подчеркивания на пробел,
# сделать буквы заглавными (или первую букву), затем вывести значения всех аргументов этой функции:
# >>> open_browser(browser_name="Chrome")
# "Open Browser [Chrome]"


def test_readable_function():
    open_browser(browser_name="Chrome")
    go_to_companyname_homepage(page_url="https://companyname.com")
    find_registration_button_on_login_page(page_url="https://companyname.com/login", button_text="Register")


def open_browser(browser_name):
    actual_result = readable_func(open_browser, browser_name)
    assert actual_result == "Open Browser [Chrome]"


def go_to_companyname_homepage(page_url):
    actual_result = readable_func(go_to_companyname_homepage, page_url)
    assert actual_result == "Go To Companyname Homepage [https://companyname.com]"


def find_registration_button_on_login_page(page_url, button_text):
    actual_result = readable_func(find_registration_button_on_login_page, page_url, button_text)
    assert actual_result == "Find Registration Button On Login Page [https://companyname.com/login, Register]"

def readable_func(func, *args):
    func_name = func.__name__.replace('_', ' ').title()
    args_name = ", ".join([*args])
    print(f"{func_name} [{args_name}]")
    return f"{func_name} [{args_name}]"
