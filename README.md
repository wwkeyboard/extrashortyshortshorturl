Very simple url shortener. 

INSTALL
=======

    pip install twisted shove
    python server.py -f "file://`pwd`/storage" -p 8080
    
And you're off, listening on port 8080! If you really want to get crazy, you can add some arguments. 

    python server.py -f "file://`pwd`/storage" -p 8080
    
The argument to server can take anything that Shove will recognize. If you really want to point this a something fancy like mysql, you can; but I don't know what that will get you.

API
===

    $ curl -d "url=www.xkcd.com" http://localhost:8080/
    http://127.0.0.1:8080/0
    
    $ curl --verbose http://localhost:8080/0
    * About to connect() to localhost port 8080 (#0)
    *   Trying ::1... Connection refused
    *   Trying 127.0.0.1... connected
    * Connected to localhost (127.0.0.1) port 8080 (#0)
    > GET /d HTTP/1.1
    > User-Agent: curl/7.21.4 (universal-apple-darwin11.0) libcurl/7.21.4 OpenSSL/0.9.8r zlib/1.2.5
    > Host: localhost:8080
    > Accept: */*
    > 
    < HTTP/1.1 302 Found
    < Date: Fri, 23 Mar 2012 11:46:04 GMT
    < Content-Length: 29
    < Content-Type: text/html
    < Location: http://www.xkcd.com
    < Server: TwistedWeb/11.0.0
    < 
    * Connection #0 to host localhost left intact
    * Closing connection #0
    onward to http://www.xkcd.com
    
Please note, this will put whatever you give it into the Location header, there is currently no check to make sure what you are trying to send people to is really a url.