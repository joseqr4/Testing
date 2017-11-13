from selenium import webdriver
from User import Usuario


import unittest
import time


class UserMain(unittest.TestCase): 
    
    
    def setUp(self):

        start = time.time()
       # crear una nueva sesion de Chrome
        self.driver = webdriver.Chrome() 
       # self.driver.implicitly_wait(30) 
        self.driver.maximize_window() 
        # navegar a Google
        self.driver.get("https://sandbox.2checkout.com/sandbox") 
        
    def test_usuario_correcto_pass_incorrecto(self):
        
        UserIngreso= Usuario(self.driver)
        UserIngreso.AccederCta("equipo2","Testing20172")
        self.assertFalse(UserIngreso.VerificarLogueo())

    def test_usuario_incorrecto_pass_correcto(self):
        UserIngreso= Usuario(self.driver)
        UserIngreso.AccederCta("asd","Testing2017")
        self.assertFalse(UserIngreso.VerificarLogueo())
 
        
    def test_usuario_pass_corretos(self):
        UserIngreso= Usuario(self.driver)
        UserIngreso.AccederCta("equipo2","Testing2017")
        assert UserIngreso.VerificarLogueo()
        
    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()

