from ui_transitions import transitions
def route_to(self, identifier):
    if identifier == 1:
        transitions.effect_fade(self,"out",self.ui.Introframe)
    pass