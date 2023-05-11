import requests
import json

head = {
  'Content-Type': 'application/json',
  'Authorization': 'Bearer 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'
}
intxt = input('txt: ')
data = {
  'prompt': intxt,
  'max_tokens': 100,
  'temperature': 0.5
}
res = requests.post(
  'https://api.openai.com/v1/engines/text-davinci-003/completions',
  headers=head,
  json=data
)

if res.status_code == 200:
    resdata = json.loads(res.text)
    print(resdata['choices'][0]['text'])
else:
    print('err: '+str(res.status_code))