from selenium import webdriver
from User import Usuario
from ProductoAlta import Producto
from ProductoEditar import ProductoEdit



import unittest
import time


class ProductoEditarMain(unittest.TestCase): 
    
    
    def setUp(self): 
   # crear una nueva sesion de Chrome
        self.driver = webdriver.Chrome() 
       # self.driver.implicitly_wait(30) 
        self.driver.maximize_window() 
        # navegar a Google
        self.driver.get("https://sandbox.2checkout.com/sandbox")
        
        UserIngreso= Usuario(self.driver)
        UserIngreso.AccederCta("equipo2","Testing2017")

        PaginaProducto= Producto(self.driver)
        PaginaProducto.EntraraProducto()
               
        PaginaProducto.CrearProductoEsc1()
        
      
        PaginaProducto.CompletarFormulario("Silla","100")
        

    def test_Editar_Producto_Precio_Letras(self):
        
        PaginaEditProducto=ProductoEdit(self.driver)
        PaginaEditProducto.EntraraProductoEdit()

        PaginaEditProducto.EditarProducto("asd")
        self.assertFalse(PaginaEditProducto.VerificarEdicion())
 

    def test_Editar_Producto_SinPrecio(self):

        PaginaEditProducto=ProductoEdit(self.driver)
        PaginaEditProducto.EntraraProductoEdit()

        PaginaEditProducto.EditarProducto("")
        self.assertFalse(PaginaEditProducto.VerificarEdicion())


    def test_Editar_Producto_Correcto(self):

        PaginaEditProducto=ProductoEdit(self.driver)
        PaginaEditProducto.EntraraProductoEdit()

        PaginaEditProducto.EditarProducto("20")
        assert PaginaEditProducto.VerificarEdicion()

        
    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()

