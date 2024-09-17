def main():
    book_path ="books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    letter_count=count_of_letter(text)
    REPORT=report(text)
    
    print(REPORT)
    
    
def get_num_words(text):
    words=text.split()
    return len(words)

def get_book_text(path):

    with open(path) as f:
         return f.read()

def count_of_letter(text):
    hashy={}
    for c in text:
        lowered=c.lower()
        if lowered in hashy:
            hashy[lowered]+=1
        else:
            hashy[lowered]=1
    return hashy



def sort_on(dict):
    return dict["num"]



def report(text):
    L=[]
    Number=get_num_words(text)
    D=count_of_letter(text)
    print('--- Begin report of books/frankenstein.txt---')
    print(f"{Number} words found in the document"+'\n')
    
    for char,count in D.items():
        if char.isalpha():
            L.append({'char':char,'num':count})
    
    L.sort(reverse=True, key=sort_on)
    
    for i in L:
        print(f"The '{i['char']}' character was gound {i['num']} times")
   
    print("--- End report ---")






main()
