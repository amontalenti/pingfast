from flask import Flask
import xml.etree.ElementTree as ET
import pingdom
import parsely_keys
from settings import thresholds

def create_app():
    return Flask("health")

app = create_app()
app.config.from_pyfile('settings.py')

@app.route('/response/<check_id>', methods=['GET', 'POST'])
def health(check_id):
    """Returns the response time and status of the pingdom check
    speicified by check_id"""
    p = pingdom.Pingdom(
        username=parsely_keys.primary_username,
        password=parsely_keys.primary_password,
        appkey=parsely_keys.primary_appkey
    )
    checks = p.method('checks')

    checkroot = ET.Element('pingdom_http_custom_check')
    for check in checks['checks']:
        if str(check['id']) == check_id:
            status = ET.SubElement(checkroot, 'status')
            if int(check['lastresponsetime']) > thresholds[check_id]:
                status.text = 'Not OK'
            else:
                status.text = 'OK'
            time = ET.SubElement(checkroot, 'response_time')
            time.text = str(check['lastresponsetime'])
            return ET.tostring(checkroot)
    err = ET.SubElement(checkroot, 'err')
    err.text = "Invalid ID"
    return ET.tostring(checkroot)

if __name__ == '__main__':
    app.run(debug=True)
