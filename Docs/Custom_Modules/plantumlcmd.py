""" This module provides commands to edit diagrams and their
    appearances/attributes to PLANTUML"""
def Start():
    """Starts the uml diagram"""
    return "@startuml \n"

def End():
    """"Ends the uml diagraam"""
    return "@enduml \n"

def Autonumber():
    return "autonumber"

def Newpage():
    return "newpage"

def Newline():
    return "\n"

def SolidLeft():
    return " <- "

def SolidRight():
    return " -> "

def DottedLeft():
    return " <-- "

def DottedRight():
    return " --> "

def ThinRight():
    return " ->> "

def ThinLeft():
    return " <<- "

def BiArrow():
    return " <=> "

def XRight():
    return " ->x "

def XLeft():
    return " x<- "

def ORight():
    return " ->o "

def OLeft():
    return " o<- "




class Model:
    """
    If the keyword participant is used to declare a participant, more control on that participant is possible.
    The order of declaration will be the (default) order of display.
    Using these other keywords to declare participants will change the shape of the participant representation:
    • actor
    • boundary
    • control
    • entity
    • database
    • collections
    """
    '''
    Example:
    @startuml
    actor Foo1
    boundary Foo2
    control Foo3
    entity Foo4
    database Foo5
    collections Foo6
    Foo1 -> Foo2 : To boundary
    Foo1 -> Foo3 : To control
    Foo1 -> Foo4 : To entity
    Foo1 -> Foo5 : To database
    Foo1 -> Foo6 : To collections
    @enduml'''

    # Participant models
    actor = 'actor '
    boundary = 'boundary '
    control = 'control '
    entity = 'entity '
    database = 'database '
    collections = 'collections '
    # You can use the order keyword to customize the display order of participants.
    first_order = "First order"
    middle_order = "Middle order"
    last_order = "Last order"

