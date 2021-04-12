import aprslib
import logging
from pprint import pprint


def p(frame):
    try:
        packet = aprslib.parse(frame)
        #if packet.get('format', None) == 'object' and packet.get('symbol', None) == 'O':
        pprint(packet)

    except (aprslib.ParseError, aprslib.UnknownFormat) as exp:
        logger.exception(f"parsing: {frame}")



#aprs_user = "N0CALL"
aprs_user = "OE1MHS"
# APRS-IS Passcode. You can generate one for your callsign here: https://apps.magicbug.co.uk/passcode/
#aprs_pass = "13023"
aprs_pass = "17849"

# filter by geo range, type=Object, symbol=Balloon
filter1 = 'r/+47.0781/+15.1257/5000'
filter2 = 't/o'
filter3 = 's/O'


logging.basicConfig(level=logging.DEBUG) # level=10

AIS = aprslib.IS(aprs_user, passwd=aprs_pass, host='radiosondy.info', port=14580, skip_login=False)

AIS.connect()
AIS.set_filter(filter1)
AIS.set_filter(filter2)
AIS.set_filter(filter3)
AIS.consumer(p, blocking=True, immortal=False, raw=True)
