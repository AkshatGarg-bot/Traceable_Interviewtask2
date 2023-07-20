import json
##reading a file
with open('/Users/akshatgarg/Downloads/openapi-spec.json') as f:
    openapi_spec = json.load(f)

## looping to all Api's
for path in openapi_spec['paths']:
    ##for looping to all methods of api
    for method in openapi_spec['paths'][path]:
        operation = openapi_spec['paths'][path][method]
        # print(f"Operation: {operation['operationId']}")

        ## printing exmaple requests
        if 'requestBody' in operation:
            print("Request Example:")
            print(json.dumps(operation['requestBody']['content']['application/json'], indent=4))
        
        #printing example responses
        if 'responses' in operation:
            for status_code in operation['responses']:
                response = operation['responses'][status_code]
                print(f"Response Example ({status_code}):")
                print(json.dumps(response['content']['application/json'], indent=4))