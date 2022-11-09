class Locator():
    locators = { "btnEnter2Acc":".//button[text()='Войти в аккаунт']",
                 "lblEmail":"//label[text()='Email']/following::input[@type='text']",
                 "lblPwd":"//input[@type='password']",
                 "btnSignIn":"//button[contains(text(),'Войти')]",
                 "link2lk":".//a[@href='/account']",
                 "builder":"//p[contains(text(),'Конструктор')]",
                 "spnSouce":"//span[contains(text(),'Соусы')]",
                 "spnBread":"//span[contains(text(),'Булки')]",
                 "spnFills":"//span[contains(text(),'Начинки')]",
                 "btnSignUp":"//button[contains(text(),'Зарегистрироваться')]",
                 "lblUserName":"//label[text()='Имя']/following::input[@type='text']",
                 "btnExit":".//ul[@class='Account_list__3KQQf mb-20']/li[@class='Account_listItem__35dAP']/button[text()='Выход']",
                 "linkSingIn":"//a[@href='/login']",
                 "linkSingUp":"//a[contains(text(),'Зарегистрироваться')]",
                 "linkRcwPwd":" //a[contains(text(),'Восстановить пароль')]",
                 "MsgIncPwd":"//p[contains(text(),'Некорректный пароль')]",
                 "Logo":"//div[@class='AppHeader_header__logo__2D0X2']"
                 }
    """
    Локаторы:
                btnEnter2Acc кнопка "Войти в аккаунт"
                lblEmail Поле ввода почты при входе/регистрации 
                lblPwd Поле ввода пароля при входе/регистрации 
                btnSignIn Кнопка "Войти"
                link2lk Переход в личный кабинет 
                builder Конструктор
                spnSouce  раздел Соусы
                spnBread раздел Булки
                spnFills Раздел Начинки
                btnSignUp Кнопка "Зарегистрироваться"
                lblUserName Поле ввода имени при регистрации 
                btnExit Кнопка Выход
                linkSingIn Переход к Входу на форме регистрации
                linkSingUp Переход к регистрации на форме входа
                linkRcwPwd Переход к форме восстановления пароля
                MsgIncPwd Сообщение Некорректный пароль
                Logo Логотип
    """
    def __init__(self):
        self
        
    def get_locator(self, name):
        return self.locators.get(name)
        
    def set_locator(self):
        """
        Не реализуем, т.к. пока нет необходимости
        в дополнении списка локаторов.
        """
        pass 
