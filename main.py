# This Python file uses the following encoding: utf-8
import sys
from PySide6.QtWidgets import (QApplication, QMainWindow, QVBoxLayout,
                               QFileDialog, QMessageBox)
from PySide6.QtGui import QIcon
from UI_mainwindow import Ui_MainWindow
from qt_material import apply_stylesheet
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
from matplotlib import pyplot as plt
import matplotlib
import csv


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        MainWindow.resize(self, 1500, 800)

        # teste github
        # tesssteeee

        self.titulo = ''
        self.arq_ok = False
        self.iniciou = False
        self.dados = {}
        self.ax_new = None

        # CRIAÇÃO DO GRÁFICO
        layout = QVBoxLayout(self.fr_grafico)
        self.setLayout(layout)

        self.canvas = FigureCanvas(Figure(figsize=(2, 2), dpi=100,
                                          layout='constrained'))
        layout.addWidget(NavigationToolbar(self.canvas, self))
        layout.addWidget(self.canvas)

        font = {
            'weight': 'normal',
            'size': 10
        }
        matplotlib.rc('font', **font)

        self.ax = self.canvas.figure.subplots(1, 1)
        self.ax.set_title("Grafico da Escala linear")
        self.ax.set_xlabel("Entrada")
        self.ax.set_ylabel("Saída")
        self.ax.grid(True)
        self.ax.xaxis.set_minor_locator(matplotlib.ticker.AutoMinorLocator())
        self.ax.yaxis.set_minor_locator(matplotlib.ticker.AutoMinorLocator())

    def calculo(self):
        grInput, grX0, grX1, grY0, grY1, grOutput = self.valores_float()
        if (self.arq_ok == False) and ((grX0 == grX1) or (grY0 == grY1)):
            self.show_message()
            return
        else:
            if self.iniciou == False:
                self.inicio()

        if self.le_input.isModified():
            self.updSlider()
            self.le_input.setModified(False)

        try:
            # Cálculo do Ganho = Coeficienbte Angular
            gr_m = (grY1 - grY0) / (grX1 - grX0)
            # Cálculo do Offset = Coeficiente Linear
            gr_b = grY1 - (gr_m * grX1)
        except ZeroDivisionError:
            return
        gr_out = (gr_m * grInput) + gr_b   # Cálculo da Saída Linear

        if self.cb_limite.isChecked():     # Considerar o Limite de Y = Saída Linear
            if grY1 > grY0:                # Sentido Direto
                if gr_out > grY1:
                    gr_out = grY1
                if gr_out < grY0:
                    gr_out = grY0
            elif grY1 < grY0:              # Sentido Reverso
                if gr_out > grY0:
                    gr_out = grY0
                if gr_out < grY1:
                    gr_out = grY1

        # Atualiza os resultados
        self.le_output.setText(str(round(gr_out, 3)))
        self.le_m.setText(str(round(gr_m, 3)))
        self.le_b.setText(str(round(gr_b, 3)))

        self.update_chart()

    def update_chart(self):
        grInput, grX0, grX1, grY0, grY1, grOutput = self.valores_float()
        
        if grX1 > grX0:            
            self.hs_input.setMinimum(int(grX1 - (grX1 * 1.5)))
            self.hs_input.setMaximum(int(grX1 + (grX1 * 0.5)))
            self.hs_input.setValue(int(self.le_input.text()))
        else:
            self.hs_input.setMinimum(int(grX0 - (grX0 * 1.5)))
            self.hs_input.setMaximum(int(grX0 + (grX0 * 0.5)))
            self.hs_input.setValue(int(self.le_input.text()))
            

        if self.ax_new:
            self.ax_new.remove()

        if grY0 > grY1:
            self.ax.set_ylim([(grY0-(grY0*1.55)), (grY0+(grY0*0.55))])
        else:
            self.ax.set_ylim([(grY1-(grY1*1.55)), (grY1+(grY1*0.55))])
        if grX0 > grX1:
            self.ax.set_xlim([(grX0 - (grX0 * 1.55)), (grX0 + (grX0 * 0.55))])
        else:
            self.ax.set_xlim([(grX1 - (grX1 * 1.55)), (grX1 + (grX1 * 0.55))])
        self.ax_new = self.ax.scatter(grInput, grOutput, s=20, edgecolor='red')
        self.ax.set_aspect(0.5/self.ax.get_data_ratio())

        self.canvas.draw()

    def load_arquivo(self):
        arquivo = QFileDialog.getOpenFileName(
            dir="Dados", filter='Arquivo DAT (*.dat)')[0]

        self.titulo = " - " + arquivo
        MainWindow.setWindowTitle(
            self, "Cálculo de Escala Linear" + self.titulo)

        with open(arquivo, 'r') as f:
            vlr = csv.reader(f)
            a = []
            for x in vlr:
                a = x

            self.le_X0.setText(a[1])
            self.le_X1.setText(a[2])
            self.le_Y0.setText(a[3])
            self.le_Y1.setText(a[4])
            if a[5] == 'True':
                self.arq_ok = True
            self.le_input.setText(a[0])

    def save_arquivo(self):
        self.dados['entrada'] = self.le_input.text()
        self.dados['X0'] = self.le_X0.text()
        self.dados['X1'] = self.le_X1.text()
        self.dados['Y0'] = self.le_Y0.text()
        self.dados['Y1'] = self.le_Y1.text()
        self.dados['controle'] = "True"

        arq = QFileDialog.getSaveFileName(
            dir="Dados", filter='Arquivo DAT (*.dat)')[0]
        arquivo = arq.rsplit('.dat')

        with open(arquivo[0] + '.dat', 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([self.dados['entrada'],
                            self.dados['X0'],
                            self.dados['X1'],
                            self.dados['Y0'],
                            self.dados['Y1'],
                            self.dados['controle']])

    def show_message(self):
        self.msg = QMessageBox()
        self.msg.setIcon(QMessageBox.Warning)
        self.msg.setWindowTitle('Atenção!')
        self.msg.setText(
            "Carregue um Arquivo ou edite os campos")
        self.msg.exec()

    def inc_dec(self):
        self.le_input.setText(str(self.hs_input.value()))

    def updSlider(self):
        gr_ValInput = self.str_to_float(self.le_input.text())
        self.hs_input.setValue(int(round(gr_ValInput, 3)))

    def str_to_float(self, entrada):
        valor = entrada
        try:
            valor = round(float(valor), 3)
            return valor
        except ValueError:
            valor = 0.0
            return valor

    def valores_float(self):
        grInput = self.str_to_float(self.le_input.text())
        grX0 = self.str_to_float(self.le_X0.text())
        grX1 = self.str_to_float(self.le_X1.text())
        grY0 = self.str_to_float(self.le_Y0.text())
        grY1 = self.str_to_float(self.le_Y1.text())
        grOutput = self.str_to_float(self.le_output.text())

        lista = [grInput, grX0, grX1, grY0, grY1, grOutput]

        return lista

    def inicio(self):
        grInput, grX0, grX1, grY0, grY1, grOutput = self.valores_float()
        if grX1 > grX0:            
            self.hs_input.setMinimum(int(grX1 - (grX1 * 1.5)))
            self.hs_input.setMaximum(int(grX1 + (grX1 * 0.5)))
            self.hs_input.setValue(int(self.le_input.text()))
        else:
            self.hs_input.setMinimum(int(grX0 - (grX0 * 1.5)))
            self.hs_input.setMaximum(int(grX0 + (grX0 * 0.5)))
            self.hs_input.setValue(int(self.le_input.text()))

        if grY0 > grY1:
            self.ax.set_ylim([(grY0-(grY0*1.55)), (grY0+(grY0*0.55))])
        else:
            self.ax.set_ylim([(grY1-(grY1*1.55)), (grY1+(grY1*0.55))])
        if grX0 > grX1:
            self.ax.set_xlim([(grX0 - (grX0 * 1.55)), (grX0 + (grX0 * 0.55))])
        else:
            self.ax.set_xlim([(grX1 - (grX1 * 1.55)), (grX1 + (grX1 * 0.55))])

        self.ax.plot(grX0, grX1, grY0, grY1)
        self.ax.scatter(0.0, grOutput, s=20, edgecolor='black')
        self.ax.set_aspect(0.5/self.ax.get_data_ratio())
        self.ax_new = None
        self.iniciou = True


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()

    app.setStyle('Fusion')
    apply_stylesheet(app, theme='dark_teal.xml')

    window.show()
    sys.exit(app.exec())
