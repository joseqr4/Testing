from page_objects import PageObject, PageElement, MultiPageElement
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException



class ProductoEdit(PageObject):
        
    BotonEdit= PageElement(xpath='//*[@id="sub-nav"]/ul/li[2]/a')
    primerelemento=PageElement(xpath='//*[@id="update_bulk"]/table/tbody/tr[2]/td[6]/input')

   #----- Campos formulario


    
    def EntraraProductoEdit(self):
        self.BotonEdit.click()
        
    def EditarProducto(self,precio):
        
        self.primerelemento.clear()
        self.primerelemento.send_keys(precio)
        self.primerelemento.submit()

    def VerificarEdicion(self):
       
        try:
            myElem = WebDriverWait(self.w, 4).until(EC.visibility_of_element_located((By.CLASS_NAME, 'form_invalid')))
            return False
        except TimeoutException:
            return True
            

  
              
                
        
        
        
