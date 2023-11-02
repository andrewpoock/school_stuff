# gui.py


import tkinter as tk
import sys
from io import StringIO
sys.path.insert(0, '..')  # fix to allow imorts from paystation module

from paystation.domain import PayStation
from paystation.config import (AlphaTownFactory,
                               BetaTownFactory,
                               GammaTownFactory,
                               TripoliFactory
                               )

from paystation.guiview import PayStationGUIview

# Configuration of PayStations to appear in the GUI
FACTORIES = [AlphaTownFactory(), BetaTownFactory(),
             GammaTownFactory(), TripoliFactory()]


class MultiPayStationModel:
    """ Model for PayStationGUIApp"""

    def __init__(self):
        self.factories = []
        self.config_id = None
        self._current_ps = None
        self.paystation_labels = []

    def add_paystation(self, factory):
        self.factories.append(factory)
        self.paystation_labels.append(factory.config_id)

    def set_paystation(self, label):
        for fact in self.factories:
            if fact.config_id == label:
                break
        self._current_ps = PayStation(fact)
        self.config_id = label
            
    def add_payment(self, payment):
        self._current_ps.add_payment(payment)

    def read_display(self):
        return self._current_ps.read_display()

    def buy(self):
        return self._current_ps.buy()

    def cancel(self):
        self._current_ps.cancel()


class PayStationGUIApp:
    """ Presenter for the PayStation GUI """

    def __init__(self, root, model, view):
        self.root = root
        self.model = model
        self.view = view
        view.set_controller(self)
        view.set_state(dict(accept_select_paystation=True, accept_transaction=False,
                 accept_coin=False, variant='Select Variant', display=''))
        view.set_labels(self.model.paystation_labels)

    def run(self):
        self.root.title("Paystation Simulator")
        self.root.deiconify()
        self.root.mainloop()

    def select_paystation(self, id):
        self.model.set_paystation(id)
        self.view.set_state(dict(accept_select_paystation=True, accept_transaction=False,
                 accept_coin=True, variant=id, display=self.model.read_display()))

    def coin(self, amount):
        self.model.add_payment(amount)
        self.view.set_state(dict(accept_select_paystation=False, accept_transaction=True,
                 accept_coin=True, variant=self.model.config_id, display=self.model.read_display()))

    def transaction(self, key):
        if key == 'cancel':
            self.model.cancel()
            self.view.set_state(dict(accept_select_paystation=True, accept_transaction=False,
                 accept_coin=True, variant=self.model.config_id, display=self.model.read_display()))
        if key == 'buy':
            stream = StringIO()
            self.model.buy().print(stream)
            self.view.show_receipt(stream.getvalue())
            self.view.set_state(dict(accept_select_paystation=True, accept_transaction=False,
                 accept_coin=True, variant=self.model.config_id, display=self.model.read_display()))

def main():
    root = tk.Tk()
    view = PayStationGUIview(root)
    model = MultiPayStationModel()
    for factory in FACTORIES:
        model.add_paystation(factory)
    PayStationGUIApp(root, model, view).run()


if __name__ == "__main__":
    main()
