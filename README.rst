pingfast
--------

Pingdom response time monitoring service;
ensure your services are not only up, 
but also fast!

Overview
--------

This is a Python web service that uses Pingdom's API and infrastructure to
create a global response-time monitoring service from your existing Pingdom
checks.

Rationale: Pingdom provides a great web interface and infrastructure for
ensuring your services are perceived as "up" by remote clients from pinging
locations across the world. And, within Pingdom's web interface, you can track
response time fluctuations in addition to uptime fluctuations.  However, there
are times when your services may not go "down", but may be "effectively down"
due to poor response time. Think of an API that is meant to respond in <500ms,
but suddenly starts responding in 5-8 seconds.

Pingdom's API provides all the information we need in order to monitor these
response times, but we want to be alerted about them in the same way we are
alerted about other downtime events. Enter pingfast.

pingfast is a simple Python web service (implemented with Flask) that
implements Pingdom's "custom check API". This is an XML endpoint that specifies
the condition of a service's uptime. pingfast also includes some tools that
allow you to "sync" your existing Pingdom account to a second "pingfast"
account, which is to say, a second Pingdom account that is used exclusively for
monitoring response times of your existing Pingdom checks.

Configuration
-------------

There is an example configuration file in `examples/localsettings.py`. Copy
this file to the root directory of the project and customize with your values.

THRESHOLDS
  a dictionary mapping Pingdom check_id's to response time thresholds (in milliseconds);
  if none is specified, the default of 1000ms (1s) is assumed

IGNORES
  a sequence of Pingdom check ids which should be "ignored" for the purposes of the ``pingdom_sync`` command
  that is, they won't be copied over to the secondary account because they are not worth doing response time monitoring on

DEPLOY_SERVER, DEPLOY_PORT
  a server address that will be used for deploying the project via Fabric; this is the same 
  host that will be used by the `pingdom_sync` management command

DEPLOY_HOSTNAME
  local hostname of deployment server; used for enabling/disabling debug mode

DEPLOY_USER
  user account (accessible via SSH) used for remote deployment
  
DEPLOY_DIR
  directory on DEPLOY_SERVER to use for storing the project files

PRIMARY_USERNAME, PRIMARY_PASSWORD, PRIMARY_APPKEY
  Pingdom credentials and API App Key used for your "primary" Pingdom account

SECONDARY_USERNAME, SECONDARY_PASSWORD, SECONDARY_APPKEY
  Pingdom credentials and API App Key used for your "secondary" Pingdom account;
  this is the account where the pingfast custom checks are created, and the target 
  of the `pingdom_sync` management command

Requirements
------------

This project depends on `Flask`_ to implement the web service. It uses dcraig's
`Python RESTful wrapper for the Pingdom API`_, as well, but embeds it here 
as `pingdom.py` for convenience.

.. _Flask: http://flask.pocoo.org/
.. _Python RESTful wrapper for the Pingdom API: https://github.com/drcraig/python-restful-pingdom

Authors
-------

* Emmett Butler - initial coding & testing
* Andrew Montalenti - concept, documentation & refactoring

