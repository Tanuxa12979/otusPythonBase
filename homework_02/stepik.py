# Проблема с late binding

if __name__ == '__main__':
    from functools import partial


    def pretty_print(text, symbol, count):
        print(symbol * count)
        print(text)
       # print(symbol * count)


    star_pretty_print = partial(pretty_print, 'Hi!!!', symbol='*')

    star_pretty_print(count=7)

    #print(star_pretty_print.args)
   ## print(star_pretty_print.keywords)

    star_pretty_print.func('Исходная функция', symbol='~', count=20)