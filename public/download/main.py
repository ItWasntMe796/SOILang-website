import sys

try:
    READER = open(sys.argv[1])
except:
    print("Error, no file specified")
    sys.exit()

count = 0;

text = True

for er in READER.read():

    if (er == ']'):

        print()

        count = 0;

        text = True

    if (count == 2):

        sys.stdout.write(er);

    if er == '[':

        count = 2;

        text = False
    
    if (text):
        if (er == '.'):
            input();