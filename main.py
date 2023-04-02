# from https://www.ictshore.com/sdn/python-snmp-tutorial/

from pysnmp.hlapi import *
from pysnmp import hlapi
import snmpFunctions



snmpV3 = hlapi.UsmUserData('user3', authKey='mypassword1',
                  privKey='privpassword1',
                  authProtocol=hlapi.usmHMACSHAAuthProtocol,
                  privProtocol=hlapi.usmDESPrivProtocol)

print(snmpFunctions.get('192.168.1.1', ['1.3.6.1.2.1.1.5.0'], snmpV3))

# Using SNMPv2c, we set the hostname of the remote device to 'SNMPHost'
#snmpFunctions.set('192.168.1.1', {'1.3.6.1.2.1.1.5.0': 'SNMPHost'}, snmpV3)

print(snmpFunctions.get('192.168.1.1', ['1.3.6.1.2.1.2.2.1.8'], snmpV3))


its = snmpFunctions.get_bulk_auto('192.168.1.1', ['1.3.6.1.2.1.2.2.1.2 ', '1.3.6.1.2.1.31.1.1.1.18'], snmpV3, '1.3.6.1.2.1.2.1.0')
for it in its:
    for k, v in it.items():
        print("{0}={1}".format(k, v))
    print('')


