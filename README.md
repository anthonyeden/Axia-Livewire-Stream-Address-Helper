# Axia Livewire Stream Address Helper
Python helper methods for Axia Livewire Audio-Over-IP Multicast Addresses.

These methods help you deal with the Multicast IP Addresses for an Axia Livewire network in a Python script. It was inspired and based on [this gist](https://gist.github.com/kylophone/a10e2c88ced3bf5e7674).

You may use this script as the basis for dealing with other parts of a Axia Livewire network, such as listening to audio, setting routes, controling audio consoles, or even [generating your own SDP file](http://www.telosalliance.com/images/Axia%20Products/Support%20Documents/Tech%20Tips/Playing-Livewire-Streams-Using-SDP-Rev-3-2015.pdf) to listen to a stream on your PC.

This script does not talk to the Livewire Advertisment Protocol. It just maniplates IP addresses and stream numbers.

## How to use this script

To import the method, copy "AxiaLivewireAddressHelper.py" to your project directory and

    import AxiaLivewireAddressHelper

To find the multicast address for standard stream #2100

    AxiaLivewireAddressHelper.streamNumToMulticastAddr("2100", "standard")

To find the multicast address for standard stream backfeed #2100

    AxiaLivewireAddressHelper.streamNumToMulticastAddr("2100", "backfeed_standard")

To finds the multicast address for livestream backfeed #2100

    AxiaLivewireAddressHelper.streamNumToMulticastAddr("2100", "backfeed_livestream")

To find the multicast address for surround stream #2100

    AxiaLivewireAddressHelper.streamNumToMulticastAddr("2100", "surround")

To find the stream number for multicast address 239.192.8.52

    AxiaLivewireAddressHelper.multicastAddrToStreamNum("239.192.8.52")

To find the stream number for multicast address 239.193.8.52

    AxiaLivewireAddressHelper.multicastAddrToStreamNum("239.193.8.52")

## More info on the Axia Livewire Protocol

* [What is Livewire+?](http://www.telosalliance.com/Axia/Livewire-AoIP-Networking) (Axia Website)
* [Axia Livewire Channel Numbering](http://www.telosalliance.com/images/Axia%20Products/Support%20Documents/Tech%20Tips/AxiaLivewireChannelNumbering.pdf) (Axia Website - PDF)
* [A Look At Livewire](https://github.com/kylophone/a-look-at-livewire) (Github)
* ["Audio Over IP: Building Pro AoIP Systems with Livewire" by Steve Church & Skip Pizzi](http://www.amazon.com/Audio-Over-IP-Building-Livewire-ebook/dp/B009OYSVV8) (2010 Book)

## Contributing

Contributions are welcomed. Feel free to submit a pull request to fix bugs or add additional functionality to this script.
