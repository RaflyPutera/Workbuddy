from ui_transitions import transitions
def route_from(self, identifier):
    if identifier == 0:
        transitions.effect_fade(self,"out",self.ui.Introframe)
        self.animationEffect.finished.connect(lambda:route_to(self,identifier))

    elif identifier==1:
        transitions.effect_fade(self,"out",self.ui.functionStack)
        self.animationEffect.finished.connect(lambda:route_to(self,identifier))
    

def route_to(self,identifier):
    if identifier==0:
        transitions.effect_fade(self,"in",self.ui.MainFrame)
        self.ui.mainStackW.setCurrentIndex(1)
        # self.animationEffect=None
    elif identifier==1:
        self.ui.functionStack.setCurrentIndex(1)
        transitions.effect_fade(self,"in",self.ui.functionStack)