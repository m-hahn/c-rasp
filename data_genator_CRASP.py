from torch.utils.data import IterableDataset
import random
from copy import deepcopy


class customTokenizer(object):
   def __init__(self):
       self.bos_token_id = 0
       self.sep_token_id = 1
       self.eos_token_id = 2
       self.pad_token_id = 3
       self.vocab_size = 1000
   def __len__(self):
       return self.vocab_size

class UniqueReverseDataset(IterableDataset):
    def __init__(self, tokenizer: customTokenizer, length_range: tuple[int, int], max_test_length: int):
        super().__init__()
        self.tokenizer = tokenizer 
        self.range_min, self.range_max = length_range
        self.range_min = max(1, self.range_min)
        self.max_test_length = max_test_length
        assert len(tokenizer) - 4 >= max_test_length
        assert (max_test_length >= self.range_max) or (max_test_length == -1)    # the pos emb is initialized based on max_test_length

    def __iter__(self):
        while True:
            length = random.randint(self.range_min, self.range_max)     # length of string to be copied
            
            temp = random.sample(range(len(self.tokenizer)-4), length)
            instance = [self.tokenizer.bos_token_id]
            instance.extend(temp)
            instance.append(self.tokenizer.sep_token_id)
            instance.extend(temp[::-1])
            instance.append(self.tokenizer.eos_token_id)
            label = deepcopy(instance)





            # setting some tokens to [pad] will make the loss on these tokens (as pred targets) be ignored
            label[:length+2] = [self.tokenizer.pad_token_id,] * (length+2)   # bos + ... + sep 
           
            # positional 
            if self.max_test_length != -1:
                offset = random.randint(0, (self.max_test_length - length) * 2)
            else:
                offset = 0
            pos_ids = list(range(offset, len(instance)+offset))

            yield instance, pos_ids, label

print("Testing UniqueReverseDataset...")
data = UniqueReverseDataset(customTokenizer(), (1, 10), 20).__iter__()

for _ in range(10):
   print(next(data))

