
# def sendform():
#     print('''
#     <html>
#     <body><form action ='cgi-bin/ssp2.py' methods='get'>
#             <label for="myname"> enter your name </label>
#             <input type="text" name="firstname" id="myname" value="jai">
#             <input type="button" >
#         </form> 
#         </body>
#         </html>
#     ''')

#     def sendpage(name):
#         print('''
#         <html>
#         <body>
#         <h1>hello %s</h1>
#         </body>
#         ''')
#         if not qs:
#             sendHeaders()
#             sendform()
#         else:


# headers = ["content-type: text/html"]

# print("content-type: text/html\n")
# qs = os.environ['QUERY_STRING']


# def sendHeaders():
#     for h in headers:
#         print(h)
#         print("\n")


# def sendForm():
#     print('''
#     <htm>
#     <body>
#     <h1> Hello{0}</h1>
#     </body>
#     </html>
#     '''.format(name))


# if not qs:
#     sendHeaders()
#     sendForm()
# else:

#     if 'firstname' in qs:
#         name = qs.split('=')[1]
#     else:
#         name = 'No name provided'
#     sendHeaders()
#     sendForm()
import os

headers=["Content-Type : text/html"]
qs= os.environ['QUERY_STRING']

def sendHeader():
    for h in headers:
        print(h)
    print("\n")

def sendForm():
    print('''
    <html>
        <body>
            <form action="ssp2.py" method="get">
                <label for="myname">Enter Your Name</label>
                <input id="myname" type="text" name="firstname" value="Mann"/>
                <input type="submit"/>
            </form>
        </body>
    </html>
    ''')

def sendPage(name):
    print('''
          <html>
            <body>
                <h1>Hello {0}</h1>
            </body>
          </html>'''.format(name))

if not qs:
    sendHeader()
    sendForm()
else:
    if 'firstname' in qs:
        name = qs.split('=')[1]
    else:
        name = "No Name Provided"
    sendHeader()
    sendPage(name)
