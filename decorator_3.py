from datetime import datetime

# декоратор-логгер
def logger(old_function):
    def new_function(*args, **kwargs):
        time = datetime.now()
        somedate = time.strftime('%d.%m.%Y %H:%M')
        result = old_function(*args, **kwargs)
        exit_data = (
            f'Функция вызвана: {somedate}\n'
            f'Название функции: {old_function.__name__}\n'
            f'Аргументы функции: {args} и {kwargs}\n'
            f'Результат: {result}\n'
            f'\n'
        )

        with open('logger_main.log', 'a', encoding='utf-8') as f:
            f.write(exit_data)                
        return result
    return new_function



class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list
    
    @logger
    def __iter__(self):
        self.main_cursor = 0
        self.inside_main_cursor = 0
        return self
    
    @logger
    def __next__(self):
        while self.main_cursor < len(self.list_of_list):
            if self.inside_main_cursor >= len(self.list_of_list[self.main_cursor]):
                self.main_cursor += 1
                self.inside_main_cursor = 0
                continue
            item = self.list_of_list[self.main_cursor][self.inside_main_cursor]
            self.inside_main_cursor += 1
            return item
        raise StopIteration
    

list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

iterator = FlatIterator(list_of_lists_1)
for item in iterator:
    pass

if __name__ == '__main__':
    print(f'Информация записана в файл: logger_main.log')