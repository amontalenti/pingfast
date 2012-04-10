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

Authors
-------

Emmett Butler (all coding & testing)
Andrew Montalenti (concept & documentation)

