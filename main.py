from pysnmp.hlapi import *

#TODO Anderes MIB versuchen

iterator = getCmd(
    SnmpEngine(),
    UsmUserData('user3', 'mypassword1', 'privpassword1',
                authProtocol=usmHMACSHAAuthProtocol,
                privProtocol=usmDESPrivProtocol),
    UdpTransportTarget(('192.168.1.1', 161)),
    ContextData(),
    ObjectType(ObjectIdentity('SNMPv2-MIB', 'sysName', 0))
)

errorIndication, errorStatus, errorIndex, varBinds = next(iterator)

if errorIndication:
    print(errorIndication)

elif errorStatus:
    print('%s at %s' % (errorStatus.prettyPrint(),
                        errorIndex and varBinds[int(errorIndex) - 1][0] or '?'))

else:
    for varBind in varBinds:
        print(' = '.join([x.prettyPrint() for x in varBind]))