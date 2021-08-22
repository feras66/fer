API Key = M3odOmLdlBF5pyAOLfT0Pp7oRC0UoyQySC7ftX7DKmQ0
URL= https://api.au-syd.language-translator.watson.cloud.ibm.com/instances/431ec0f5-59e6-4cad-81f7-3a1da84f2f6e
### en to fr
curl -X POST --user "apikey:M3odOmLdlBF5pyAOLfT0Pp7oRC0UoyQySC7ftX7DKmQ0" \
--header "Content-Type: application/json" \
--data '{"text": ["Hello, world.", "How are you?"], 
"model_id":"en-fr"}' \
"https://api.au-syd.language-translator.watson.cloud.ibm.com/instances/431ec0f5-59e6-4cad-81f7-3a1da84f2f6e/v3/translate?version=2018-05-01"


### fr to en
curl -X POST --user "apikey:M3odOmLdlBF5pyAOLfT0Pp7oRC0UoyQySC7ftX7DKmQ0" \
--header "Content-Type: application/json" \
--data '{"text": ["Hello, world.", "How are you?"], 
"model_id":"fr-en"}' \
"https://api.au-syd.language-translator.watson.cloud.ibm.com/instances/431ec0f5-59e6-4cad-81f7-3a1da84f2f6e/v3/translate?version=2018-05-01"

