# json de pruebas: https://jsonplaceholder.typicode.com/
import jmespath
import json
import requests

persons = {
  "persons": [
    { "name": "erik", "age": 38 },
    { "name": "john", "age": 45 },
    { "name": "rob", "age": 14 }
  ]
}
print(jmespath.search('persons[*].age', persons))

response = requests.get("https://jsonplaceholder.typicode.com/users")
todos = json.loads(response.text)
data22 = json.dumps(todos, indent=2)
print(data22)
# print(jmespath.search('id.1', data22))

# print(data22)
# print(jmespath.search([*], data22))

with open("1er-NSC-OK.json", "r") as read_file:
  registro = json.load(read_file)

print("RequiredDomains\n",jmespath.search('RequiredDomains[*]', registro))
# print("SetupQueries\n",jmespath.search('SetupQueries.Input[*].DeltaRequestInfo.*.Requests[*]', registro))
print("TestCases.Input\n",jmespath.search('TestCases[1].Input[*]', registro))
print("TestCases.Input.Input0\n",jmespath.search('TestCases[1].Input[0].Input', registro))
print("TestCases.Input.Input1\n",jmespath.search('TestCases[1].Input[1].Input', registro))
print("TestCases.Input.Input2\n",jmespath.search('TestCases[1].Input[2].Input', registro))
print("TestCases.Expected\n",jmespath.search('TestCases[1].Expected[*].JSON[*].CommandKind', registro))
print("TestCases.Expected\n",jmespath.search('TestCases[1].Expected[0].JSON[*].CommandKind', registro))
print("TestCases.Expected\n",jmespath.search('TestCases[1].Expected[1].JSON[*].CommandKind', registro))
print("TestCases.Expected\n",jmespath.search('TestCases[1].Expected[2].JSON[*].CommandKind', registro))
