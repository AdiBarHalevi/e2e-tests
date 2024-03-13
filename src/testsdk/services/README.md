# Testsdk Services
A list of all services and services methods.
- Services

    - [Pets](#pets)
- [All Methods](#all-methods)


## Pets

| Method    | Description|
| :-------- | :----------| 
| [create_pets](#create_pets) | Create a pet |
| [list_pets](#list_pets) | List all pets |
| [show_pet_by_id](#show_pet_by_id) | Info for a specific pet |




## All Methods


### **create_pets**
Create a pet
- HTTP Method: POST
- Endpoint: /pets

**Parameters**
| Name    | Type| Required | Description |
| :-------- | :----------| :----------| :----------| 
| request_input | [Pet](/src/testsdk/models/README.md#pet) | Required | Request body. |

**Return Type**

Returns a dict object.

**Example Usage Code Snippet**
```Python
from os import getenv
from pprint import pprint
from testsdk import Testsdk
sdk = Testsdk()
sdk.set_access_token(getenv("TESTSDK_ACCESS_TOKEN"))
request_body = {
	'id': 60806210,
	'name': 'name',
	'tag': 'tag'
}
results = sdk.pets.create_pets(request_input = request_body)

pprint(vars(results))

```

### **list_pets**
List all pets
- HTTP Method: GET
- Endpoint: /pets

**Parameters**
| Name    | Type| Required | Description |
| :-------- | :----------| :----------| :----------| 
| limit | int | Optional | How many items to return at one time (max 100) |

**Return Type**

[Pets](/src/testsdk/models/README.md#pets) 

**Example Usage Code Snippet**
```Python
from os import getenv
from pprint import pprint
from testsdk import Testsdk
sdk = Testsdk()
sdk.set_access_token(getenv("TESTSDK_ACCESS_TOKEN"))
results = sdk.pets.list_pets(limit = -43403082)

pprint(vars(results))

```

### **show_pet_by_id**
Info for a specific pet
- HTTP Method: GET
- Endpoint: /pets/{petId}

**Parameters**
| Name    | Type| Required | Description |
| :-------- | :----------| :----------| :----------| 
| pet_id | str | Required | The id of the pet to retrieve |

**Return Type**

[Pet](/src/testsdk/models/README.md#pet) 

**Example Usage Code Snippet**
```Python
from os import getenv
from pprint import pprint
from testsdk import Testsdk
sdk = Testsdk()
sdk.set_access_token(getenv("TESTSDK_ACCESS_TOKEN"))
results = sdk.pets.show_pet_by_id(pet_id = 'petId')

pprint(vars(results))

```




