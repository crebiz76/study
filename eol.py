data = []

def input_eol():
    code = input("Input the value = ")
    data = code.split(' ')
    return data
    
def output_eol(data):
    for i in data:        
        print("" )
    

def print_menu():
    # print("------------------------------")
    # print(" Dec 값을 아래와 같이 입력하세요. ")
    # print(" ex) 12 34 56 78              ")
    # print("------------------------------")
    print("=============================")
    print("-----------------------------")
    print(" 1) Dec                      ")
    print(" 2) Hex                      ")
    print(" 3) Bin                      ")
    print(" 4) Terminate                ")
    print("-----------------------------")
    menu = input(" Select Menu: ")
    print("=============================")
    return int(menu)

def run():
    while 1:
        menu = print_menu()
        #
        if menu == 4:
            break
        #
        output_eol(input_eol())

if __name__ == "__main__":
    run()
