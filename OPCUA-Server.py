import sys
sys.path.insert(0, "..")
import time


from opcua import ua, Server


if __name__ == "__main__":

    # setup our server
    server = Server()
    #server.set_endpoint("opc.tcp://192.168.105.173:4840/htwdresden/server/")
    server.set_endpoint("opc.tcp://0.0.0.0:4840/htwdresden/server/")

    # setup our own namespace, not really necessary but should as spec
    uri = "http://htw-dresden.de/workshop22"
    idx = server.register_namespace(uri)

    # get Objects node, this is where we should put our nodes
    objects = server.get_objects_node()

    # populating our address space
    output = server.nodes.objects.add_object(idx, "root")


    #Abschnitt Endpunkte
    #Fenster = output.add_object(idx, "Fenster")
    #Fenster.add_variable(idx, "Client1", True).set_writable()
    #Fenster.add_variable(idx, "Client2", True).set_writable()
    #Fenster.add_variable(idx, "Client3", True).set_writable()


    # Tempteratur
    Temperatur = output.add_object(idx, "Temperatur")
    Temperatur.add_variable(idx, "rpi1Sen1", 0.00).set_writable()
    #Temperatur.add_variable(idx, "Client1Sen2", 0.00).set_writable()
    Temperatur.add_variable(idx, "rpi2Sen1", 0.00).set_writable()
    #Temperatur.add_variable(idx, "Client2Sen2", 0.00).set_writable()
    Temperatur.add_variable(idx, "rpi4Sen1", 0.00).set_writable()
    #Temperatur.add_variable(idx, "Client3Sen2", 0.00).set_writable()
    Parameter = output.add_object(idx, "Parameter")
    Parameter.add_variable(idx, "currentSen", 0).set_writable()
    # starting!
    server.start()

    try:
        count = 0
        while True:
            time.sleep(1)
    finally:
        #close connection, remove subcsriptions, etc
        server.stop()
