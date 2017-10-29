from kivy.app import App
import winsound
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.checkbox import CheckBox
from kivy.uix.textinput import TextInput
from kivy.uix.behaviors import FocusBehavior
from kivy.core.window import Window
from data import csv_loadHeader
from kivy.uix.popup import Popup
import csv
from builtins import Exception
from data import *
from queue import Queue
from ui.the_end import TheEnd
import time

import sys

queue_matched = Queue()
queue_nomatched = Queue()




# print(remove_sub_str(prefixes_to_remove, "pl pl Bieńczyski Plac targowy".lower()))
# print(remove_sub_str(prefixes_to_remove, "al. ignacego daszyńskiego"))
# print(remove_sub_str(prefixes_to_remove, "os. kolorowe"))
# print(remove_sub_str(prefixes_to_remove, "al. 29 listopada"))
# print(remove_sub_str(prefixes_to_remove, "os. os. os al aleja. kolorowe"))
# sys.exit(0)

def dict_by_column(data_header, data, column_name, column_number):
    if column_name not in data_header:
        raise Exception("Cannot find column " + str(column_name) + " in " + str(data_header))

    dict_data = {}
    cols = list(range(0, len(data[0])))
    cols.pop(column_number)
    # print(column_name, type(cols), cols)
    for row in data:
        key = row[column_number]
        # print("key", type(key), key)
        if key not in dict_data:
            dict_data[key] = []
        dict_data[key].append(get_elements(row, cols))

    return dict_data


# ----------------------------------------
def gen_to_remove_list(input_data, ul_in_column, dict_nazwa_glowna_czesc):
    word_list = []

    for in_row in input_data:
        words = in_row[ul_in_column].split()
        word_list.extend(words)

    in_u_set = set(word_list)
    # print(len(in_u_set), in_u_set)

    unique_posorowane = []

    for key in dict_nazwa_glowna_czesc:
        words = key.split()
        unique_posorowane.extend(words)

    dict_u_set = set(unique_posorowane)
    # print(len(dict_u_set), dict_u_set)

    list1 = list(in_u_set)
    list2 = list(dict_u_set)
    wynik_diff = [a for a in list1 + list2 if (a not in list2)]
    for el in wynik_diff:
        if not el.endswith('.'):
            indx = wynik_diff.index(el)
            wynik_diff[indx] = wynik_diff[indx] + u' '

    return wynik_diff


# ----------------------------------------

def remove_prefix(prefixes_to_remove_list, in_str):
    temp = remove_sub_str(prefixes_to_remove_list, in_str)
    temp = remove_sub_str(prefixes_to_remove_list, temp)
    temp = remove_sub_str(prefixes_to_remove_list, temp)
    temp = remove_sub_str(prefixes_to_remove_list, temp)
    return temp


def nr_budynu_z_ulicy(nazwa_ulicy, poprawna_nazwa_ulicy):
    if nazwa_ulicy == poprawna_nazwa_ulicy:
        return None
    elif nazwa_ulicy.startswith(poprawna_nazwa_ulicy):
        return nazwa_ulicy[len(poprawna_nazwa_ulicy):].strip()


