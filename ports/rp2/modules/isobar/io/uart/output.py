from ..output import OutputDevice
from ...pattern import Pattern

try:
    from machine import UART
except ModuleNotFoundError:
    pass

class UARTOutputDevice(OutputDevice):
    """
    UARTOutputDevice: Wraps MIDI messages in UART.
    /note [ note, velocity, channel ]
    /control [ control, value, channel ]
    """

    def __init__(self, port, baud):
        """
        Args:
            port
            baud
        """
        try:
            self.uart = UART(port, baud)

        except NameError:
            raise Exception("UART must be installed")

    def note_on(self, note=60, velocity=64, channel=0):
        self.uart.send_message("/note %s %s"%(velocity, channel))

    def note_off(self, note=60, channel=0):
        self.uart.send_message("/note %s %s"%(0, channel))

    def control(self, control, value, channel=0):
        self.uart.send_message("/control %s %s"%(value, channel))
    """
    def send(self, address, params=None):
        if params is not None:
            params = [Pattern.value(param) for param in params]
        self.uart.send_message(address, params)
    """
