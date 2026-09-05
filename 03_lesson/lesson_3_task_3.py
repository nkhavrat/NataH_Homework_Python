from address import Address
from mailing import Mailing

from_address = Address('445032', 'Самара', 'Ленина', '5', '43')
to_address = Address('445028', 'Тольятти', 'Свердлова', '9', '5')

mailing = Mailing(from_address, to_address, cost=500, track='456373')

print(mailing)
