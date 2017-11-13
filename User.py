from page_objects import PageObject, PageElement

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class Usuario(PageObject):
    usuario= PageElement(name="username")
    password=PageElement(id_="password")
    element= PageElement(id_="login-error")

    def AccederCta(self,user,password):
        self.usuario.send_keys(user)
        self.password.send_keys(password)
        self.password.submit()

    def VerificarLogueo(self):
        try:
                                    
            myElem = WebDriverWait(self.w, 5).until(EC.visibility_of_element_located((By.ID, 'login-error')))
            return False
        except:
            return True
        
