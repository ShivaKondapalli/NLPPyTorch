import torch
import torch.nn as nn
import Web_Scraper
import string
import unicodedata

#
# def unicodetoascii(s):
#     return ''.join(c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) != 'Mn' and c in all_letters)
#
#
all_letters = string.ascii_letters + " .,;'"
n_letters = len(all_letters)

# girls_list = Web_Scraper.get_data('https://www.verywellfamily.com/top-1000-baby-girl-names-2757832')
# boys_list = Web_Scraper.get_data('https://www.verywellfamily.com/top-1000-baby-boy-names-2757618')
#
# girls_list_ascii = [unicodetoascii(girl) for girl in girls_list]
# boys_list_ascii = [unicodetoascii(boy) for boy in boys_list]
#
#
# # sex to dictionary mapping
# sex_to_name = dict()
#
# sex_to_name['Girl'] = girls_list
# sex_to_name['Boy'] = boys_list


# n_categories = len(sex_to_name)


def lettertoindex(l):
    """converts letter to index"""
    return all_letters.index(l)


def nametotensor(name):
    """converts a name into a tensor of shape seq, 1, len(all_letters)"""
    tensor = torch.zeros(len(name), 1, len(all_letters))
    for idx, l in enumerate(name):
        tensor[idx][0][lettertoindex(l)] = 1
    return tensor


class LSTM(nn.Module):

    def __init__(self, input_size, hidden_size, output_size, num_layers=1):

        super(LSTM, self).__init__()

        self.hidden_size = hidden_size
        self.num_layers = num_layers

        self.lstm = nn.LSTM(input_size=input_size, hidden_size=hidden_size, num_layers=num_layers)
        self.fc = nn.Linear(hidden_size, output_size)

    def forward(self, x):
        batch_size = x.size(1)

        hidden = self.init_hidden(batch_size)
        cell = self.cell_state(batch_size)

        output, hidden = self.lstm(x, (hidden, cell))

        last_output = output[-1]  # batch_size * hidden_size

        fc_out = self.fc(last_output)  # 1 * hidden_size

        return fc_out

    def init_hidden(self, batch_size):
        return torch.zeros(self.num_layers, batch_size, self.hidden_size)

    def cell_state(self, batch_size):
        return torch.zeros(self.num_layers, batch_size, self.hidden_size)


def main():
    n_hidden = 128
    n_categories = 2
    lstm = LSTM(n_letters, n_hidden, n_categories, num_layers=2)
    print(lstm)

    name = nametotensor('Albert')
    print(name)
    print(name.size())

    fcout = lstm.forward(name)
    print(fcout)
    print(fcout.size())


if __name__ == '__main__':
    main()

