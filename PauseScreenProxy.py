# coding=utf-8
import client.extraClientApi as clientApi
CustomUIScreenProxy = clientApi.GetUIScreenProxyCls()
ViewBinder = clientApi.GetViewBinderCls()

class PauseScreenProxy(CustomUIScreenProxy):
    def __init__(self, screenName, screenNode):
        CustomUIScreenProxy.__init__(self, screenName, screenNode)
        self.node = screenNode

    def OnCreate(self):
        print("PauseScreenProxy Create")

    def OnDestroy(self):
        print("PauseScreenProxy Destroy")

    def OnTick(self):
        pass

    @ViewBinder.binding(ViewBinder.BF_ButtonClickUp, '#snow.setting_click')
    def click(self, args):
        print('clicked')
