from page_objects import PageObject, PageElement, MultiPageElement
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import unittest


class ProductoDelet(PageObject):
        
    BotonView= PageElement(xpath='//*[@id="sub-nav"]/ul/li[1]/a')
    primerelementoCheckBox=PageElement(xpath='//*[@id="update_bulk"]/table/tbody/tr[2]/td[1]/input')
    SegundoBotonSumit=PageElement(xpath='//*[@id="delete_items"]/input[2]')
    idPrimerElemento=PageElement(xpath='//*[@id="update_bulk"]/table/tbody/tr[2]/td[4]')
    idElemento=0
       #----- Campos formulario

    def ObtenerPrimerElemento(self):
        self.idElemento=self.idPrimerElemento.text
    
    def EntraraProductoView(self):
        self.BotonView.click()
        

    def SeleccionarProducto(self):
              
        self.primerelementoCheckBox.click()
        
        
    def EliminarProductoPaso1(self):
        self.primerelementoCheckBox.submit()
                
    def EliminarProductoPaso2(self):
        
        try:
            SegundoBotonSumit = WebDriverWait(self.w, 4).until(EC.presence_of_element_located((By.XPATH, '//*[@id="delete_items"]/input[2]')))
            self.SegundoBotonSumit.click()
            return True
        except:
            return False

    def verificarEliminacion(self):
        self.EntraraProductoView()
        print(self.idElemento)
        print(self.idPrimerElemento.text)
        if self.idElemento==self.idPrimerElemento.text:
            return False
        else:
            return True
        
        
        
        
