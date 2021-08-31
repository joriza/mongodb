#! Arma UDT con objetos.

import json
from collections import OrderedDict
import luadata


class RequiredDomains():

    ''' Objeto RequiredDomains que se representa como una lista que contiene Dominios'''
    def __init__(self, *args):
        self.required_domains_lst = [elem for elem in args]
        self.required_dom_data =  {}

        self.required_dom_data["RequiredDomains"] = self.required_domains_lst

    def append(self, dominio):
        self.required_domains_lst.append(dominio)

    def __str__(self):
        required_dom_str = json.dumps(self.required_dom_data, ensure_ascii=False, sort_keys=False, separators=(',', ':'), indent=4)
        return required_dom_str

    @property
    def data(self):
        return self.required_dom_data['RequiredDomains']

class SetupQueries():
    ''' Objeto SetupQueres que se levanta desde un archivo con el formato JSON -> { "SetUpQueries": {...} }'''
    def __init__(self, setup_queries_file):
        self.setup_queries_data = {}
        self.setup_queries_data = json.load(open(setup_queries_file, 'r'))

    def __str__(self):
        setup_queries_str = json.dumps(self.setup_queries_data, ensure_ascii=False, sort_keys=False, separators=(',', ':'), indent=4)
        return setup_queries_str

    @property
    def data(self):
        if  self.setup_queries_data['SetupQueries']:
            return self.setup_queries_data['SetupQueries']
        else:
            return None


class Test():
    ''' Objeto Test que vive dentro del objeto que lo va a contener que es TestCases()'''
    def __init__(self, query, delta_request_info=None, json_ExpRes=""):
        self.testcase = OrderedDict()
        self.testcase['Input'] = []
        self.testcase['Expected'] = []

        # TestCase -> Input
        self.input_elem = {}
        self.input_elem["Kind"] = "Text"
        self.input_elem['Input'] = query
        if delta_request_info:
            # si logramos pasarle una captura en txt del Delta_Request_Info del TEST o necesario para este UDT
            self.input_elem['DeltaRequestInfo'] = luadata.unserialize(delta_request_info, encoding="utf-8", multival=False)

        # Guardo lo referente a Input (es una lista)
        self.testcase['Input'].append(self.input_elem)

        # TestCase -> Expected
        self.expected_elem = {}
        self.expected_elem["Kind"] = "Equal"
        self.expected_elem["JSON"] = "FALTA PONER EXPECTED RESULT CAPTURADO POR ALGÚN MEDIO"
        # Si logramos capturar el ExpRes por algún medio iría la linea de abajo
        #self.expected_elem["JSON"] = [json.loads(json_ExpRes)]
        self.expected_elem["Path"] = "ServerResponse"

        # Guardo lo referente a Expected (es una lista)
        self.testcase["Expected"].append(self.expected_elem)

    def __str__(self):
        testcase_str = json.dumps(self.testcase, ensure_ascii=False, sort_keys=False, separators=(',', ':'), indent=4)
        return testcase_str

    @property
    def data(self):
        return self.testcase


class TestCases():
    '''Objeto TestCases() que es un contenedor(una lista) de objetos Test()'''
    def __init__(self):
        self.testcases = {}
        self.testcases_lst = []
        self.testcases['TestCases'] = self.testcases_lst

    def append(self, testcase):
        self.testcases['TestCases'].append(testcase)

    def __str__(self):
        for elem in self.testcases['TestCases']:
            testcases_str = str(elem)
        return testcases_str

    @property
    def data(self):
        return self.testcases


class UDT():
    ''' Objeto UDT que es un contenedor de TODOS los demás objetos.
        Los objetos que contiene se crean con métodos propios de esta clase
        (se crean nombrabdo al objeto UDT).
    '''
    def __init__(self, dominio):
        self.dominio = dominio
        self.udt_data = {}
        self.udt_data['SetupQueries'] = {}
        self.udt_data['TestCases'] = []

    def add_required_domains(self, *args):
        self.udt_data['RequiredDomains'] = RequiredDomains(*args)


    def add_setup_queries(self, setup_queries_file):
        self.udt_data['SetupQueries'] = SetupQueries(setup_queries_file)

    def add_test(self, query, delta_request_info, json_exp_res):
        tcs = TestCases()
        tc = Test(query, delta_request_info, json_exp_res)
        tcs.append(tc)
        self.udt_data['TestCases'].append(tcs)

    def __data_to_dict(self):
        '''Creacción de diccionario con atributos de los objetos que contiene
           los cuales son diccionarios.
        '''

        # diccionario que almacenará todos los objetos que componen el objeto UDT
        udt_data_json = {}

        # datos de RequiredDomains
        udt_data_json['RequiredDomains'] = self.udt_data['RequiredDomains'].data

        # datos de SetupQueries
        if self.udt_data['SetupQueries']:
            udt_data_json['SetupQueries'] = self.udt_data['SetupQueries'].data

        # datos de TestCases
        udt_data_json['TestCases'] = list()
        for elem in self.udt_data['TestCases']:
            # datos de Test almacenados en TestCases
            udt_data_json['TestCases'].append(elem.data['TestCases'][0].data)

        # devuelo en un diccionario
        return udt_data_json

    def to_file(self):
        # Bajada de DiccionatiostsJSON a file
        udt_data_json = self.__data_to_dict()
        with open(self.dominio+'_UDT.json', "w") as json_file:
            json.dump(udt_data_json, json_file, ensure_ascii=False, sort_keys=False, separators=(',', ':'), indent=4)

    def __str__(self):
        # Representación del objeto en modo texto (se pone lo que se quiera mostrar en la representación)
        # En este caso el diccionario y su contenido como un String.
        udt_data_json = self.__data_to_dict()
        udt_str = json.dumps(udt_data_json, ensure_ascii=False, sort_keys=False, separators=(',', ':'), indent=4)
        return udt_str


if __name__ == '__main__':

    # Pruebas de carga de objetos por separados sin el objeto agrupador que es UDT

    #rd = RequiredDomains("User Music Search", "Contact Access V2", "Query Glue", "Terrier Upload")
    #print(rd)

    #sq = SetupQueries("SetupQueries_UMS.json")
    #print(sq)

    #tc = TestCase("lista todos mis discos")
    #print(tc)

    #tcs = TestCases()
    #tcs.append(tc.data)
    #print(tcs)


    udt = UDT('UserMusicSearch')
    udt.add_required_domains("User Music Search", "Contact Access V2", "Query Glue", "Terrier Upload")
    udt.add_setup_queries("SetupQueries_UMS.json")
    udt.add_test("lista todos mis discos") # podría también pasarse un delta_request_info y un command_result
    udt.add_test("lista todos mis CD")
    print(udt)
    udt.to_file()







