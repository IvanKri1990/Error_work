class OpenFiles:
    def __init__(self, file_name_list=None, encoding='utf-8'):
        self.file_name_list = file_name_list
        self.encoding = encoding
        self.file_data_list = []

    def open_files(self):
        if self.file_name_list is None:
            print('Ошибка! Список файлов не передан')
        elif len(self.file_name_list) <= 0:
            return print('Ошибка! Список файлов пуст')
        else:
            for file in self.file_name_list:
                try:
                    with open(file, 'r', encoding=self.encoding) as f:
                        data = f.read().split('\n')
                        self.file_data_list.append(data)
                except FileNotFoundError:
                    print(f'Ошибка! Не удалось открыть следующий файл: {file}')
        return self.file_data_list


class TextInfo(OpenFiles):
    def __init__(self, file_name_list=None, encoding='utf-8'):
        super().__init__(file_name_list, encoding)
        self.files_data = self.open_files()
        self.files_dict = {}
        self.files_dict_sorted = {}

    def get_files_dict(self):
        for idx, val in enumerate(self.file_name_list):
            self.files_dict[val] = {'len_text': len(self.files_data[idx]),
                                    'text': self.files_data[idx]}
        return self.files_dict

    def sort_dict(self):
        self.len_text_list = [self.get_files_dict()[k]['len_text'] for k in self.get_files_dict().keys()]
        for l in sorted(list(set(self.len_text_list))):
            for f in self.file_name_list:
                if self.get_files_dict()[f]['len_text'] == l:
                    self.files_dict_sorted[f] = self.get_files_dict()[f]
                    for k in self.get_files_dict()[f]:
                        self.files_dict_sorted[f][k] = self.get_files_dict()[f][k]
        return self.files_dict_sorted

    def print_info(self):
        for k, v in self.sort_dict().items():
            print(k)
            for v2 in v.values():
                if type(v2) == int:
                    print(f"{v2}")
                else:
                    for s in v2:
                        print(s.strip())



TextInfo(['filehw1.txt', 'filehw2.txt', 'filehw3.txt']).print_info()
