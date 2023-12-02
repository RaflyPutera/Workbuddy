from PySide6.QtWidgets import QGraphicsOpacityEffect
from PySide6.QtCore import QPropertyAnimation, QEasingCurve

def effect_fade(self, fadestyle:str,objectname):
    opacityeffect=QGraphicsOpacityEffect(objectname)
    objectname.setGraphicsEffect(opacityeffect)    
    self.animationEffect= QPropertyAnimation(opacityeffect, b"opacity")
    self.animationEffect.setEasingCurve(QEasingCurve.InOutQuart)
    if fadestyle == "in":
        self.animationEffect.setStartValue(0)
        self.animationEffect.setEndValue(1)
    if fadestyle == "out":
        self.animationEffect.setStartValue(1)
        self.animationEffect.setEndValue(0)
    self.animationEffect.setDuration(1500)
    self.animationEffect.start()
    pass
def fade_out(self):
    pass