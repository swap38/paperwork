import ConfigParser
import os

class AppConfig(object):
    CONFIGFILE = "~/.paperwork"

    def __init__(self):
        self.read()

    def read(self):
        self.configparser = ConfigParser.SafeConfigParser()
        self.configparser.read([ os.path.expanduser(self.CONFIGFILE) ])
        if not self.configparser.has_section("Global"):
            self.configparser.add_section("Global")
        if not self.configparser.has_section("OCR"):
            self.configparser.add_section("OCR")
        # TODO(Jflesch): Load settings from the config file
        self._print_settings = None

    @property
    def workdir(self):
        try:
            return self.configparser.get("Global", "WorkDirectory")
        except:
            return os.path.expanduser("~/papers")

    @workdir.setter
    def workdir(self, wd):
        self.configparser.set("Global", "WorkDirectory", wd)

    @property
    def ocrlang(self):
        try:
            return self.configparser.get("OCR", "Lang")
        except:
            return "eng"

    @ocrlang.setter
    def ocrlang(self, lang):
        self.configparser.set("OCR", "Lang", lang)

    @property
    def print_settings(self):
        return self._print_settings

    @print_settings.setter
    def print_settings(self, settings):
        # TODO(Jflesch): Save settings in the config file
        self._print_settings = settings

    def write(self):
        f = os.path.expanduser(self.CONFIGFILE)
        print "Writing %s ... " % f
        with open(f, 'wb') as fd:
            self.configparser.write(fd)
        print "Done"
