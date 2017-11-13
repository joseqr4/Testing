from selenium import webdriver
from User import Usuario
from ProductoAlta import Producto


import unittest
import time


class ProductoAltaMain(unittest.TestCase): 
    
    
    def setUp(self):

        start = time.time()
       # crear una nueva sesion de Chrome
        self.driver = webdriver.Chrome() 
       # self.driver.implicitly_wait(30) 
        self.driver.maximize_window() 
        # navegar a Google
        self.driver.get("https://sandbox.2checkout.com/sandbox") 

        UserIngreso= Usuario(self.driver)
        UserIngreso.AccederCta("equipo2","Testing2017")
        
        
    def test_Creacion_Sin_Nombre(self):
        
        PaginaProducto= Producto(self.driver)
        PaginaProducto.EntraraProducto()
               
        PaginaProducto.CrearProductoEsc1()
        
      
        PaginaProducto.CompletarFormulario("","100")
        self.assertFalse(PaginaProducto.VerificarPrecioyNombre())

    def test_Creacion_Sin_Precio(self):

        PaginaProducto= Producto(self.driver)
        PaginaProducto.EntraraProducto()
               
        PaginaProducto.CrearProductoEsc1()
        
      
        PaginaProducto.CompletarFormulario("Silla","")
        self.assertFalse(PaginaProducto.VerificarPrecioyNombre())


    def test_Creacion_Precio_Numerico(self):

        PaginaProducto= Producto(self.driver)
        PaginaProducto.EntraraProducto()
               
        PaginaProducto.CrearProductoEsc1()
        
      
        PaginaProducto.CompletarFormulario("Silla","asd")
        self.assertFalse(PaginaProducto.VerificarPrecioyNombre())

    def test_Creacion_Correcto(self):

        PaginaProducto= Producto(self.driver)
        PaginaProducto.EntraraProducto()
               
        PaginaProducto.CrearProductoEsc1()
        
      
        PaginaProducto.CompletarFormulario("Silla","100")
        assert PaginaProducto.VerificarPrecioyNombre()
    
        
    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()


