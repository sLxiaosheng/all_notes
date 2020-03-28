
def sanitize(time_string):
    if '-' in time_string:
        splitter = '-'
    elif ':' in time_string:
        splitter = ':'
    else:
        return(time_string)
    (mins, secs) = time_string.split(splitter)
    return(mins + '.' + secs)

def get_data(filename):
    try:
        with open(filename) as f:
            data = f.readline()
        return(data.strip().split(','))
    except IOError as ioerr:
        print('File error:' + str(ioerr))
        return(None)

Bob = get_data('boy.txt')
Lily = get_data('Lily.txt')
Tom = get_data('Tom.txt')
Bob = [sanitize(t) for t in Bob]
Bob = [Bob]
print(sorted(set(Bob))[0:3])
print(sorted(set([sanitize(t) for t in Lily]))[0:3])
print(sorted(set([sanitize(t) for t in Tom]))[0:3])