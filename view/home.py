from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFormLayout, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QMainWindow, QMenuBar,
    QPushButton, QRadioButton, QSizePolicy, QSpacerItem,
    QSpinBox, QStatusBar, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget, QMessageBox)

from infra.repository.aposta_repository import ApostaRepository
from infra.entities.aposta import Aposta
from infra.configs.connection import DBConnectionHandler
import random

class Home(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(998, 885)

        conn = DBConnectionHandler()

        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.widget_5 = QWidget(self.widget)
        self.widget_5.setObjectName(u"widget_5")
        self.verticalLayout_3 = QVBoxLayout(self.widget_5)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.lbl_titulo = QLabel(self.widget_5)
        self.lbl_titulo.setObjectName(u"lbl_titulo")

        self.verticalLayout_3.addWidget(self.lbl_titulo)


        self.verticalLayout_2.addWidget(self.widget_5)

        self.widget_3 = QWidget(self.widget)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setMaximumSize(QSize(16777215, 16777215))
        self.formLayout = QFormLayout(self.widget_3)
        self.formLayout.setObjectName(u"formLayout")
        self.lbl_nome = QLabel(self.widget_3)
        self.lbl_nome.setObjectName(u"lbl_nome")
        font = QFont()
        font.setPointSize(10)
        self.lbl_nome.setFont(font)

        self.formLayout.setWidget(0, QFormLayout.SpanningRole, self.lbl_nome)

        self.txt_nome = QLineEdit(self.widget_3)
        self.txt_nome.setObjectName(u"txt_nome")
        self.txt_nome.setMaximumSize(QSize(500, 16777215))
        self.txt_nome.setFont(font)

        self.formLayout.setWidget(1, QFormLayout.SpanningRole, self.txt_nome)

        self.lbl_vencedor = QLabel(self.widget_3)
        self.lbl_vencedor.setObjectName(u"lbl_vencedor")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.lbl_vencedor)

        self.radio_casa = QRadioButton(self.widget_3)
        self.radio_casa.setObjectName(u"radio_casa")
        self.radio_casa.setFont(font)

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.radio_casa)

        self.radio_visitante = QRadioButton(self.widget_3)
        self.radio_visitante.setObjectName(u"radio_visitante")
        self.radio_visitante.setFont(font)

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.radio_visitante)

        self.lbl_placar = QLabel(self.widget_3)
        self.lbl_placar.setObjectName(u"lbl_placar")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.lbl_placar)

        self.lbl_casa = QLabel(self.widget_3)
        self.lbl_casa.setObjectName(u"lbl_casa")

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.lbl_casa)

        self.sb_casa = QSpinBox(self.widget_3)
        self.sb_casa.setObjectName(u"sb_casa")
        self.sb_casa.setMaximumSize(QSize(50, 16777215))
        self.sb_casa.setMaximum(5)

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.sb_casa)

        self.lbl_visitante = QLabel(self.widget_3)
        self.lbl_visitante.setObjectName(u"lbl_visitante")

        self.formLayout.setWidget(7, QFormLayout.FieldRole, self.lbl_visitante)

        self.sb_visitante = QSpinBox(self.widget_3)
        self.sb_visitante.setObjectName(u"sb_visitante")
        self.sb_visitante.setMaximumSize(QSize(50, 16777215))
        self.sb_visitante.setMaximum(5)

        self.formLayout.setWidget(8, QFormLayout.FieldRole, self.sb_visitante)

        self.lbl_valor_aposta_2 = QLabel(self.widget_3)
        self.lbl_valor_aposta_2.setObjectName(u"lbl_valor_aposta_2")

        self.formLayout.setWidget(9, QFormLayout.SpanningRole, self.lbl_valor_aposta_2)

        self.sb_valor_aposta = QSpinBox(self.widget_3)
        self.sb_valor_aposta.setObjectName(u"sb_valor_aposta")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sb_valor_aposta.sizePolicy().hasHeightForWidth())
        self.sb_valor_aposta.setSizePolicy(sizePolicy)
        self.sb_valor_aposta.setMaximumSize(QSize(150, 16777215))
        self.sb_valor_aposta.setMaximum(999999999)
        self.sb_valor_aposta.setValue(0)

        self.formLayout.setWidget(11, QFormLayout.SpanningRole, self.sb_valor_aposta)

        self.widget_7 = QWidget(self.widget_3)
        self.widget_7.setObjectName(u"widget_7")
        self.horizontalLayout = QHBoxLayout(self.widget_7)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.btn_adicionar_aposta = QPushButton(self.widget_7)
        self.btn_adicionar_aposta.setObjectName(u"btn_adicionar_aposta")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btn_adicionar_aposta.sizePolicy().hasHeightForWidth())
        self.btn_adicionar_aposta.setSizePolicy(sizePolicy1)
        self.btn_adicionar_aposta.setMinimumSize(QSize(300, 30))
        self.btn_adicionar_aposta.setMaximumSize(QSize(300, 16777215))
        self.btn_adicionar_aposta.setFont(font)
        self.btn_adicionar_aposta.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout.addWidget(self.btn_adicionar_aposta)


        self.formLayout.setWidget(12, QFormLayout.FieldRole, self.widget_7)


        self.verticalLayout_2.addWidget(self.widget_3)


        self.verticalLayout.addWidget(self.widget)

        self.widget_2 = QWidget(self.centralwidget)
        self.widget_2.setObjectName(u"widget_2")
        self.verticalLayout_4 = QVBoxLayout(self.widget_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.lbl_ganhador = QLabel(self.widget_2)
        self.lbl_ganhador.setObjectName(u"lbl_ganhador")

        self.verticalLayout_4.addWidget(self.lbl_ganhador, 0, Qt.AlignHCenter)

        self.btn_gerar_resultado = QPushButton(self.widget_2)
        self.btn_gerar_resultado.setObjectName(u"btn_gerar_resultado")
        self.btn_gerar_resultado.setFont(font)

        self.verticalLayout_4.addWidget(self.btn_gerar_resultado)


        self.verticalLayout.addWidget(self.widget_2)

        self.widget_6 = QWidget(self.centralwidget)
        self.widget_6.setObjectName(u"widget_6")
        self.verticalLayout_6 = QVBoxLayout(self.widget_6)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_quantidade_apostadores = QLabel(self.widget_6)
        self.label_quantidade_apostadores.setObjectName(u"label_quantidade_apostadores")
        self.label_quantidade_apostadores.setFont(font)

        self.verticalLayout_5.addWidget(self.label_quantidade_apostadores)

        self.tb_apostas = QTableWidget(self.widget_6)
        if (self.tb_apostas.columnCount() < 3):
            self.tb_apostas.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.tb_apostas.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tb_apostas.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tb_apostas.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.tb_apostas.setObjectName(u"tb_apostas")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.tb_apostas.sizePolicy().hasHeightForWidth())
        self.tb_apostas.setSizePolicy(sizePolicy2)
        self.tb_apostas.setFont(font)
        self.tb_apostas.horizontalHeader().setDefaultSectionSize(291)

        self.verticalLayout_5.addWidget(self.tb_apostas)


        self.verticalLayout_6.addLayout(self.verticalLayout_5)


        self.verticalLayout.addWidget(self.widget_6)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 998, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

        self.btn_adicionar_aposta.clicked.connect(self.criar_aposta)
        self.btn_gerar_resultado.clicked.connect(self.gerar_resultado)
        self.popula_quantidade_apostadores()
        self.popula_tabela_apostas("", "")

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.lbl_titulo.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:28pt; font-weight:600;\">365bet</span></p></body></html>", None))
        self.lbl_nome.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Nome completo</p></body></html>", None))
        self.txt_nome.setInputMask("")
        self.lbl_vencedor.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt;\">Vencedor:</span></p></body></html>", None))
        self.radio_casa.setText(QCoreApplication.translate("MainWindow", u"Casa", None))
        self.radio_visitante.setText(QCoreApplication.translate("MainWindow", u"Visitante", None))
        self.lbl_placar.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt;\">Placar:</span></p></body></html>", None))
        self.lbl_casa.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt;\">Casa</span></p></body></html>", None))
        self.lbl_visitante.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt;\">Visitante</span></p></body></html>", None))
        self.lbl_valor_aposta_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt;\">Valor da aposta</span></p></body></html>", None))
        self.btn_adicionar_aposta.setText(QCoreApplication.translate("MainWindow", u"Adicionar aposta", None))
        self.lbl_ganhador.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt;\">Ganhador: </span></p></body></html>", None))
        self.btn_gerar_resultado.setText(QCoreApplication.translate("MainWindow", u"Gerar resultado", None))
        self.label_quantidade_apostadores.setText(QCoreApplication.translate("MainWindow", u"Quantidade de Apostadores", None))
        ___qtablewidgetitem = self.tb_apostas.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Nome", None));
        ___qtablewidgetitem1 = self.tb_apostas.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Aposta", None));
        ___qtablewidgetitem2 = self.tb_apostas.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Valor Ganho", None));

    def criar_aposta(self):
        db = ApostaRepository()

        if ((self.radio_casa.isChecked() or self.radio_visitante.isChecked()) and self.txt_nome.text() != ""
                and self.sb_valor_aposta.text() != "0"):
            if ((self.radio_casa.isChecked() and self.sb_casa.text() < self.sb_visitante.text()) or
                    (self.radio_visitante.isChecked() and self.sb_casa.text() > self.sb_visitante.text()) or
                    (self.sb_casa.text() == self.sb_visitante.text())):
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setWindowTitle('Erro ao criar aposta')
                msg.setText(f'FAZ DIREITO O NEGÓCIO')
                msg.exec()
            else:
                aposta = Aposta(
                    nome_apostador=self.txt_nome.text(),
                    time_casa=self.sb_casa.text(),
                    time_visitante=self.sb_visitante.text(),
                    valor_aposta=self.sb_valor_aposta.text(),
                    vencedor="Casa" if self.radio_casa.isChecked() else "Visitante"
                )

                retorno = db.insert(aposta)
                if retorno == "OK":
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Information)
                    msg.setWindowTitle('Cadastro realizado')
                    msg.setText('Cadastro realizado com sucesso')
                    msg.exec()

                    self.lbl_ganhador.setText("Ganhador:")
                    self.btn_gerar_resultado.setEnabled(True)
                    self.popula_quantidade_apostadores()
                    self.popula_tabela_apostas("", "")
                    self.limpar_campos()
                else:
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Critical)
                    msg.setWindowTitle('Erro ao cadastrar')
                    msg.setText(f'Erro ao cadastrar a aposta, verifique os dados')
                    msg.exec()
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setWindowTitle('Erro ao criar aposta')
            msg.setText(f'Preencha os campos corretamente!')
            msg.exec()

    def popula_quantidade_apostadores(self):
        db = ApostaRepository()
        apostas = db.select_all()

        self.label_quantidade_apostadores.setText(f"Quantidade de Apostadores: {len(apostas)}")

    def gerar_resultado(self):
        placar = self.gerar_placar()
        vencedor = self.validar_vencedor(placar)
        self.popula_tabela_apostas(placar, vencedor)
        self.btn_gerar_resultado.setEnabled(False)
        db = ApostaRepository()
        db.delete_all()

    def gerar_placar(self):
        gols_casa = random.randint(0, 5)
        gols_vistante = random.randint(0, 5)

        placar = [
            {"time": "Casa", "gols": gols_casa},
            {"time": "Visitante", "gols": gols_vistante}
        ]

        return placar

    def validar_vencedor(self, placar):
        if placar[0]['gols'] > placar[1]['gols']:
            self.lbl_ganhador.setText(f"Ganhador: {placar[0]['time']}, Placar: {placar[0]['gols']}x{placar[1]['gols']}")
            return placar[0]['time']
        elif placar[1]['gols'] > placar[0]['gols']:
            self.lbl_ganhador.setText(f"Ganhador: {placar[1]['time']}, Placar: {placar[0]['gols']}x{placar[1]['gols']}")
            return placar[1]['time']
        else:
            self.lbl_ganhador.setText(f"Ganhador: NINGUÉM, EMPATOU HUAHUAHUA")
            return "Empate"

    def popula_tabela_apostas(self, placar, vencedor):
        self.tb_apostas.setRowCount(0)
        db = ApostaRepository()
        lista_apostas = db.select_all()
        self.tb_apostas.setRowCount(len(lista_apostas))

        for linha, aposta in enumerate(lista_apostas):
            valoresNota = []
            if (placar != "" and vencedor != ""):
                if (vencedor == aposta.vencedor):
                    if (placar[0]['gols'] == aposta.time_casa and placar[1]['gols'] == aposta.time_visitante):
                        valoresNota = [aposta.nome_apostador, aposta.valor_aposta, aposta.valor_aposta * 2]
                    else:
                        valoresNota = [aposta.nome_apostador, aposta.valor_aposta, aposta.valor_aposta * 1.5]
                else:
                    valoresNota = [aposta.nome_apostador, aposta.valor_aposta, 0]
            else:
                valoresNota = [aposta.nome_apostador, aposta.valor_aposta]

            for coluna, valor in enumerate(valoresNota):
                item = QTableWidgetItem(str(valor))
                self.tb_apostas.setItem(linha, coluna, item)
                self.tb_apostas.item(linha, coluna)

    def limpar_campos(self):
        for widget in self.widget_3.children():
            if isinstance(widget, QLineEdit):
                widget.setText("")
            elif isinstance(widget, QSpinBox):
                widget.setValue(0)
            elif isinstance(widget, QRadioButton):
                widget.setChecked(False)




