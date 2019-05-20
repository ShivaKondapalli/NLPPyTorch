from PyPDF2 import PdfFileReader

# This the function based implementation

path = "data/Apocalypse_Now.pdf"

file_object = open(path, 'rb')


def read_data(file_object):

    text = PdfFileReader(file_object)

    if text.isEncrypted:
        text.decrypt('')

    return text


def extract_all_data(text):

    my_lst = []

    for i in range(1, text.numPages):

        pageobj = text.getPage(i)

        my_lst.append(pageobj.extractText())

    return my_lst


def main():
    data_list = extract_all_data(read_data(file_object))
    p = [data.split() for data in data_list]
    print(p[1])
    print(len(p[1]))


if __name__ == '__main__':
    main()

file_object.close()