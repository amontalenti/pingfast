from flask import Flask, make_response
import xml.etree.ElementTree as ET
from xml.dom import minidom
import pingdom
import settings

def create_app():
    return Flask("health")

app = create_app()
app.config.from_pyfile('settings.py')

@app.route('/response/<check_id>', methods=['GET', 'POST'])
def health(check_id):
    """Returns the response time and status of the pingdom check
    speicified by check_id"""
    pingdom_conn = pingdom.Pingdom(
        username=settings.PRIMARY_USERNAME,
        password=settings.PRIMARY_PASSWORD,
        appkey=settings.PRIMARY_APPKEY
    )
    status, responsetime = pingfast_status(pingdom_conn, check_id)
    if status is None:
        return valid_xml(make_error_element())
    return valid_xml(make_status_element(status, responsetime))

def pingfast_status(pingdom_conn, check_id, thresholds=None, default_threshold=1000):
    if thresholds is None:
        thresholds = {}
    checks = pingdom_conn.method('checks')
    for check in checks['checks']:
        threshold = thresholds.get(check_id, default_threshold)
        if str(check['id']) == check_id:
            if int(check['lastresponsetime']) > threshold:
                status = 'Not OK'
            else:
                status = 'OK'
            responsetime = check['lastresponsetime']
            return status, responsetime
    return None, None

def make_status_element(status, responsetime):
    check_root = ET.Element('pingdom_http_custom_check')
    status_elem = ET.SubElement(check_root, 'status')
    status_elem.text = status
    time = ET.SubElement(check_root, 'response_time')
    time.text = str(responsetime)
    return check_root

def make_error_element():
    check_root = ET.Element('pingdom_http_custom_check')
    err = ET.SubElement(check_root, 'err')
    err.text = "Invalid ID"
    return check_root

def valid_xml(et_elem):
    # create the rough ElementTree string
    markup_str = ET.tostring(et_elem, 'utf-8')
    # reparse it for validity
    reparsed = minidom.parseString(markup_str)
    # pretty-print it w/ indentation
    pretty = reparsed.toprettyxml(indent="    ")
    # make a Flask response so we can set headers
    resp = make_response(pretty)
    # set XML mime type
    resp.headers['Content-Type'] = "application/xml"
    return resp

if __name__ == '__main__':
    app.run(debug=True)
