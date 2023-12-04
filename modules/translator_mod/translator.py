from googletrans import Translator

#initial variables
tr_to=None
languages=['en','ko','id','ja','zh-TW']
#call functions
def translate(self):
    translator=Translator()
    tr_in=self.ui.tr_input.toPlainText()
    tolang=self.ui.tr_to.currentIndex()
    tr_to=translator.translate(tr_in,dest=languages[tolang])
    self.ui.tr_output.setPlainText(tr_to.text)