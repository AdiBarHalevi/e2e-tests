# Testsdk Python SDK 1.0.0
A Python SDK for Testsdk.



- API version: 1.0.0
- SDK version: 1.0.0

## Table of Contents
- [Requirements](#requirements)
- [Installation](#installation)
    - [Dependencies](#dependencies)
- [Authentication](#authentication)
    - [Access Token Authentication](#bearer-authentication)
- [API Endpoint Services](#api-endpoint-services)
- [API Models](#api-models)
- [Testing](#testing)
- [Configuration](#configuration)
- [Sample Usage](#sample-usage)
- [Testsdk Services](#testsdk-services)
- [License](#license)

## Installation
```bash
pip install testsdk
```

### Dependencies

This SDK uses the following dependencies:
- requests 2.28.1
- http-exceptions 0.2.10
- pytest 7.1.2
- responses 0.21.0

## Authentication

To see whether an endpoint needs a specific type of authentication check the endpoint's documentation.

### Access Token Authentication
The Testsdk API uses bearer tokens as a form of authentication.You can set the bearer token when initializing the SDK through the constructor: 

```py
sdk = Testsdk('YOUR_BEARER_TOKEN')
```

Or through the `set_access_token` method:
```py
sdk = Testsdk()
sdk.set_access_token('YOUR_BEARER_TOKEN')
```

You can also set it for each service individually:
```py
sdk = Testsdk()
sdk.pets.set_access_token('YOUR_BEARER_TOKEN')
```

## API Endpoint Services

All URIs are relative to http://petstore.swagger.io/v1.

Click the service name for a full list of the service methods.

| Service |
| :------ |
|[Pets](./services/README.md#pets)|

## API Models
[A list documenting all API models for this SDK](./models/README.md#testsdk-models).

## Testing

Run unit tests with this command:

```sh
python -m unittest discover -p "test*.py" 
```

## Sample Usage

```py
from os import getenv
from pprint import pprint
from testsdk import Testsdk

sdk = Testsdk()
sdk.set_access_token(getenv("TESTSDK_ACCESS_TOKEN"))

results = sdk.pets.list_pets()

pprint(vars(results))
```


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





## License

License: MIT. See license in LICENSE.
