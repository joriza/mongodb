# CSV version
import os
import json
import copy
import csv


# qry_input = "frases.txt" # Name of the source file that contains the phrases

class UDTstructure:
    """Main class."""
    os.system("clear")

    def __init__(self):
        """Initialize the class"""
        self.frases_obtenidas = 0

    def press_enter(self):
        """Just pause until Enter is pressed"""
        input("Presione Enter para continuar...")

    def read_source_data_file(self, sourcefile):
        """Opens file containing the phrases to be processed"""
        aux = open(sourcefile, "r")
        return aux

    def open_source_json_file(self, filename):
        """Read json model file sent by parameter, and return an object"""
        with open(filename, "r") as read_file:
            docjson = json.load(read_file)
        return docjson

    def open_csv_file(self, filename):
        csvfile = udt.read_source_data_file(filename)
        frases_obtenidas = csv.DictReader(csvfile, delimiter='\t')
        return frases_obtenidas

    def save_target_file(self, object_input, filename):
        """Write the output in json format, the object sent by parameter"""
        with open(filename, "w") as output_file:  # Escribe en archivo json indentado
            json.dump(object_input, output_file, ensure_ascii=False, indent=2)
        # return(docJson)


if __name__ == '__main__':
    udt = UDTstructure()
    frases = udt.open_csv_file("frasesPSA_MPC.csv")  # Lee archivo CSV.
    jsonModel = udt.open_source_json_file("jsonModeloMPC_PSA.json")
    TestCaseModel = jsonModel['TestCases'][0]   # Extrae el primer testcase para reutilizar
    jsonModel['TestCases'].clear()              # Elimina los test cases del json modelo.

    for frase_actual in frases:
        TestCaseActual = copy.deepcopy(TestCaseModel)  # Ojo al copiar un diccionario o lista
        # Reemplaza la frase en el testcase_modelo recurrente
        TestCaseActual["Input"][0]["Input"] = frase_actual["Query"]
        # Reemplaza el nro de Query en el testcase_modelo recurrente
        TestCaseActual["Input"][0]["kpic_extra_info"]["query_nr"] = frase_actual["Query#"]
        # Reemplaza el nivel en el testcase_modelo recurrente
        TestCaseActual["Input"][0]["kpic_extra_info"]["level_subset"] = frase_actual["Level"]
        # Vacío Expected para que luego pueda hacer un append sin problemas
        TestCaseActual["Expected"][0]["JSON"].clear()
        # Acondiciono expected (aun en modo texto)
        acond_expected = frase_actual["Expected Json Result"]
        acond_expected = acond_expected.replace("AllResults", "ServerResponse")
        acond_expected = acond_expected.replace("[", "")
        acond_expected = acond_expected.replace("]", "")
        # Fin Acondiciono expected
        TestCaseActual["Expected"][0]["JSON"].append(json.loads(acond_expected))  # Reemplaza el ExpextedJson en el Json
        jsonModel["TestCases"].append(TestCaseActual)  # Agrega un nuevo test_case a la lista de testcases

    udt.save_target_file(jsonModel, "salida.json")
    print("Generados", len(jsonModel["TestCases"]), "test")
    print("Actualizar", len(jsonModel["TestCases"]))
    # print(type(frases))

# TestCases[0].Input[0].Input
# TestCases[0].Expected[0].JSON[0]
# TestCases[0].Expected[0].JSON
