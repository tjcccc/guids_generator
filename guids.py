import sys
import uuid

def main():
    if not sys.argv[1].isnumeric():
        print('Please input a number')
        exit(1)

    guid_count = int(sys.argv[1])

    output = ''

    for i in range(guid_count):
        output += str(uuid.uuid4()).upper() + '\n'

    print(output)

    file = open('guids.txt', 'w')
    file.write(output)
    file.close()


if __name__ == '__main__':
    main()
