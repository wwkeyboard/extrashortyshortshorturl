from twisted.web import server, resource
from twisted.internet import reactor
import optparse
import shove
import sys

parser = optparse.OptionParser()
parser.add_option("-p", dest="port", default="8080")
parser.add_option("-f", dest="filename", default="file://./storage")
(options, args) = parser.parse_args()

file_store = options.filename
print "loading storage %s" % file_store
storage = shove.Shove(file_store)

try:
    storage['num_urls']
except KeyError:
    storage['num_urls'] = 0

class Redirector(resource.Resource):
    isLeaf = True

    def render_GET(self, request):
        key = "%s" % request.postpath[0]
        try:
            destination = storage[key]
        except KeyError:
            return "Sorry couldn't find that key"
        print "%s -> %s" % (key, destination)
        request.redirect(destination)
        return "onward to %s" % destination

    def render_POST(self, request):
        request_num = storage['num_urls']
        storage['num_urls'] =  request_num + 1
        key = "%x" % request_num
        destination = "http://%s" % request.args['url'][0]
        storage[key] = destination
        print "%s <- %s" % (key, destination)
        return "http://127.0.0.1:8080/%s" % key

reactor.listenTCP(int(options.port), server.Site(Redirector()))
reactor.run()
