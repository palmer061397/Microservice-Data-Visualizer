
import sys
import plantuml



sys.path.append("C:/Users/Nathan Palmer/PycharmProjects/MicroserviceVisualizer/.venv/Custom_Modules")
from plantumlcmd import *

with open('./Docs/Testing/testinguml.txt', 'w', encoding="utf-8") as file:
    file.write(Start())
    file.write(Model.actor + "foo1" + Newline())
    file.write(Model.boundary + "foo2" + " " + Newline())
    file.write(Model.control + "foo3" + " " + Newline())
    file.write(Model.entity + "foo4" + " " + Newline())
    file.write(Model.database + "foo5" + " " + Newline())
    file.write(Model.collections + "foo6" + " " + Newline())
    file.write('Foo1' + XLeft() + 'Foo2 : To boundary' + Newline())
    file.write('Foo1' + ORight() + 'Foo3 : To control' + Newline())
    file.write('Foo1' + OLeft() + 'Foo4 : To entity' + Newline())
    file.write('Foo1' + XRight() + 'Foo5 : To database' + Newline())
    file.write('Foo1' + SolidRight() + 'Foo6 : To collections' + Newline())
    file.write(End())

def load_data():
    with open("./Docs/Testing/testinguml.txt", "r", encoding="utf-8") as plant_file:
        plant_data = plant_file.read()
        return plant_data

def create_plantuml_image():
    """ create_plantuml_image function reads plantuml.txt
        data and sends it to website to create and capture image"""
    plantuml.PlantUML("http://www.plantuml.com/plantuml/img/").processes_file('./Docs/Testing/testinguml.txt',
                                                                                  outfile="./PlantUML_Images/PlantUML.Testing.png",
                                                                                  errorfile="PlantUML_log.log")

load_data()
create_plantuml_image()
