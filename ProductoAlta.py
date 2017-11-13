from page_objects import PageObject, PageElement, MultiPageElement
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException


class Producto(PageObject):
    
    botonProducto= PageElement(id_='tab-products')
    CrearProducto= PageElement(xpath='//*[@id="content"]/div[1]/div/div/a')

   #----- Campos formulario

    Name= PageElement(name="name")
    Precio=PageElement(name="price")
    BotonCrear=PageElement(name="submit")
    
    def EntraraProducto(self):
        self.botonProducto.click()
        
    def CrearProductoEsc1(self):
        self.CrearProducto.click()

    def CompletarFormulario(self,name,Precio):
        self.Name.send_keys(name)
        self.Precio.send_keys(Precio)
        self.BotonCrear.click()

    def VerificarPrecioyNombre(self):
        try:
                                    
            myElem = WebDriverWait(self.w, 5).until(EC.presence_of_element_located((By.CLASS_NAME, 'form_invalid')))
            return False
        except TimeoutException:
            return True
              
                
   
