# ამოცანა 1
from datetime import datetime

def dgeebi_mde_dabadebis_dghemde(dabadebis_dghe):
    dghes = datetime.today()
    es_tseli_dabadebis = dabadebis_dghe.replace(year=dghes.year)
    if es_tseli_dabadebis < dghes:
        es_tseli_dabadebis = es_tseli_dabadebis.replace(year=dghes.year + 1)
    return (es_tseli_dabadebis - dghes).days

# ამოცანა 2
def gaormage_result(func):
    def shemowmeba(*args, **kwargs):
        shedegi = func(*args, **kwargs)
        return shedegi * 2
    return shemowmeba

@gaormage_result
def jamit_mimateba(a, b):
    return a + b

# ამოცანა 3
from datetime import datetime

def logi_gamodzaxebis(func):
    def shemowmeba(*args, **kwargs):
        shedegi = func(*args, **kwargs)
        print(f"Function '{func.__name__}' was called at {datetime.now()} and returned {shedegi}")
        return shedegi
    return shemowmeba

@logi_gamodzaxebis
def gamravleba(a, b):
    return a * b

# ამოცანა 4
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel

class მარტივიპროგრამა(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.garemo = QVBoxLayout()

        self.texT_shemotana = QLineEdit(self)
        self.garemo.addWidget(self.texT_shemotana)

        self.gundi = QPushButton('Textis Gamoxatva', self)
        self.gundi.clicked.connect(self.textis_gamoxatva)
        self.garemo.addWidget(self.gundi)

        self.etiketi = QLabel('', self)
        self.garemo.addWidget(self.etiketi)

        self.setLayout(self.garemo)
        self.setWindowTitle('Martivi PyQt Program')

    def textis_gamoxatva(self):
        teqsti = self.texT_shemotana.text()
        self.etiketi.setText(teqsti)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    piroba = მარტივიპროგრამა()
    piroba.show()
    sys.exit(app.exec_())
