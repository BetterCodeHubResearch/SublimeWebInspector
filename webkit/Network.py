from .wkutils import WebkitObject, Command


def clearBrowserCache():
    command = Command('Network.clearBrowserCache', {})
    return command


def canClearBrowserCache():
    command = Command('Network.canClearBrowserCache', {})
    return command


def setCacheDisabled(value):
    command = Command('Network.setCacheDisabled', {'cacheDisabled': value})
    return command

def setUserAgentOverride(value):
    command = Command('Network.setUserAgentOverride', {'userAgent': value})
    return command


class RequestId(WebkitObject):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return self.value

    def __repr__(self):
        return self.value
