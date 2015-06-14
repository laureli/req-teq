import requests, sys

# enter url on the commandline
s = str(sys.argv[1])
breaker = '- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -'
breaker1 = ' - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -'

for url in range(1, len(sys.argv)):
    s = sys.argv[url]
    print s

    r = requests.get(s, verify=False)
    print "The URL you're checking is %s" % s
    print "Header count is %s" % (len(r.headers))

# get / print all of the headers

    for h in r.headers:
        print h, '::', r.headers[h]
    print 'done with bulk header printing'

# get / print a specific header (single)

    h = raw_input('what specific header do you want to check for? type 0 to exit: ')
    while h != '0':
        if h in r.headers:
            print h, '::', r.headers[h]
            h = raw_input('check another header? type 0 to exit: ')
        else:
            h = raw_input("that isn't a header. again, type 0 to exit: ")


# get a specific group of headers
    # designated at the commandline probably?


# we're done with 1 url here
    print breaker
    print breaker1
    print breaker


# print the content of the page
# print r.content
