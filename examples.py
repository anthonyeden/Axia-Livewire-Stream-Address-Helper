import AxiaLivewireAddressHelper


# Finds the multicast address for standard stream #2100
streamAddr1 = AxiaLivewireAddressHelper.streamNumToMulticastAddr("2100", "standard")
print streamAddr1

# Finds the multicast address for standard stream backfeed #2100
streamAddr2 = AxiaLivewireAddressHelper.streamNumToMulticastAddr("2100", "backfeed_standard")
print streamAddr2

# Finds the multicast address for livestream backfeed #2100
streamAddr3 = AxiaLivewireAddressHelper.streamNumToMulticastAddr("2100", "backfeed_livestream")
print streamAddr3

# Finds the multicast address for surround stream #2100
streamAddr4 = AxiaLivewireAddressHelper.streamNumToMulticastAddr("2100", "surround")
print streamAddr4

# Finds the stream number for multicast address 239.192.8.52
streamNum1 = AxiaLivewireAddressHelper.multicastAddrToStreamNum("239.192.8.52")
print streamNum1

# Finds the stream number for multicast address 239.193.8.52
streamNum2 = AxiaLivewireAddressHelper.multicastAddrToStreamNum("239.193.8.52")
print streamNum2

