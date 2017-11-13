from selenium import webdriver
from User import Usuario
from ProductoAlta import Producto
from ProductoEditar import ProductoEdit
from ProductoEliminar import ProductoDelet


import unittest
import time


class ProductoEliminarMain(unittest.TestCase): 
    
    
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
##               
##        PaginaProducto.CrearProductoEsc1()
##        
##      
##        PaginaProducto.CompletarFormulario("Silla","100")
##
##        PaginaEditProducto=ProductoEdit(self.driver)
##        PaginaEditProducto.EntraraProductoEdit()
##
##        PaginaEditProducto.EditarProducto("20")

    def test_Eliminar_sin_seleccionar(self):
                
        PaginaEliminarProducto= ProductoDelet(self.driver)
        PaginaEliminarProducto.EntraraProductoView()
        PaginaEliminarProducto.ObtenerPrimerElemento()
        PaginaEliminarProducto.EliminarProductoPaso1()
        self.assertFalse(PaginaEliminarProducto.EliminarProductoPaso2())
        self.assertFalse(PaginaEliminarProducto.verificarEliminacion())

    def test_Eliminar_correcto(self):

        PaginaEliminarProducto= ProductoDelet(self.driver)
        PaginaEliminarProducto.EntraraProductoView()
        PaginaEliminarProducto.ObtenerPrimerElemento()
        PaginaEliminarProducto.SeleccionarProducto()
        PaginaEliminarProducto.EliminarProductoPaso1()
        self.assertTrue(PaginaEliminarProducto.EliminarProductoPaso2())
        self.assertTrue(PaginaEliminarProducto.verificarEliminacion())
        
  

        
    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()

