import unittest
import HTMLTestRunner
import os
from UserMain import UserMain
from ProductoAltaMain import ProductoAltaMain
from ProductoEditarMain import ProductoEditarMain
from ProductoEliminarMain import ProductoEliminarMain



# obtengo path para localizar donde escribir el reporte
dir = os.getcwd()

# obtener los casos de test de SearchText
usuario = unittest.TestLoader().loadTestsFromTestCase(UserMain)
ProductoAlta = unittest.TestLoader().loadTestsFromTestCase(ProductoAltaMain)
ProductoEditar = unittest.TestLoader().loadTestsFromTestCase(ProductoEditarMain)
ProductoEliminar = unittest.TestLoader().loadTestsFromTestCase(ProductoEliminarMain)


# creamos un test suite
test_suite = unittest.TestSuite([usuario,ProductoAlta,ProductoEditar,ProductoEliminar])

# creo archivo de reporte
outfile = open(dir + "\SeleniumPythonTestSummary.html", "w")

# configuro opciones de HTMLTestRunner
runner = HTMLTestRunner.HTMLTestRunner(stream=outfile,title='Test Report', description='Acceptance Tests')

# ejecutamos usando HTMLTestRunner
runner.run(test_suite)

