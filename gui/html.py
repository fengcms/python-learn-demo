import htmlPy

web_app = htmlPy.WebAppGUI(title=u"test", maximized=True)
web_app.url = u"http://www.baidu.com/"

web_app.start()