class ChooseColumns(GridLayout):
    #
    # def readPath(dupa):
    #     heders = csv_loadHeader(dupa[0])
    #     print(heders)
    #     ChooseColumns()

    def getcheckboxes_active(self, *arg):
         for idx, wgt in enumerate(self.check_ref.items()):
            if wgt[1].active:
                self.selected.append(idx)
         # print(self.street.text)
         # print(self.buildingNumber.text)

         self.zButaWjezdzam()


    def zButaWjezdzam(self):
        # print("Wjeżdżajcie")
        # print(self.selected)
        # input_data_filename = '''C:/Users/wiedmo/Desktop/Hack/dane wsadowe/dane wejściowe.csv'''
        input_data_filename = self.choosing_path_and_file
        #TODO
        #TODO
        #TODO
        #TODO
        #TODO
        #TODO
        #TODO
        #TODO

        address_dict_filename = '''C:/Users\morvi_000/Desktop/Nowy folder/dane wsadowe/Słownik Adresów.csv'''



        # print(nr_budynu_z_ulicy("adama 34", "adama"))
        # print(nr_budynu_z_ulicy("adama 54 36", "adama 54"))
        # print(nr_budynu_z_ulicy("jana sawickiego", "sawickiego"))
        # sys.exit(0)

        #if __name__ == '__main__':
        if True:
            # print(type(input_data_filename), input_data_filename)
            # input_data_header = csv_loadHeader(str(input_data_filename))

            print("=============================================================")
            print("==================== Inicjalizacja ... ======================")
            print("=============================================================")

            columns = []
            ul_in_column = int(self.street.text)
            if self.buildingNumber:
                nr_in_column = int(self.buildingNumber.text)
            else:
                nr_in_column = None
            # nr_in_column = self.buildingNumber
            user_colums = [1]
            # print("Ul in cuttend columns is col = ", ul_in_column)
            # time.sleep(2)

            # wczytywane danych wejsciowych
            # print(input_data_filename)
            # print(input_data_filename[0])
            # input_data_filename = str(input_data_filename).replace('\\\\', '\\')
            input_data_filename = input_data_filename[0]
            input_data_header = csv_loadHeader(str(input_data_filename), columns=columns)
            input_data = csv_load(input_data_filename, skip_first_line=True, columns=columns)

            # print(input_data_header)
            # print(len(input_data), input_data[0])

            # print("-------------------")
            # wczytywane słownika
            dict_columns = [1, 5, 10, 11]
            address_dict_header = csv_loadHeader(address_dict_filename, dict_columns)
            address_dict = csv_load(address_dict_filename, skip_first_line=True, columns=dict_columns)

            start_process_time = time.time()

            # print(address_dict_header)
            # print(len(address_dict), address_dict[0])

            # print("++++++++++++++++++++")

            # ddh = csv_loadHeader(input_data_filename, columns=[])
            dict_by_column_index = 1
            dict_nazwa_glowna_czesc = dict_by_column(address_dict_header, address_dict,
                                                     address_dict_header[dict_by_column_index], dict_by_column_index)
            for key_ulica in dict_nazwa_glowna_czesc:
                dict_nazwa_glowna_czesc[key_ulica] = dict_by_column(address_dict_header,
                                                                    dict_nazwa_glowna_czesc[key_ulica],
                                                                    address_dict_header[0], 0)

            # print("-=-=---=-=-")
            # print(len(dict_nazwa_glowna_czesc))
            # for d in dict_nazwa_glowna_czesc:
            #    print(d, " -> ", len(dict_nazwa_glowna_czesc[d]), dict_nazwa_glowna_czesc[d])
            # sys.exit(0)

            # print(len(dict_nazwa_glowna_czesc), address_dict_header[dict_by_column_index])
            # print(address_dict_header)

            matchet_geom_data = []  # nr. line,
            i = 0
            j = 0
            c = 0
            # print("dict_nazwa_glowna_czesc:")
            # print(dict_nazwa_glowna_czesc.keys())

            to_remove_list = gen_to_remove_list(input_data, ul_in_column, dict_nazwa_glowna_czesc)
            to_remove_list.sort()
            prefixes_to_remove.sort()
            # print("sss:", len(to_remove_list), to_remove_list)
            # print("prefixes_to_remove:", len(prefixes_to_remove), prefixes_to_remove)
            # sys.exit(0)
            frequency = 2500  # Set Frequency To 2500 Hertz
            duration = 300  # Set Duration To 1000 ms == 1 second
            winsound.Beep(frequency, duration)

            print("")
            print("")
            print("")
            print("=============================================================")
            print("==================== Geolokalizacja ... =====================")
            print("=============================================================")
            print("")
            print("")
            print("")


            startDate = time.strftime("%Y-%m-%d %H:%M:%S")
            start_process_time = time.time()

            to_second_match = []

            # input_data
            # [0] -
            # [1] - nr budynku
            # [6] - losowo
            for in_row in input_data:
                c += 1
                # print(in_row, ul_in_column)
                in_ul = remove_prefix(to_remove_list, in_row[ul_in_column])

                nr_bud = None
                if nr_in_column is not None:
                    nr_bud = in_row[nr_in_column]

                if nr_in_column is None:
                    temp = in_ul.split()
                    nr_bud = temp[-1]
                    temp.pop(-1)
                    in_ul = " ".join(temp)
                    # print(in_row[ul_in_column], " => :::: in ul:", in_ul, "nr:", nr_bud)

                if in_ul in dict_nazwa_glowna_czesc:  # ["stanislata lema", "barbary fa"]
                    if nr_bud in dict_nazwa_glowna_czesc[in_ul].keys():
                        x = dict_nazwa_glowna_czesc[in_ul][nr_bud][0][0]
                        y = dict_nazwa_glowna_czesc[in_ul][nr_bud][0][1]
                        # print(in_row, "=>", [in_row, x, y])
                        in_row.append(x)
                        in_row.append(y)
                        queue_matched.put(in_row)
                        i += 1
                        continue

                # queue_nomatched.put(in_row)
                to_second_match.append(in_row)
                j += 1
                # print(c, "NO ", in_row[ul_in_column], " F: ", filtered_data)

            #
            # dopasowania dwukolumniwe
            # Fitrowanie jeszcez nie zmaczowanych
            #

            # wczytywane słownika
            dict_columns = [1, 0, 10, 11]
            address_dict_header = csv_loadHeader(address_dict_filename, dict_columns)
            address_dict = csv_load(address_dict_filename, skip_first_line=True, columns=dict_columns)

            # print(address_dict_header)
            # print(len(address_dict), address_dict[0])
            dict_by_column_index = 1
            dict_nazwa_glowna_czesc = dict_by_column(address_dict_header, address_dict,
                                                     address_dict_header[dict_by_column_index], dict_by_column_index)
            for key_ulica in dict_nazwa_glowna_czesc:
                dict_nazwa_glowna_czesc[key_ulica] = dict_by_column(address_dict_header,
                                                                    dict_nazwa_glowna_czesc[key_ulica],
                                                                    address_dict_header[0], 0)

            # print("---------------------", len(to_second_match))
            # print("dict_nazwa_glowna_czesc:", dict_nazwa_glowna_czesc)

            dict_nazwa_glowna_czesc_fifxed = {}
            for key in dict_nazwa_glowna_czesc.keys():
                value = dict_nazwa_glowna_czesc[key]
                fixed_key = remove_prefix(to_remove_list, key)
                dict_nazwa_glowna_czesc_fifxed[fixed_key] = value

            to_third_match = []

            for in_row in to_second_match:
                # print("Second(", len(to_second_match), "):", in_row)
                # in_ul = remove_prefix(to_remove_list, in_row[ul_in_column])
                in_ul = in_row[ul_in_column]

                nr_bud = None
                if nr_in_column is not None:
                    nr_bud = in_row[nr_in_column]

                if nr_in_column is None:
                    temp = in_ul.split()
                    nr_bud = temp[-1]
                    temp.pop(-1)
                    in_ul = " ".join(temp)
                    # print(in_row[ul_in_column], " => :::: in ul:", in_ul, "nr:", nr_bud)

                if in_ul in dict_nazwa_glowna_czesc:  # ["stanislata lema", "barbary fa"]
                    if nr_bud in dict_nazwa_glowna_czesc[in_ul].keys():
                        x = dict_nazwa_glowna_czesc[in_ul][nr_bud][0][0]
                        y = dict_nazwa_glowna_czesc[in_ul][nr_bud][0][1]
                        # print(in_row, "=>", [in_row, x, y])
                        in_row.append(x)
                        in_row.append(y)
                        queue_matched.put(in_row)
                        i += 1
                        continue

                # queue_nomatched.put(in_row)
                to_third_match.append(in_row)

            for in_row in to_third_match:
                in_ul = remove_prefix(to_remove_list, in_row[ul_in_column])

                nr_bud = None
                if nr_in_column is not None:
                    nr_bud = in_row[nr_in_column]

                if nr_in_column is None:
                    temp = in_ul.split()
                    nr_bud = temp[-1]
                    temp.pop(-1)
                    in_ul = " ".join(temp)
                    # print(in_row[ul_in_column], " => :::: in ul:", in_ul, "nr:", nr_bud)

                if in_ul in dict_nazwa_glowna_czesc_fifxed:  # ["stanislata lema", "barbary fa"]
                    if nr_bud in dict_nazwa_glowna_czesc_fifxed[in_ul].keys():
                        x = dict_nazwa_glowna_czesc_fifxed[in_ul][nr_bud][0][0]
                        y = dict_nazwa_glowna_czesc_fifxed[in_ul][nr_bud][0][1]
                        # print(in_row, "=>", [in_row, x, y])
                        in_row.append(x)
                        in_row.append(y)
                        queue_matched.put(in_row)
                        i += 1
                        continue

                queue_nomatched.put(in_row)

            stop_process_time = time.time()
            stopData = time.strftime("%Y-%m-%d %H:%M:%S")

            print("=============================================================")
            print("============= Geolokacja zakończona powodzeniem =============")
            print("=============================================================")
            print("")
            print("Zapisywanie danych...")
            print("")

            log_file_str = ("Summary: \n"
                            "Input data lines: " + str(len(input_data)) +
                            "\nStart date: " + startDate +
                            "\nStop date: " + stopData +
                            "\nMatched: " + str(queue_matched.qsize()) +
                            "\nNo matched: " + str(queue_nomatched.qsize()) +
                            "\nProcess time: " + str(stop_process_time - start_process_time) + "s")


            header = csv_loadHeader(input_data_filename)
            headerxy = header
            headerxy.append('x')
            headerxy.append('y')
            headerxy = ";".join(headerxy)
            save_ready_csv(queue_matched, "Matched.csv", headerxy)
            save_ready_csv(queue_nomatched, "NotMatched.csv", ";".join(header))

            print("=============================================================")
            print("=========== Zakończono zapisywanie z powodzeniem ============")
            print("=============================================================")
            #
            # print("Summary: \n")
            # print("Input data lines: ", len(input_data))
            # print("\nMatched: ", queue_matched.qsize())
            # print("\nNo matched: ", queue_nomatched.qsize())
            # print("\nProcess time: ", stop_process_time - start_process_time)

            print(log_file_str)

            with open("log.txt", "w", encoding="utf-8-sig") as f:
                f.write(log_file_str)
            # print(log_file_str)

            frequency = 2500  # Set Frequency To 2500 Hertz
            duration = 300  # Set Duration To 1000 ms == 1 second
            winsound.Beep(frequency, duration)

            self.toTheEnd()

            # for el in no_matched:
            #   print(el[1], el[2], el[5])

    def toTheEnd(instance):
        Window.size = (700, 500)
        TheEnd()

    def __init__(self, choosing_path_and_file, **kwargs):
        super(ChooseColumns, self).__init__(**kwargs)
        # print(choosing_path_and_file)
        self.choosing_path_and_file = choosing_path_and_file
        self.hhh = {}
        self.selected = []
        self.check_ref = {}
        self.street = None
        self.buildingNumber = None

        def get_r():
            return self.selected, 4, None

        content = GridLayout()
        self.popup = popup = Popup(title="Choose header rows", content=content, size_hint = (None,None), size=(700,500))

        heders = csv_loadHeader(choosing_path_and_file[0])
        # print(heders)
        self.hhh = heders

        content.cols = 6
        for i in enumerate(heders):
            # print(i)
            cbx = CheckBox()
            self.check_ref["cb" + str(i[1])] = cbx
            content.add_widget(cbx)
            content.add_widget(Label(text=str(i[0])+ " " + i[1]))
        btn1 = Button(text="Analysis")

        # txtField = TextInput(hint_text="ulica", input_filter=int)
        txtField = TextInput(input_filter = 'int', hint_text = 'Ulica: ')

        # txtField = TextInput(hint_text="ulica")
        txtField2 = TextInput(input_filter='int', hint_text='Nr Domu: ')

        content.add_widget(btn1)
        # content.add_widget(Label(text="Wybor ulicy:"))
        content.add_widget(txtField)
        # content.add_widget(Label(text="Wybor budynku, jesli osobny naglowek"))
        content.add_widget(txtField2)
        self.street = txtField
        self.buildingNumber = txtField2
        btn1.bind(on_press=self.getcheckboxes_active)
        popup.open()





