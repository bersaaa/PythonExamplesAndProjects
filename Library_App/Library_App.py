"""
Create the library.txt file. This file contains the title of the book, the author and the category. Read this file and then write the history books in history.txt and personal development books in personalGelisim.txt files.
"""
def input_data ():
    name = input ('Enter the book name: ')
    author = input ('Enter the author name: ')
    kind = input ('Enter the book kind: ')

    with open("Kutuphane.txt","a", encoding="utf-8") as file:
        file.write(name+','+ author+ ','+kind+','+'\n')
    file.close()

def read_data():

    with open("Kutuphane.txt","r",encoding="utf-8") as file:
        for satir in file:
            liste = satir.split(',')
            book_name = liste[0]
            book_author = liste[1]
            book_kind = liste[2]
            
            if (book_kind =='Tarih'):
                with open("Tarih.txt","a", encoding="utf-8") as file2:
                    file2.write(book_name+','+ book_author+ ','+book_kind+','+'\n')   
                file2.close()
            elif (book_kind == 'Kisisel Gelisim' ):
                with open("Kisiselg Gelisim.txt","a", encoding="utf-8") as file1:
                    file1.write(book_name+','+ book_author+ ','+book_kind+','+'\n')    
                file1.close()            
    file.close()


while True:
    process = input('1- Data input \n2- Read Data \n3- Exit\n')

    if process == '1':
        input_data()
    elif process == '2':
        read_data()
    else:
        break