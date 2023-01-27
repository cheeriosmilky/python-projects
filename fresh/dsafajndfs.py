from licensing.models import *
from licensing.methods import Key, Helpers

RSAPubKey = "<RSAKeyValue><Modulus>nakBsggAFPeri5w98jlWfQ2bLlFG4b704be79ox+VOhze7kiqGZFc4zHAAHFVObC8sCAXT443NXxp4vxUwkXuMOjDl+WYzzGEeOvaotnjbSUwwKnF9mmHn3HxR8vahvpxcdOK/QErj20D6FArgqSAPNe4fWBowfK0LBcsmUgA9S4aAWqdbzn5I/wymbEdFALLDP00q1sDmEYlLNGXI+ixwX1ozn8gK0dx7QPyyK9GqJ551wWCknFwc63dJbYA1c7k98FLhgWC/vxcBdNZTH66WGtsRLT/sYboYd/2LRUoFGCeZ8GOiJ4F2oTOVLGImJaXmdod6sB1jXB8YQAImqbjQ==</Modulus><Exponent>AQAB</Exponent></RSAKeyValue>"
auth = "WyIzNjA2NjYxNCIsInlLSWJ5VVJEdFVPZHpkN3A3TE1rVk9HQ3Zxa29UcTVVaE1YeUtmR0giXQ=="

result = Key.activate(token=auth,\
                    rsa_pub_key=RSAPubKey,\
                    product_id=18566, \
                    key='IVLOG-LBCBL-TVPSF-OSALT',\
                    machine_code=Helpers.GetMachineCode())

if result[0] == None or not Helpers.IsOnRightMachine(result[0]):
    print('no')
else:
    print('yes')