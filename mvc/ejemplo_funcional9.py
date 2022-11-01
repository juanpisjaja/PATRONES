class Model(object):
    services = {
    'reparación': {'Código': '#6135','precio': 100.000},
        'limpieza': {'Código': '#8569','precio': 250.000},
        'alimentación': {'Código': '#3596','precio': 325.000},
    }
class View(object):
    def list_services(self, services):
        for svc in services:
            print(svc, " ")
    def list_pricing(self, services):
        for svc in services:
            print("Código", Model.services[svc]['Código'],
                  svc, "in total you pay $",
                  Model.services[svc]['precio'])
class Controller(object):
    def __init__(self):
        self.model = Model()
        self.view = View()
    def get_services(self):
        services = self.model.services.keys()
        return self.view.list_services(services)
    def get_pricing(self):
        services = self.model.services.keys()
        return self.view.list_pricing(services)
class Client(object):
    con = Controller()
    print("Servicios prestados:")
    con.get_services()
    print("Precios de los servicios:")
    con.get_pricing()