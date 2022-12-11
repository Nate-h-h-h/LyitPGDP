from devices import Firewall
# Create a firewall instance
firewall27 = Firewall("firewall27")
# Configure it
firewall27.configure_firewall()
# Create a firewall instance
firewall28 = Firewall("firewall28")
# Verify a CRC
firewall28.calculate_crc("dummy data")

from devices import switches
# Create a switches instance
switches27 = switches("switches27")
# Configure it
switches27.configure_switches()
# Create a switches instance
switches28 = switches("switches28")
# Verify a CRC
switches28.calculate_crc("dummy data")

from devices import load_balancers
# Create a load_balancers instance
load_balancers27 = load_balancers("load_balancers27")
# Configure it
load_balancers27.configure_switches()
# Create a load_balancers instance
load_balancers28 = load_balancers("load_balancers28")
# Verify a CRC
load_balancers28.calculate_crc("dummy data")
