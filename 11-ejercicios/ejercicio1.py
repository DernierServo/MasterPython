from random import randint

def show_list(ls):
    print('*'*20 + '| List |' +'*'*20)
    for l in ls:
        print(l)
    print('\n')


def ds_fun_p4(ls):
    
    while True:
        num_found = int(input('Please, insert a number: '))
        if num_found in ls:
            return f'The Number \'{num_found}\' was found, with position {ls.index(num_found)}!'
        else:
            print('Not Found!')


def ds_fun():
    # Parte 1
    ls = [randint(1,100) for x in range(10)]
    show_list(ls)

    # Parte 2
    show_list(sorted(ls))  

    # Parte 3
    print(f'Longitud: {len(ls)}')

    # Parte 4
    print(ds_fun_p4(ls))


def main():
    ds_fun()


if __name__ == '__main__':
    main()

