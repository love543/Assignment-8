import os

headers = ["content-type: text/html"]

print("content-type: text/html\n")
qs = os.environ['QUERY_STRING']


def sendHeaders():
    for h in headers:
        print(h)
        print("\n")


def sendform():
    print('''
    <html>
    <body><form action ='ssp2.py' method='get'>
            <label for="myname"> enter your name </label>
            <input type="text" name="firstname" id="myname" value="Shiv"/>
            <input type="button" >
        </form> 
        </body>
        </html>
    ''')

    def sendpage(name):
        print('''
        <html>
        <body>
        <h1>hello %s</h1>
        </body>
        '''.format(name))
        if not qs:
            sendHeaders()
            sendform()
        else:
            if 'firstname' in qs:
                name = qs.split('=')[1]
            else:
                name = 'no Name Provided'
            sendHeaders()
            sendpage(name)

