mockOutput = """
3 sink(s) available.
    index: 0
	name: <alsa_output.pci-0000_01_00.1.hdmi-stereo>
	driver: <module-alsa-card.c>
	flags: HARDWARE DECIBEL_VOLUME LATENCY DYNAMIC_LATENCY
	state: IDLE
	suspend cause:
	priority: 9050
	volume: front-left: 13755 /  21% / -40.68 dB,   front-right: 13755 /  21% / -40.68 dB
	        balance 0.00
	base volume: 65536 / 100% / 0.00 dB
	volume steps: 65537
	muted: yes
	current latency: 30.96 ms
	max request: 6 KiB
	max rewind: 344 KiB
	monitor source: 0
	sample spec: s16le 2ch 44100Hz
	channel map: front-left,front-right
	             Stereo
	used by: 0
	linked by: 1
	configured latency: 40.00 ms; range is 0.50 .. 1999.82 ms
	card: 0 <alsa_card.pci-0000_01_00.1>
	module: 6
	properties:
		alsa.resolution_bits = "16"
		device.api = "alsa"
		device.class = "sound"
		alsa.class = "generic"
		alsa.subclass = "generic-mix"
		alsa.name = "HDMI 0"
		alsa.id = "HDMI 0"
		alsa.subdevice = "0"
		alsa.subdevice_name = "subdevice #0"
		alsa.device = "3"
		alsa.card = "2"
		alsa.card_name = "HDA ATI HDMI"
		alsa.long_card_name = "HDA ATI HDMI at 0xfddfc000 irq 28"
		alsa.driver_name = "snd_hda_intel"
		device.bus_path = "pci-0000:01:00.1"
		sysfs.path = "/devices/pci0000:00/0000:00:02.0/0000:01:00.1/sound/card2"
		device.bus = "pci"
		device.vendor.id = "1002"
		device.vendor.name = "Advanced Micro Devices, Inc. [AMD/ATI]"
		device.product.id = "aab0"
		device.product.name = "Cape Verde/Pitcairn HDMI Audio [Radeon HD 7700/7800 Series]"
		device.string = "hdmi:2"
		device.buffering.buffer_size = "352768"
		device.buffering.fragment_size = "176384"
		device.access_mode = "mmap+timer"
		device.profile.name = "hdmi-stereo"
		device.profile.description = "Digital Stereo (HDMI)"
		device.description = "Cape Verde/Pitcairn HDMI Audio [Radeon HD 7700/7800 Series] Digital Stereo (HDMI)"
		alsa.mixer_name = "ATI R6xx HDMI"
		alsa.components = "HDA:1002aa01,00aa0100,00100300"
		module-udev-detect.discovered = "1"
		device.icon_name = "audio-card-pci"
	ports:
		hdmi-output-0: HDMI / DisplayPort (priority 5900, latency offset 0 usec, available: yes)
			properties:
				device.icon_name = "video-display"
	active port: <hdmi-output-0>
  * index: 2
	name: <alsa_output.pci-0000_00_14.2.iec958-stereo>
	driver: <module-alsa-card.c>
	flags: HARDWARE HW_MUTE_CTRL DECIBEL_VOLUME LATENCY DYNAMIC_LATENCY
	state: IDLE
	suspend cause:
	priority: 9958
	volume: front-left: 0 /   0% / -inf dB,   front-right: 0 /   0% / -inf dB
	        balance 0.00
	base volume: 65536 / 100% / 0.00 dB
	volume steps: 65537
	muted: no
	current latency: 38.61 ms
	max request: 6 KiB
	max rewind: 344 KiB
	monitor source: 4
	sample spec: s16le 2ch 44100Hz
	channel map: front-left,front-right
	             Stereo
	used by: 0
	linked by: 1
	configured latency: 40.00 ms; range is 0.50 .. 1999.82 ms
	card: 3 <alsa_card.pci-0000_00_14.2>
	module: 9
	properties:
		alsa.resolution_bits = "16"
		device.api = "alsa"
		device.class = "sound"
		alsa.class = "generic"
		alsa.subclass = "generic-mix"
		alsa.name = "ALC889 Digital"
		alsa.id = "ALC889 Digital"
		alsa.subdevice = "0"
		alsa.subdevice_name = "subdevice #0"
		alsa.device = "1"
		alsa.card = "1"
		alsa.card_name = "HDA ATI SB"
		alsa.long_card_name = "HDA ATI SB at 0xfdff4000 irq 16"
		alsa.driver_name = "snd_hda_intel"
		device.bus_path = "pci-0000:00:14.2"
		sysfs.path = "/devices/pci0000:00/0000:00:14.2/sound/card1"
		device.bus = "pci"
		device.vendor.id = "1002"
		device.vendor.name = "Advanced Micro Devices, Inc. [AMD/ATI]"
		device.product.id = "4383"
		device.product.name = "SBx00 Azalia (Intel HDA)"
		device.form_factor = "internal"
		device.string = "iec958:1"
		device.buffering.buffer_size = "352768"
		device.buffering.fragment_size = "176384"
		device.access_mode = "mmap+timer"
		device.profile.name = "iec958-stereo"
		device.profile.description = "Digital Stereo (IEC958)"
		device.description = "Built-in Audio Digital Stereo (IEC958)"
		alsa.mixer_name = "Realtek ALC889"
		alsa.components = "HDA:10ec0889,1458a002,00100004"
		module-udev-detect.discovered = "1"
		device.icon_name = "audio-card-pci"
	ports:
		iec958-stereo-output: Digital Output (S/PDIF) (priority 0, latency offset 0 usec, available: unknown)
			properties:

	active port: <iec958-stereo-output>
    index: 9
	name: <alsa_output.usb-Logitech_Logitech_G930_Headset-00.iec958-stereo>
	driver: <module-alsa-card.c>
	flags: HARDWARE DECIBEL_VOLUME LATENCY DYNAMIC_LATENCY
	state: RUNNING
	suspend cause:
	priority: 9048
	volume: front-left: 20201 /  31% / -30.67 dB,   front-right: 20201 /  31% / -30.67 dB
	        balance 0.00
	base volume: 65536 / 100% / 0.00 dB
	volume steps: 65537
	muted: no
	current latency: 26.65 ms
	max request: 4 KiB
	max rewind: 344 KiB
	monitor source: 17
	sample spec: s16le 2ch 44100Hz
	channel map: front-left,front-right
	             Stereo
	used by: 1
	linked by: 3
	configured latency: 23.22 ms; range is 0.50 .. 2000.00 ms
	card: 10 <alsa_card.usb-Logitech_Logitech_G930_Headset-00>
	module: 30
	properties:
		alsa.resolution_bits = "16"
		device.api = "alsa"
		device.class = "sound"
		alsa.class = "generic"
		alsa.subclass = "generic-mix"
		alsa.name = "USB Audio"
		alsa.id = "USB Audio"
		alsa.subdevice = "0"
		alsa.subdevice_name = "subdevice #0"
		alsa.device = "0"
		alsa.card = "0"
		alsa.card_name = "Logitech G930 Headset"
		alsa.long_card_name = "Logitech Logitech G930 Headset at usb-0000:02:00.0-1, full speed"
		alsa.driver_name = "snd_usb_audio"
		device.bus_path = "pci-0000:02:00.0-usb-0:1:1.0"
		sysfs.path = "/devices/pci0000:00/0000:00:04.0/0000:02:00.0/usb1/1-1/1-1:1.0/sound/card0"
		udev.id = "usb-Logitech_Logitech_G930_Headset-00"
		device.bus = "usb"
		device.vendor.id = "046d"
		device.vendor.name = "Logitech, Inc."
		device.product.id = "0a1f"
		device.product.name = "G930"
		device.serial = "Logitech_Logitech_G930_Headset"
		device.form_factor = "headset"
		device.string = "iec958:0"
		device.buffering.buffer_size = "352800"
		device.buffering.fragment_size = "176400"
		device.access_mode = "mmap+timer"
		device.profile.name = "iec958-stereo"
		device.profile.description = "Digital Stereo (IEC958)"
		device.description = "G930 Digital Stereo (IEC958)"
		alsa.mixer_name = "USB Mixer"
		alsa.components = "USB046d:0a1f"
		module-udev-detect.discovered = "1"
		device.icon_name = "audio-headset-usb"
		device.intended_roles = "phone"
	ports:
		iec958-stereo-output: Digital Output (S/PDIF) (priority 0, latency offset 0 usec, available: unknown)
			properties:

	active port: <iec958-stereo-output>
"""

badCommand = """Unknown command: obviously-fake
"""

from parser import parseList
import json
import unittest
class TestStringMethods(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.data = parseList(mockOutput)

    def test_correctActive(self):
        self.assertTrue(self.data['activeItem'] == '2')

    def test_capturesAttributesWithSpaces(self):
        self.assertTrue(self.data['2']['max request'] == '6 KiB')

    def test_capturesProperties(self):
        self.assertEquals(self.data['2']['properties']['sysfs.path'], '/devices/pci0000:00/0000:00:14.2/sound/card1')

    def test_supportsMultiline(self):
        self.assertTrue('\nbalance' in self.data['0']['volume'])

    def test_indexedCorrectly(self):
        self.assertTrue(self.data['9']['name'] == '<alsa_output.usb-Logitech_Logitech_G930_Headset-00.iec958-stereo>')
        self.assertTrue(self.data['0']['name'] == '<alsa_output.pci-0000_01_00.1.hdmi-stereo>')

    def test_raises(self):
        with self.assertRaises(Exception) as context:
            parseList(badCommand)

        self.assertTrue(str(context.exception).startswith('Unknown command'))

if __name__ == '__main__':
    unittest.main()