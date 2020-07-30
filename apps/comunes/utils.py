import os

def get_template_path(appname, template):
    path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    file = "{path}/{app}/templates/{app}/tabla.html".format(path=path, app=appname)
    if os.path.exists(file):
        template_name = "{app}/{html}".format(app=appname, html=template)
    else:
        template_name = "comunes/{html}".format(html=template)
    return template_name
