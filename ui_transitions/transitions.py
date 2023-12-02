from PySide6.QtWidgets import QGraphicsOpacityEffect
from PySide6.QtCore import QPropertyAnimation, QEasingCurve

def reset_state(self):
    self.opacityeffect.deleteLater()

def effect_fade(self, fadestyle:str,objectname):
    self.opacityeffect=QGraphicsOpacityEffect(objectname)
    objectname.setGraphicsEffect(self.opacityeffect)    
    self.animationEffect= QPropertyAnimation(self.opacityeffect, b"opacity")
    self.animationEffect.setEasingCurve(QEasingCurve.InOutCubic)
    if fadestyle == "in":
        self.animationEffect.setEasingCurve(QEasingCurve.OutQuart)
        self.animationEffect.setStartValue(0)
        self.animationEffect.setEndValue(1)
    if fadestyle == "out":
        self.animationEffect.setEasingCurve(QEasingCurve.InQuart)
        self.animationEffect.setStartValue(1)
        self.animationEffect.setEndValue(0)
    self.animationEffect.setDuration(1000)
    self.animationEffect.start()
    self.animationEffect.finished.connect(lambda:reset_state(self))

    pass
