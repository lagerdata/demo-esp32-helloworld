import os
import esptool

# esptool.py -p (PORT) -b 460800 --before default_reset --after hard_reset --chip esp32  write_flash --flash_mode dio --flash_size detect --flash_freq 40m 0x1000 build/bootloader/bootloader.bin 0x8000 build/partition_table/partition-table.bin 0x10000 build/hello-world.bin

port = "/dev/ttyUSB2"
argv = ['-p', port, '-b', '460800', '--before', 'default_reset', '--after', 'hard_reset', '--chip', 'esp32', 'write_flash', '--flash_mode', 'dio', '--flash_size', 'detect', '--flash_freq', '40m', '0x1000', 'bootloader.bin', '0x8000', 'partition-table.bin', '0x10000', 'hello-world.bin']

esptool.main(argv)