import wmi
import re
import os
#import pywin32


class UserInfo:
    def __init__(self):
        self.computer = wmi.WMI()
        self.Os_info = self.computer.Win32_OperatingSystem()[0]

    def gpu_info(self):
        try:
            return self.computer.Win32_VideoController()[0].Name
        except:
            return 'no data'

    def cpu_info(self):
        try:
            return self.computer.Win32_Processor()[0].Name.rstrip()
        except:
            return 'no data'

    def name_info(self):
        try:
            name = self.Os_info.Caption
            result = re.sub(r'[^A-Za-z \d+]', '', name)
            return result
        except:
            return 'no data'

    def version_info(self):
        try:
            return ' '.join([self.Os_info.Version, self.Os_info.BuildNumber])
        except:
            return 'no data'

    def ram_info(self):
        try:
            return str(round((float(self.Os_info.TotalVisibleMemorySize) / 1048576), 2))
        except:
            return 'no data'

    def location_info(self):
        try:
            return self.computer.Win32_OperatingSystem()[0].CountryCode
        except:
            return 'no data'

    def username_info(self):
        try:
            name = os.getlogin()
            result = re.sub(r'[^A-Za-z \d+]', '', name)
            if result == '':
                result = 'Anon'
            return result
        except:
            return 'no data'