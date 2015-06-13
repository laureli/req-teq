import requests, sys

# enter url on the commandline
s = str(sys.argv[1])

for url in range(1, len(sys.argv)):
    s = sys.argv[url]
    print s

    r = requests.get(s, verify=False)
    print "The URL you're checking is %s" % s
    print "Header count is %s" % (len(r.headers))

    for h in r.headers:
        print h, '::', r.headers[h]
        print '- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -'

for i in range(2):
    print '++++++++++++++++++++'


# print the content of the page
# print r.content
