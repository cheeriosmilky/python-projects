from licensing.models import *
from licensing.methods import Key, Helpers

RSAPubKey = "<RSAKeyValue><Modulus>xnTzcz52AZRQ0GRKhHOQ0k8mS2FcgyyWPFD8Ro21uluBLZNaH/ewQGhj8dnXMnJ0HAoaItiGY/BvpHto2FSpypYPNMxXGZC3Go+lswVYPnyfRH76ro5/k0jHRrMLQdErR1BiCJDzUWGhbJIXkoXTj7YnVyGHCbcUC/xuNifGRFhj/SnSg/chpw27DYKVbeC2SzN4q9XvtTqdPKH3AVuC7M5FjjhsSb4+dtwHyqLbGeW8elCPs5bf25tOvQFmWoWK+v3MF/np0Ig+BzTZP5E6hWbSVCGk3kK9yPpQXlEB9dVm3x9oNhwvpl6gHYLjCXaBA5bjUgzdIL00dS/6x0INwQ==</Modulus><Exponent>AQAB</Exponent></RSAKeyValue>"
auth = "WyIyOTk0MTQ3NCIsIkJ6TmxpdGNPZkRMMmVDbzZ5b1JwZXpYSWtSdmcwMHV4MXlFZyttOE8iXQ=="

result = Key.activate(token=auth,\
                   rsa_pub_key=RSAPubKey,\
                   product_id=17671, \
                   key="",\
                   machine_code=Helpers.GetMachineCode(v=2))

if result[0] == None or not Helpers.IsOnRightMachine(result[0], v=2):
    # an error occurred or the key is invalid or it cannot be activated
    # (eg. the limit of activated devices was achieved)
    print("The license does not work: {0}".format(result[1]))
else:
    # everything went fine if we are here!
    print("The license is valid!")
    license_key = result[0]
    print("Feature 1: " + str(license_key.f1))
    print("License expires: " + str(license_key.expires))
