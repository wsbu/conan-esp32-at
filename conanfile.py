# (C)2019 Red Lion Controls, Inc. All rights reserved. Red Lion, the Red Lion
# logo and Sixnet are registered trademarks of Red Lion Controls, Inc. All other
# company and product names are trademarks of their respective owners.
import os

from conans import ConanFile
from conans.errors import ConanException


class Esp32AT(ConanFile):
    name = 'esp32-at'
    version = '1.1.3.0'
    license = 'Proprietary'
    url = 'https://bitbucket.org/redlionstl/esp32-at'
    description = 'AT library for ESP32 ESP-IDF'
    settings = 'compiler', 'build_type', 'arch'

    scm = {
        'type': 'git',
        'url': 'https://github.com/wsbu/esp32-at.git',
        'revision': 'v' + version
    }

    def configure(self):
        del self.settings.compiler.libcxx
        if not self.settings.arch or self.settings.arch not in ['esp32', 'esp8266']:
            raise ConanException('Invalid architecture {}. Only esp32 and esp8266 allowed.'.format(self.settings.arch))

    def package(self):
        self.copy('*', src=os.path.join('components', 'at'), excludes=('component.mk',))

    def package_info(self):
        self.cpp_info.libs = ['at_core']
