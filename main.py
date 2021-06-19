import math
import random
import re
import sys
import scipy
import zlib
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from scipy.stats import laplace
from model import Ui_model


class ExampleApp(QtWidgets.QMainWindow, Ui_model):
    def __init__(self, log_uncaught_exceptions=None):
        super().__init__()
        self.setupUi(self)
        self.data = None
        self.setFixedSize(896, 662)
        self.pushButton_5.clicked.connect(self.on_clicked_IS)  # Метод кнопки 'ИС'
        self.pushButton_3.clicked.connect(self.on_clicked_START)  # Метод кнопки 'START'
        self.file_name = ""
        sys.excepthook = log_uncaught_exceptions

    def on_clicked_IS(self):
        fname, _ = QtWidgets.QFileDialog.getOpenFileName(self, 'Open File', './')

        if fname.endswith("txt"):
            slova = {'\n': '00000000', 'Ƒ': '00000001', 'ƕ': '00000010', 'ƒ': '00000011', 'Ɠ': '00000100',
                     'Ɣ': '00000101',
                     'Ɩ': '00000110', 'Ɨ': '00000111', 'Ƙ': '00001000', 'ƙ': '00001001', 'ƚ': '00001010',
                     'ƛ': '00001011',
                     'Ɯ': '00001100', 'Ɲ': '00001101', 'ƞ': '00001110', 'Ɵ': '00001111', 'Ơ': '00010000',
                     'ơ': '00010001',
                     'Ƣ': '00010010', 'ƣ': '00010011', 'Ƥ': '00010100', 'ƥ': '00010101', 'Ʀ': '00010110',
                     'Ƨ': '00010111',
                     'ƨ': '00011000', 'Ʃ': '00011001', 'ƪ': '00011010', 'ƫ': '00011011', 'Ƭ': '00011100',
                     'ƭ': '00011101',
                     'Ʈ': '00011110', 'Ư': '00011111', ' ': '00100000', '!': '00100001', '"': '00100010',
                     '#': '00100011',
                     '$': '00100100', '%': '00100101', '&': '00100110', "'": "00100111", '(': '00101000',
                     ')': '00101001',
                     '*': '00101010', '+': '00101011', ',': '00101100', '-': '00101101', '.': '00101110',
                     '/': '00101111',
                     '0': '00110000', '1': '00110001', '2': '00110010', '3': '00110011', '4': '00110100',
                     '5': '00110101',
                     '6': '00110110', '7': '00110111', '8': '00111000', '9': '00111001', ':': '00111010',
                     ';': '00111011',
                     '<': '00111100', '=': '00111101', '>': '00111110', '?': '00111111', '@': '01000000',
                     'A': '01000001', 'B': '01000010', 'C': '01000011', 'D': '01000100', 'E': '01000101',
                     'F': '01000110',
                     'G': '01000111', 'H': '01001000', 'I': '01001001', 'J': '01001010', 'K': '01001011',
                     'L': '01001100',
                     'M': '01001101', 'N': '01001110', 'O': '01001111', 'P': '01010000', 'Q': '01010001',
                     'R': '01010010',
                     'S': '01010011', 'T': '01010100', 'U': '01010101', 'V': '01010110', 'W': '01010111',
                     'X': '01011000',
                     'Y': '01011001', 'Z': '01011010', '[': '01011011', '\\': '01011100', ']': '01011101',
                     '^': '01011110',
                     '_': '01011111', '`': '01100000',
                     'a': '01100001', 'b': '01100010', 'c': '01100011', 'd': '01100100', 'e': '01100101',
                     'f': '01100110',
                     'g': '01100111', 'h': '01101000', 'i': '01101001', 'j': '01101010', 'k': '01101011',
                     'l': '01101100',
                     'm': '01101101', 'n': '01101110', 'o': '01101111', 'p': '01110000', 'q': '01110001',
                     'r': '01110010',
                     's': '01110011', 't': '01110100', 'u': '01110101', 'v': '01110110', 'w': '01110111',
                     'x': '01111000',
                     'y': '01111001', 'z': '01111010', '{': '01111011', '|': '01111100', '}': '01111101',
                     '~': '01111110',
                     '': '01111111', 'Ђ': '10000000', 'Ѓ': '10000001', '‚': '10000010', 'ѓ': '10000011',
                     '„': '10000100',
                     '…': '10000101', '†': '10000110', '‡': '10000111',
                     '€': '10001000', '‰': '10001001', 'Љ': '10001010', '‹': '10001011', 'Њ': '10001100',
                     'Ќ': '10001101',
                     'Ћ': '10001110', 'Џ': '10001111', 'ђ': '10010000', '‘': '10010001', '’': '10010010',
                     '“': '10010011',
                     '”': '10010100', '•': '10010101', '–': '10010110', '—': '10010111', '': '10011000',
                     '™': '10011001',
                     'љ': '10011010', '›': '10011011', 'њ': '10011100', 'ќ': '10011101', 'ћ': '10011110',
                     'џ': '10011111',
                     'ª': '10100000', 'Ў': '10100001', 'ў': '10100010', 'Ј': '10100011', '¤': '10100100',
                     'Ґ': '10100101',
                     '¦': '10100110', '§': '10100111', 'Ё': '10101000', '©': '10101001', 'Є': '10101010',
                     '«': '10101011',
                     '¬': '10101100', 'Ʋ': '10101101', '®': '10101110', 'Ї': '10101111', '°': '10110000',
                     '±': '10110001',
                     'І': '10110010', 'і': '10110011',
                     'ґ': '10110100', 'µ': '10110101', '¶': '10110110', '·': '10110111', 'ё': '10111000',
                     '№': '10111001',
                     'є': '10111010', '»': '10111011', 'ј': '10111100', 'Ѕ': '10111101', 'ѕ': '10111110',
                     'ї': '10111111',
                     'А': '11000000', 'Б': '11000001', 'В': '11000010', 'Г': '11000011', 'Д': '11000100',
                     'Е': '11000101',
                     'Ж': '11000110', 'З': '11000111', 'И': '11001000', 'Й': '11001001', 'К': '11001010',
                     'Л': '11001011',
                     'М': '11001100', 'Н': '11001101', 'О': '11001110', 'П': '11001111', 'Р': '11010000',
                     'С': '11010001',
                     'Т': '11010010', 'У': '11010011', 'Ф': '11010100', 'Х': '11010101', 'Ц': '11010110',
                     'Ч': '11010111',
                     'Ш': '11011000', 'Щ': '11011001', 'Ъ': '11011010', 'Ы': '11011011', 'Ь': '11011100',
                     'Э': '11011101',
                     'Ю': '11011110', 'Я': '11011111',
                     'а': '11100000', 'б': '11100001', 'в': '11100010', 'г': '11100011', 'д': '11100100',
                     'е': '11100101',
                     'ж': '11100110', 'з': '11100111', 'и': '11101000', 'й': '11101001', 'к': '11101010',
                     'л': '11101011',
                     'м': '11101100', 'н': '11101101', 'о': '11101110', 'п': '11101111', 'р': '11110000',
                     'с': '11110001',
                     'т': '11110010', 'у': '11110011', 'ф': '11110100', 'х': '11110101', 'ц': '11110110',
                     'ч': '11110111',
                     'ш': '11111000', 'щ': '11111001', 'ъ': '11111010', 'ы': '11111011', 'ь': '11111100',
                     'э': '11111101',
                     'ю': '11111110', 'я': '11111111'}
            inv_slova = {value: key for key, value in slova.items()}

            U_sh = self.doubleSpinBox.value()  # уровень шума
            f = self.doubleSpinBox_5.value()  # частота шума
            u = self.doubleSpinBox_2.value()  # скорость передачи, Бод
            bod = self.doubleSpinBox_4.value()  # уровень полезного сигнала

            razmerbloka = int(self.comboBox.currentText())  # Размер блока
            povtor_isk_blocks = self.doubleSpinBox_7.value()  # Повтор искаженных блоков (0 - 10)

            df = (f * 1000) / 20
            n0 = (U_sh ** 2) / df
            e = (u ** 2) / bod
            asda = (math.sqrt((2 * e) / n0))
            p_bitosh = ((1 - ((scipy.stats.norm.cdf(asda / math.sqrt(2)) - 0.5) * 2)) / 2)
            p_bitpr = 1 - p_bitosh
            with open('text_file.txt', encoding='utf-8') as f:
                stroka_faila = str(f.read())
            kod_stroki_faila = ""
            for i in stroka_faila:
                kod_stroki_faila += slova[i]

            spisok_istochnika_block = re.findall(r'\d' * razmerbloka, kod_stroki_faila)
            spisok_istochnika_byte = []
            for i in spisok_istochnika_block:
                spisok_istochnika_byte.append(re.findall(r'\d' * 8, i))

            def chunk_based_on_size(lst, n):
                for x in range(0, len(lst), n):
                    each_chunk = lst[x: n + x]

                    if len(each_chunk) < n:
                        each_chunk = each_chunk + [None for y in range(n - len(each_chunk))]
                    yield each_chunk

            def oshibki(spisok, p_bitpr):
                stroka_oshibok = ''
                for i in spisok:
                    for y in i:
                        for z in y:
                            if p_bitpr <= random.random():
                                stroka_oshibok += "1"
                            else:
                                stroka_oshibok += "0"
                return stroka_oshibok

            stroka_oshibok_block = oshibki(spisok_istochnika_byte, p_bitpr)
            spisok_oshibok_block = re.findall(r'\d' * razmerbloka, stroka_oshibok_block)
            spisok_oshibok_byte = []
            for i in spisok_oshibok_block:
                spisok_oshibok_byte.append(re.findall(r'\d' * 8, i))
            byteee = 0
            block11 = 0
            for i in spisok_oshibok_byte:
                for y in i:
                    if y != "00000000":
                        byteee += 1
            for i in spisok_oshibok_block:
                if i != "0" * razmerbloka:
                    block11 += 1
            m_povt = 0
            stroka_priemnika_block = ''
            for i in range(len(spisok_istochnika_block)):
                for x in range(razmerbloka):
                    stroka_priemnika_block += str(int(spisok_istochnika_block[i][x]) ^ int(spisok_oshibok_block[i][x]))
            spisok_priemnika_block = re.findall(r'\d' * razmerbloka, stroka_priemnika_block)
            spisok_priemnika_byte = []
            for i in spisok_priemnika_block:
                spisok_priemnika_byte.append(re.findall(r'\d' * 8, i))
            for e in range(int(povtor_isk_blocks)):
                spisok_priemnika_AP_block1 = []
                pov = 0
                osh_bit = 0
                for i, j in zip(spisok_priemnika_byte, enumerate(spisok_istochnika_byte)):
                    spisok_priemnika_AP_block = []
                    for y, z in zip(i, j[1]):
                        if zlib.crc32(y.encode('utf-8')) == zlib.crc32(z.encode('utf-8')):
                            spisok_priemnika_AP_block.append(z)
                        else:
                            spisok_priemnika_AP_block.append('')
                    indeksi_block = []
                    indeksi_block = [i for i, ltr in enumerate(spisok_priemnika_AP_block) if ltr == '']
                    povtor_kodovih_kombinaci_block = []
                    for x in indeksi_block:
                        povtor_kodovih_kombinaci_block.append(spisok_istochnika_byte[j[0]][x])
                    pov += len(povtor_kodovih_kombinaci_block)
                    stroka_oshibok_povtor_block = oshibki(povtor_kodovih_kombinaci_block, p_bitpr)
                    spisok_oshibok_povtor_byte = re.findall(r'\d' * 8,
                                                            stroka_oshibok_povtor_block)  # Количество ошибок блок
                    stroka_priemnika1_block = ''
                    for asd in range(len(povtor_kodovih_kombinaci_block)):
                        for x in range(8):
                            stroka_priemnika1_block += str(
                                int(povtor_kodovih_kombinaci_block[asd][x]) ^ int(spisok_oshibok_povtor_byte[asd][x]))
                    spisok_priemnika1_block = re.findall(r'\d' * 8, stroka_priemnika1_block)
                    for ind, ja in zip(indeksi_block, spisok_priemnika1_block):
                        spisok_priemnika_AP_block[ind] = ja
                    spisok_priemnika_AP_block1.append(spisok_priemnika_AP_block)
                    spisok_priemnika_byte = spisok_priemnika_AP_block1
                    osh_bit += stroka_oshibok_povtor_block.count('1')
                    m_povt += len(povtor_kodovih_kombinaci_block)

            a1 = 0
            a2 = 0
            a3 = 0
            for i, j in zip(spisok_priemnika_byte, spisok_istochnika_byte):
                if i != j:
                    a1 += 1
                for y, z in zip(i, j):
                    if y != z:
                        a2 += 1
                    for g, s in zip(y, z):
                        if g != s:
                            a3 += 1
            kod = ''
            for i in spisok_priemnika_block:
                for y in i:
                    kod += y
            kod = re.findall(r'\d' * 8, kod)
            kod1 = ''
            for x in kod:
                kod1 += inv_slova[x]
            with open('text_file2.txt', 'w', encoding="utf-8") as f:
                f.write(kod1)

            if povtor_isk_blocks == 0:
                self.lineEdit.setText(str(len(kod_stroki_faila)))  # Принято бит
                self.lineEdit_9.setText(str(int(len(kod_stroki_faila) / 8)))  # Принято байт
                self.lineEdit_2.setText(str(byteee))  # Ошибки байт
                self.lineEdit_4.setText(str(stroka_oshibok_block.count('1')))  # Ошибки бит
                self.lineEdit_8.setText(str(len(spisok_istochnika_block)))  # Блоки 1
                self.lineEdit_5.setText(str(int(block11)))  # Блоки 2
                self.lineEdit_6.setText(str(int(block11) / len(spisok_istochnika_block)))  # Блок, коэф. ошибки
                self.lineEdit_7.setText(
                    str(stroka_oshibok_block.count('1') / len(kod_stroki_faila)))   # коэф. ошибки, бит
                self.lineEdit_3.setText(str(byteee / (len(kod_stroki_faila) / 8)))  # коэф. ошибки, байт
                n_bb = int(razmerbloka) / 8
                m_povt = 0
                B_poln = int(
                    ((len(kod_stroki_faila) - stroka_oshibok_block.count('1')) / (len(kod_stroki_faila))) * bod)
                self.lineEdit_11.setText(str(B_poln))
                self.lineEdit_10.setText(str(m_povt))
            else:
                self.lineEdit.setText(str(len(kod_stroki_faila)))  # Принято бит
                self.lineEdit_9.setText(str(int(len(kod_stroki_faila) / 8)))  # Принято байт
                self.lineEdit_2.setText(str(a2))  # Ошибки байт
                self.lineEdit_4.setText(str(a3))  # Ошибки бит
                self.lineEdit_8.setText(str(len(spisok_istochnika_block)))  # Блоки 1
                self.lineEdit_5.setText(str(a1))  # Блоки 2
                self.lineEdit_6.setText(str(a1 / len(spisok_istochnika_block)))  # Блок, коэф. ошибки
                self.lineEdit_7.setText(str((a3 / len(kod_stroki_faila))))  # коэф. ошибки, бит
                self.lineEdit_3.setText(str((a2 / (len(kod_stroki_faila) / 8))))  # коэф. ошибки, байт
                n_bb = int(razmerbloka) / 8
                B_poln = int(((len(kod_stroki_faila) - a3) / (len(kod_stroki_faila) + m_povt * n_bb * 8)) * bod)
                self.lineEdit_11.setText(str(B_poln))
                self.lineEdit_10.setText(str(m_povt))

        # проверка чекбокса на моделирование аварии
        if self.checkBox_2.isChecked():
            bits_value = self.lineEdit_4.text()
            bytes_value = self.lineEdit_2.text()
            blocks_value = self.lineEdit_5.text()

            if (int(bits_value) > 0) or (int(bytes_value) > 0) or (int(blocks_value) > 0):
                QMessageBox.critical(self, "АВАРИЯ", "Произошла авария", QMessageBox.Ok)

        self.file_name = fname  # записываем название файла в глобальную переменную

    def on_clicked_START(self):  # После выбора значений, по нажатию 'START', считает 'p_bitosh'
        U_sh = self.doubleSpinBox.value()  # уровень шума
        f = self.doubleSpinBox_5.value()  # частота шума
        u = self.doubleSpinBox_2.value()  # скорость передачи, Бод
        bod = self.doubleSpinBox_4.value()  # уровень полезного сигнала

        df = (f * 1000) / 20  # полоса частот
        n0 = (U_sh ** 2) / df
        e = (u ** 2) / bod
        asda = (math.sqrt((2 * e) / n0))
        p_bitosh = ((1 - ((scipy.stats.norm.cdf(asda / math.sqrt(2)) - 0.5) * 2)) / 2)
        p_bitpr = 1 - p_bitosh

        fname = self.file_name  # записываем название файла в локальную переменную

        if fname.endswith("txt"):  # Открываем *.txt файл на считывание
            slova = {'\n': '00000000', 'Ƒ': '00000001', 'ƕ': '00000010', 'ƒ': '00000011', 'Ɠ': '00000100',
                     'Ɣ': '00000101',
                     'Ɩ': '00000110', 'Ɨ': '00000111', 'Ƙ': '00001000', 'ƙ': '00001001', 'ƚ': '00001010',
                     'ƛ': '00001011',
                     'Ɯ': '00001100', 'Ɲ': '00001101', 'ƞ': '00001110', 'Ɵ': '00001111', 'Ơ': '00010000',
                     'ơ': '00010001',
                     'Ƣ': '00010010', 'ƣ': '00010011', 'Ƥ': '00010100', 'ƥ': '00010101', 'Ʀ': '00010110',
                     'Ƨ': '00010111',
                     'ƨ': '00011000', 'Ʃ': '00011001', 'ƪ': '00011010', 'ƫ': '00011011', 'Ƭ': '00011100',
                     'ƭ': '00011101',
                     'Ʈ': '00011110', 'Ư': '00011111', ' ': '00100000', '!': '00100001', '"': '00100010',
                     '#': '00100011',
                     '$': '00100100', '%': '00100101', '&': '00100110', "'": "00100111", '(': '00101000',
                     ')': '00101001',
                     '*': '00101010', '+': '00101011', ',': '00101100', '-': '00101101', '.': '00101110',
                     '/': '00101111',
                     '0': '00110000', '1': '00110001', '2': '00110010', '3': '00110011', '4': '00110100',
                     '5': '00110101',
                     '6': '00110110', '7': '00110111', '8': '00111000', '9': '00111001', ':': '00111010',
                     ';': '00111011',
                     '<': '00111100', '=': '00111101', '>': '00111110', '?': '00111111', '@': '01000000',
                     'A': '01000001', 'B': '01000010', 'C': '01000011', 'D': '01000100', 'E': '01000101',
                     'F': '01000110',
                     'G': '01000111', 'H': '01001000', 'I': '01001001', 'J': '01001010', 'K': '01001011',
                     'L': '01001100',
                     'M': '01001101', 'N': '01001110', 'O': '01001111', 'P': '01010000', 'Q': '01010001',
                     'R': '01010010',
                     'S': '01010011', 'T': '01010100', 'U': '01010101', 'V': '01010110', 'W': '01010111',
                     'X': '01011000',
                     'Y': '01011001', 'Z': '01011010', '[': '01011011', '\\': '01011100', ']': '01011101',
                     '^': '01011110',
                     '_': '01011111', '`': '01100000',
                     'a': '01100001', 'b': '01100010', 'c': '01100011', 'd': '01100100', 'e': '01100101',
                     'f': '01100110',
                     'g': '01100111', 'h': '01101000', 'i': '01101001', 'j': '01101010', 'k': '01101011',
                     'l': '01101100',
                     'm': '01101101', 'n': '01101110', 'o': '01101111', 'p': '01110000', 'q': '01110001',
                     'r': '01110010',
                     's': '01110011', 't': '01110100', 'u': '01110101', 'v': '01110110', 'w': '01110111',
                     'x': '01111000',
                     'y': '01111001', 'z': '01111010', '{': '01111011', '|': '01111100', '}': '01111101',
                     '~': '01111110',
                     '': '01111111', 'Ђ': '10000000', 'Ѓ': '10000001', '‚': '10000010', 'ѓ': '10000011',
                     '„': '10000100',
                     '…': '10000101', '†': '10000110', '‡': '10000111',
                     '€': '10001000', '‰': '10001001', 'Љ': '10001010', '‹': '10001011', 'Њ': '10001100',
                     'Ќ': '10001101',
                     'Ћ': '10001110', 'Џ': '10001111', 'ђ': '10010000', '‘': '10010001', '’': '10010010',
                     '“': '10010011',
                     '”': '10010100', '•': '10010101', '–': '10010110', '—': '10010111', '': '10011000',
                     '™': '10011001',
                     'љ': '10011010', '›': '10011011', 'њ': '10011100', 'ќ': '10011101', 'ћ': '10011110',
                     'џ': '10011111',
                     'ª': '10100000', 'Ў': '10100001', 'ў': '10100010', 'Ј': '10100011', '¤': '10100100',
                     'Ґ': '10100101',
                     '¦': '10100110', '§': '10100111', 'Ё': '10101000', '©': '10101001', 'Є': '10101010',
                     '«': '10101011',
                     '¬': '10101100', 'Ʋ': '10101101', '®': '10101110', 'Ї': '10101111', '°': '10110000',
                     '±': '10110001',
                     'І': '10110010', 'і': '10110011',
                     'ґ': '10110100', 'µ': '10110101', '¶': '10110110', '·': '10110111', 'ё': '10111000',
                     '№': '10111001',
                     'є': '10111010', '»': '10111011', 'ј': '10111100', 'Ѕ': '10111101', 'ѕ': '10111110',
                     'ї': '10111111',
                     'А': '11000000', 'Б': '11000001', 'В': '11000010', 'Г': '11000011', 'Д': '11000100',
                     'Е': '11000101',
                     'Ж': '11000110', 'З': '11000111', 'И': '11001000', 'Й': '11001001', 'К': '11001010',
                     'Л': '11001011',
                     'М': '11001100', 'Н': '11001101', 'О': '11001110', 'П': '11001111', 'Р': '11010000',
                     'С': '11010001',
                     'Т': '11010010', 'У': '11010011', 'Ф': '11010100', 'Х': '11010101', 'Ц': '11010110',
                     'Ч': '11010111',
                     'Ш': '11011000', 'Щ': '11011001', 'Ъ': '11011010', 'Ы': '11011011', 'Ь': '11011100',
                     'Э': '11011101',
                     'Ю': '11011110', 'Я': '11011111',
                     'а': '11100000', 'б': '11100001', 'в': '11100010', 'г': '11100011', 'д': '11100100',
                     'е': '11100101',
                     'ж': '11100110', 'з': '11100111', 'и': '11101000', 'й': '11101001', 'к': '11101010',
                     'л': '11101011',
                     'м': '11101100', 'н': '11101101', 'о': '11101110', 'п': '11101111', 'р': '11110000',
                     'с': '11110001',
                     'т': '11110010', 'у': '11110011', 'ф': '11110100', 'х': '11110101', 'ц': '11110110',
                     'ч': '11110111',
                     'ш': '11111000', 'щ': '11111001', 'ъ': '11111010', 'ы': '11111011', 'ь': '11111100',
                     'э': '11111101',
                     'ю': '11111110', 'я': '11111111'}
            inv_slova = {value: key for key, value in slova.items()}

            U_sh = self.doubleSpinBox.value()  # уровень шума
            f = self.doubleSpinBox_5.value()  # частота шума
            u = self.doubleSpinBox_2.value()  # скорость передачи, Бод
            bod = self.doubleSpinBox_4.value()  # уровень полезного сигнала

            razmerbloka = int(self.comboBox.currentText())  # Размер блока
            povtor_isk_blocks = self.doubleSpinBox_7.value()  # Повтор искаженных блоков (0 - 10)

            df = (f * 1000) / 20  # полоса частот
            n0 = (U_sh ** 2) / df
            e = (u ** 2) / bod
            asda = (math.sqrt((2 * e) / n0))
            p_bitosh = ((1 - ((scipy.stats.norm.cdf(asda / math.sqrt(2)) - 0.5) * 2)) / 2)
            p_bitpr = 1 - p_bitosh
            with open('text_file.txt', encoding='utf-8') as f:
                stroka_faila = str(f.read())
            kod_stroki_faila = ""
            for i in stroka_faila:
                kod_stroki_faila += slova[i]

            spisok_istochnika_block = re.findall(r'\d' * razmerbloka, kod_stroki_faila)
            spisok_istochnika_byte = []
            for i in spisok_istochnika_block:
                spisok_istochnika_byte.append(re.findall(r'\d' * 8, i))

            def chunk_based_on_size(lst, n):
                for x in range(0, len(lst), n):
                    each_chunk = lst[x: n + x]

                    if len(each_chunk) < n:
                        each_chunk = each_chunk + [None for y in range(n - len(each_chunk))]
                    yield each_chunk

            def oshibki(spisok, p_bitpr):
                stroka_oshibok = ''
                for i in spisok:
                    for y in i:
                        for z in y:
                            if p_bitpr <= random.random():
                                stroka_oshibok += "1"
                            else:
                                stroka_oshibok += "0"
                return stroka_oshibok

            stroka_oshibok_block = oshibki(spisok_istochnika_byte, p_bitpr)
            spisok_oshibok_block = re.findall(r'\d' * razmerbloka, stroka_oshibok_block)
            spisok_oshibok_byte = []
            for i in spisok_oshibok_block:
                spisok_oshibok_byte.append(re.findall(r'\d' * 8, i))
            byteee = 0
            block11 = 0
            for i in spisok_oshibok_byte:
                for y in i:
                    if y != "00000000":
                        byteee += 1
            for i in spisok_oshibok_block:
                if i != "0" * razmerbloka:
                    block11 += 1
            m_povt = 0
            stroka_priemnika_block = ''
            for i in range(len(spisok_istochnika_block)):
                for x in range(razmerbloka):
                    stroka_priemnika_block += str(int(spisok_istochnika_block[i][x]) ^ int(spisok_oshibok_block[i][x]))
            spisok_priemnika_block = re.findall(r'\d' * razmerbloka, stroka_priemnika_block)
            spisok_priemnika_byte = []
            for i in spisok_priemnika_block:
                spisok_priemnika_byte.append(re.findall(r'\d' * 8, i))
            for e in range(int(povtor_isk_blocks)):
                spisok_priemnika_AP_block1 = []
                pov = 0
                osh_bit = 0
                for i, j in zip(spisok_priemnika_byte, enumerate(spisok_istochnika_byte)):
                    spisok_priemnika_AP_block = []
                    for y, z in zip(i, j[1]):
                        if zlib.crc32(y.encode('utf-8')) == zlib.crc32(z.encode('utf-8')):
                            spisok_priemnika_AP_block.append(z)
                        else:
                            spisok_priemnika_AP_block.append('')
                    indeksi_block = []
                    indeksi_block = [i for i, ltr in enumerate(spisok_priemnika_AP_block) if ltr == '']
                    povtor_kodovih_kombinaci_block = []
                    for x in indeksi_block:
                        povtor_kodovih_kombinaci_block.append(spisok_istochnika_byte[j[0]][x])
                    pov += len(povtor_kodovih_kombinaci_block)
                    stroka_oshibok_povtor_block = oshibki(povtor_kodovih_kombinaci_block, p_bitpr)
                    spisok_oshibok_povtor_byte = re.findall(r'\d' * 8,
                                                            stroka_oshibok_povtor_block)  # Количество ошибок блок
                    stroka_priemnika1_block = ''
                    for asd in range(len(povtor_kodovih_kombinaci_block)):
                        for x in range(8):
                            stroka_priemnika1_block += str(
                                int(povtor_kodovih_kombinaci_block[asd][x]) ^ int(spisok_oshibok_povtor_byte[asd][x]))
                    spisok_priemnika1_block = re.findall(r'\d' * 8, stroka_priemnika1_block)
                    for ind, ja in zip(indeksi_block, spisok_priemnika1_block):
                        spisok_priemnika_AP_block[ind] = ja
                    spisok_priemnika_AP_block1.append(spisok_priemnika_AP_block)
                    spisok_priemnika_byte = spisok_priemnika_AP_block1
                    osh_bit += stroka_oshibok_povtor_block.count('1')
                    m_povt += len(povtor_kodovih_kombinaci_block)

            a1 = 0
            a2 = 0
            a3 = 0
            for i, j in zip(spisok_priemnika_byte, spisok_istochnika_byte):
                if i != j:
                    a1 += 1
                for y, z in zip(i, j):
                    if y != z:
                        a2 += 1
                    for g, s in zip(y, z):
                        if g != s:
                            a3 += 1
            kod = ''
            for i in spisok_priemnika_block:
                for y in i:
                    kod += y
            kod = re.findall(r'\d' * 8, kod)
            kod1 = ''
            for x in kod:
                kod1 += inv_slova[x]
            with open('text_file2.txt', 'w', encoding="utf-8") as f:
                f.write(kod1)

            if povtor_isk_blocks == 0:
                self.lineEdit.setText(str(len(kod_stroki_faila)))  # Принято бит
                self.lineEdit_9.setText(str(int(len(kod_stroki_faila) / 8)))  # Принято байт
                self.lineEdit_2.setText(str((byteee)))  # Ошибки байт
                self.lineEdit_4.setText(str(stroka_oshibok_block.count('1')))  # Ошибки бит
                self.lineEdit_8.setText(str(len(spisok_istochnika_block)))  # Блоки 1
                self.lineEdit_5.setText(str(int(block11)))  # Блоки 2
                self.lineEdit_6.setText(str(int(block11) / len(spisok_istochnika_block)))  # Блок, коэф. ошибки
                self.lineEdit_7.setText(
                    str(stroka_oshibok_block.count('1') / len(kod_stroki_faila)))  # коэф. ошибки, бит
                self.lineEdit_3.setText(str(byteee / (len(kod_stroki_faila) / 8)))  # коэф. ошибки, байт
                n_bb = int(razmerbloka) / 8
                m_povt = 0
                B_poln = int(
                    ((len(kod_stroki_faila) - stroka_oshibok_block.count('1')) / (len(kod_stroki_faila))) * bod)
                self.lineEdit_11.setText(str(B_poln))
                self.lineEdit_10.setText(str(m_povt))
            else:
                self.lineEdit.setText(str(len(kod_stroki_faila)))  # Принято бит
                self.lineEdit_9.setText(str(int(len(kod_stroki_faila) / 8)))  # Принято байт
                self.lineEdit_2.setText(str(a2))  # Ошибки байт
                self.lineEdit_4.setText(str(a3))  # Ошибки бит
                self.lineEdit_8.setText(str(len(spisok_istochnika_block)))  # Блоки 1
                self.lineEdit_5.setText(str(a1))  # Блоки 2
                self.lineEdit_6.setText(str(a1 / len(spisok_istochnika_block)))  # Блок, коэф. ошибки
                self.lineEdit_7.setText(str((a3 / len(kod_stroki_faila))))  # коэф. ошибки, бит
                self.lineEdit_3.setText(str((a2 / (len(kod_stroki_faila) / 8))))  # коэф. ошибки, байт
                n_bb = int(razmerbloka) / 8
                B_poln = int(((len(kod_stroki_faila) - a3) / (len(kod_stroki_faila) + m_povt * n_bb * 8)) * bod)
                self.lineEdit_11.setText(str(B_poln))
                self.lineEdit_10.setText(str(m_povt))

        # проверка чекбокса на моделирование аварии
        if self.checkBox_2.isChecked():
            bits_value = self.lineEdit_4.text()
            bytes_value = self.lineEdit_2.text()
            blocks_value = self.lineEdit_5.text()

            if (int(bits_value) > 0) or (int(bytes_value) > 0) or (int(blocks_value) > 0):
                QMessageBox.critical(self, "АВАРИЯ", "Произошла авария", QMessageBox.Ok)

        self.file_name = fname  
        print(self.file_name)


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = ExampleApp()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
