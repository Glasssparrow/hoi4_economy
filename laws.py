

class Law:

    def __init__(self):
        self.names = []
        self.constr = []
        self.civil_constr = []
        self.mil_constr = []
        self.mil_output = []
        self.cons_goods = []
        self._default_pos = 0
        self.pos = 0

    def law_up(self):
        if self.pos < len(self.civil_constr):
            self.pos += 1

    def law_down(self):
        if self.pos > 0:
            self.pos += -1

    @property
    def default_pos(self):
        return self._default_pos

    @default_pos.setter
    def default_pos(self, new_default_pos):
        self._default_pos = new_default_pos
        self.pos = new_default_pos

    def add_law_lvl(self, name,
                    const=0.0, civil_constr=0.0, mil_constr=0.0,
                    mil_output=0.0, cons_goods=0.0):
        self.names.append(name)
        self.constr.append(const)
        self.civil_constr.append(civil_constr)
        self.mil_constr.append(mil_constr)
        self.mil_output.append(mil_output)
        self.cons_goods.append(cons_goods)
