# BBDN-WsSoapPythonWorkshop

**NOTE: SOAP Web Services have been removed from the Blackboard Learn product as of the Q4 2019 Release (3900.0.0)**

This project contains sample code for a workshop. The purpose of this workshop is to learn how to interact with the Blackboard Learn SOAP Web Services in Python. This sample code was built with Python 2.7.9.

###Project at a glance:
- Target: Blackboard Learn 9.1 SP 11 minimum
- Source Release: v1.0
- Release Date  2015-08-19
- Author: shurrey
- Tested on Blackboard Learn 9.1 April 2014 release

###Requirements:
- Python  2.7.9
- SUDS: https://bitbucket.org/jurko/suds

### Setting Up Your Development Environment
You will first need to install Python 2.7.9. You can use tools like brew or ports to install, or run the installation manually.

In addition, you will need to install SUDS. I am using a branch of SUDS that is maintained (the original SUDS project has gone stagnant).

You can download this library from here:<br />
  https://bitbucket.org/jurko/suds

Addionally, you can also install the library with pip:<br />
  **pip install suds-jurko**

<i>NOTE: SUDS and the SUDS fork listed above are third-party libraries not associated with Blackboard in any way. Use at your own risk.</i>

### Configuring the Script
Also, this script is currently configured to use the Learn Developer Virtual Machine. You may use this with other systems, it will just require you to modify the following section in the main application loop. The only thing you should have to change is the server variable:

    protocol = 'https'
    server = 'localhost:9877'
    service_path = 'webapps/ws/services'
    url_header = protocol + "://" + server + "/" + service_path + "/"

### Developer Virtual Machine and SSL Certificate Checking
If you decide to use the Blackboard Developer virtual machine, it is important to note that this VM contains a self-signed certificate, which will cause Python's urllib2 module to fail. Because the Blackboard Learn 9.1 April and newer releases require you to use SSL, you must make a change to Python's urllib2 module manually. THIS CHANGE WILL BYPASS SSL CERTIFICATE CHECKING, so be sure to undo this change when rolling out to production.

To make this change, find the library urllib2. You can find it in the directory you installed Python. For me it is:
    .../python/2.7.9/Frameworks/Python.framework/Versions/2.7/lib/python2.7/urllib2.py

Edit this file, and search for the class HTTPHandler. It will look like this:

        class HTTPHandler(AbstractHTTPHandler):
        
            def http_open(self, req):
                return self.do_open(httplib.HTTPConnection, req)
        
            http_request = AbstractHTTPHandler.do_request_
        
        if hasattr(httplib, 'HTTPS'):
            class HTTPSHandler(AbstractHTTPHandler):
        
                def __init__(self, debuglevel=0, context=None):
                    AbstractHTTPHandler.__init__(self, debuglevel)
                    self._context = context
        
                def https_open(self, req):
                    return self.do_open(httplib.HTTPSConnection, req,
                        context=self._context)
        
                https_request = AbstractHTTPHandler.do_request_
        
Make it look like this:

        class HTTPHandler(AbstractHTTPHandler):
        
            def http_open(self, req):
                return self.do_open(httplib.HTTPConnection, req)
        
            http_request = AbstractHTTPHandler.do_request_
        
        if hasattr(httplib, 'HTTPS'):
            class HTTPSHandler(AbstractHTTPHandler):
        
                def __init__(self, debuglevel=0, context=None):
                    gcontext = ssl.SSLContext(ssl.PROTOCOL_TLSv1)   # Turn off SSL Cert Checking DEV ONLY
                    AbstractHTTPHandler.__init__(self, debuglevel)
                    self._context = gcontext                        # Change context to gcontext
        
                def https_open(self, req):
                    return self.do_open(httplib.HTTPSConnection, req,
                        context=self._context)
        
                https_request = AbstractHTTPHandler.do_request_

### Gradebook.WS WSDL and Learn October 2014
There is a bug in the Blackboard Learn 9.1 October 2014 release with the WSDL for gradebook.ws. This will cause SUDS to fail when trying to ingest the WSDL. 

For more information and work-arounds for this bug, see the article <a href="https://blackboard.secure.force.com/btbb_articleview?id=kA370000000H5Fc" target="_blank">here</a>.

- If you follow workaround 1, simply change the initial gradebookWS call:<br/>
  <pre>
    url = url_header + 'Gradebook.WS?wsdl'
  </pre>
with this:<br/>
<pre>
    url = 'file:///Users/shurrey/wsdl/Gradebook.xml'
</pre>

Just be sure to replace my absolute path to the absolute path on your file system.

- If you follow workaround 2, the code should work as-is.

### Conclusion
Look for a corresponding Gist with instuctions to take advantage of this workshop on your own time. 
