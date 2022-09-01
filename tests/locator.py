#buttons

button_personal_account = "//p[contains(text(),'Личный Кабинет')]" #кнопка «Личный кабинет»
button_registry = "//button[contains(text(),'Зарегистрироваться')]" #кнопка «Зарегистрироваться»
button_sign_in = "//button[text()='Войти'] " #кнопка «Войти»
button_sign_in_account = "//button[contains(text(),'Войти в аккаунт')]" #кнопка «Войти в аккаунт»
button_constructor = "//p[contains(text(),'Конструктор')]" #кнопка «Конструктор»
button_exit = "//button[contains(text(),'Выход')]" #кнопка "Выход"

#inputs

input_name_on_page_registry = "//fieldset[1]//input" #поле "Имя" на станице регистрации
input_email_on_page_registry = "//fieldset[2]//input" #поле "email" на станице регистрации
input_password_on_page_registry = "//input[@name='Пароль']" #поле "Пароль" на станице регистрации
input_email_on_page_sign_in = "//fieldset[1]//input" #поле "email" на странице входа
input_password_on_page_sign_in = "//fieldset[2]//input" #поле "Пароль" на странице входа

#links

link_registry = "//a[contains(text(),'Зарегистрироваться')]" #линк «Зарегистрироваться»
link_recover_password = "//a[contains(text(),'Восстановить пароль')]" #линк «Восстановить пароль»
link_sign_in = "//a[contains(text(),'Войти')]" #линк "Войти"

#pages

page_registry = "//h2[contains(text()='Регистрация')]" #страница регистрации
page_sign_in = "//h2[contains(text(),'Вход')]" #страница входа
page_main = "//h1[contains(text(),'Соберите бургер')]" #главная страница приложения
page_account = "//a[contains(text(),'Профиль')]" #страница с личным кабинетом
page_recover_password = "//h2[contains(text(),'Восстановление пароля')]" #страница восстановления пароля

#tabs

tab_toppings = "//span[contains(text(),'Начинки')]" #вкладка «Начинки»
tab_buns = "//span[contains(text(),'Булки')]" #вкладка «Булки»
tab_sauces = "//span[contains(text(),'Соусы')]" #вкладка «Соусы»
menu_toppings = "//p[contains(text(),'Филе Люминесцентного тетраодонтимформа')]" #меню «Начинки», используем позицию из меню,
# чтоб определить по ней, что меню с начинками появилось на экране
menu_buns = "//p[contains(text(),'Краторная булка N-200i')]" #меню «Булки», используем позицию из меню,
# чтоб определить по ней, что меню с булками появилось на экране
menu_sauces = "//p[contains(text(),'Соус с шипами Антарианского плоскоходца')]" #меню «Соусы», , используем позицию из меню,
# чтоб определить по ней, что меню с соусами появилось на экране

#others

message_error_password = "//p[contains(text(),'Некорректный пароль')]" #сообщение «Некорректный пароль» в форме ввода под полем «Пароль»
logo = "//header/nav[1]/div[1]/a[1]/*[1]" #логотип Stellar Burgers



