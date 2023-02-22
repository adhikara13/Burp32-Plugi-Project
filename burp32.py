from burp import IBurpExtender, IContextMenuFactory
from burp import IHttpRequestResponse
from java.io import PrintWriter
from java.util import ArrayList
from javax.swing import JMenuItem
import base64

class BurpExtender(IBurpExtender):
    implements = [IBurpExtender, IContextMenuFactory]
    def registerExtenderCallbacks(self, callbacks):
        self._callbacks = callbacks
        self._helpers = callbacks.getHelpers()
        self._callbacks.setExtensionName("Base32 Encoder")

        self._stdout = PrintWriter(callbacks.getStdout(), True)

        callbacks.registerContextMenuFactory(self._MenuFactory(self._helpers, self))

        return

    class _MenuFactory(IContextMenuFactory):
        def __init__(self, helpers, extender):
            self._helpers = helpers
            self._extender = extender

        def createMenuItems(self, contextMenuInvocation):
            self._contextMenuInvocation = contextMenuInvocation
            self._selectedMessage = contextMenuInvocation.getSelectedMessages()[0]
    
            menuList = ArrayList()
            menuItem = JMenuItem("Encode request in Base32", actionPerformed=self._EncodeRequestInBase32)
            menuList.add(menuItem)
            return menuList
    
        def _EncodeRequestInBase32(self, event):
            httpRequest = self._selectedMessage.getRequest()
            httpRequestString = self._helpers.bytesToString(httpRequest)
            httpRequestBytes = httpRequestString.encode('utf-8')
            encodedRequest = base64.b32encode(httpRequestBytes)
            self._extender._stdout.println(encodedRequest)
            self._selectedMessage.setRequest(encodedRequest)
            return
