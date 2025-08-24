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

class AnBnDataset(IterableDataset):
    def __init__(self, tokenizer: customTokenizer, length_range: tuple[int, int], max_test_length: int):
        super().__init__()
        self.tokenizer = tokenizer 
        self.range_min, self.range_max = length_range
        self.range_min = max(1, self.range_min)
        self.max_test_length = max_test_length
        assert len(tokenizer) - 4 >= max_test_length
        assert (max_test_length >= self.range_max) or (max_test_length == -1)    # the pos emb is initialized based on max_test_length
        assert self.tokenizer.bos_token_id not in [5, 6, 7, 8]
        assert self.tokenizer.pad_token_id not in [5, 6, 7, 8]
        self.mapping = {("a",) : 5, ("b",) : 6, ("a", "b") : 7, ("$",) : 8}
    def __iter__(self):
        while True:
            length = random.randint(self.range_min, self.range_max)     
#            length = (length//2) + 1
            temp = random.sample(range(len(self.tokenizer)-4), length)
            instance = [self.tokenizer.bos_token_id]
            label = [("a",)]
            for _ in range(length//2):
              instance.append(("a",))
              label.append(("a", "b"))
            for i in range(length//2):
              instance.append(("b",))
              if i < length//2 - 1:
                label.append(("b",))
              else:
                label.append(("$",))
            instance = [self.mapping.get(x, x) for x in instance]
            label = [self.mapping.get(x, x) for x in label]
            instance.append(self.tokenizer.eos_token_id)
            label.append(self.tokenizer.pad_token_id)
           

            # positional 
            if self.max_test_length != -1:
                offset = random.randint(0, (self.max_test_length - length) * 2)
            else:
                offset = 0
            pos_ids = list(range(offset, len(instance)+offset))
            
            yield instance, pos_ids, label

class AnBnCnDataset(IterableDataset):
    def __init__(self, tokenizer: customTokenizer, length_range: tuple[int, int], max_test_length: int):
        super().__init__()
        self.tokenizer = tokenizer 
        self.range_min, self.range_max = length_range
        self.range_min = max(1, self.range_min)
        self.max_test_length = max_test_length
        assert len(tokenizer) - 4 >= max_test_length
        assert (max_test_length >= self.range_max) or (max_test_length == -1)    # the pos emb is initialized based on max_test_length
        self.mapping = {("a",) : 5, ("b",) : 6, ("a", "b") : 7, ("$",) : 8, ("c",) : 9, self.tokenizer.bos_token_id : self.tokenizer.bos_token_id}
    def __iter__(self):
        while True:
            length = random.randint(self.range_min, self.range_max)   
#            length = (length//2) + 1
            temp = random.sample(range(len(self.tokenizer)-4), length)
            instance = [self.tokenizer.bos_token_id]
            label = [("a",)]
            for _ in range(length//3):
              instance.append(("a",))
              label.append(("a", "b"))
            for i in range(length//3):
              instance.append(("b",))
              if i < (length//3) - 1:
                label.append(("b",))
              else:
                label.append(("c",))
            for i in range(length//3):
              instance.append(("c",))
              if i < (length//3) - 1:
                label.append(("c",))
              else:
                label.append(("$",))
            print(instance, "\t", label)
            instance = [self.mapping[x] for x in instance]
            label = [self.mapping[x] for x in label]
#            print(instance, label)
            instance.append(self.tokenizer.eos_token_id)
            label.append(self.tokenizer.pad_token_id)
           

            # positional 
            if self.max_test_length != -1:
                offset = random.randint(0, (self.max_test_length - length) * 2)
            else:
                offset = 0
            pos_ids = list(range(offset, len(instance)+offset))
            
            yield instance, pos_ids, label


class Dyck1Dataset(IterableDataset):
    def __init__(self, tokenizer: customTokenizer, length_range: tuple[int, int], max_test_length: int):
        super().__init__()
        self.tokenizer = tokenizer 
        self.range_min, self.range_max = length_range
        self.range_min = max(1, self.range_min)
        self.max_test_length = max_test_length
        assert len(tokenizer) - 4 >= max_test_length
        assert (max_test_length >= self.range_max) or (max_test_length == -1)    # the pos emb is initialized based on max_test_length
        assert self.tokenizer.bos_token_id not in [5, 6, 7, 8]
        assert self.tokenizer.pad_token_id not in [5, 6, 7, 8]
        self.mapping = {("a",) : 5, ("b",) : 6, ("a", "b") : 7, ("a", "$",) : 8, self.tokenizer.bos_token_id : self.tokenizer.bos_token_id}
    def __iter__(self):
        while True:
            length = random.randint(self.range_min, self.range_max)     
#            length = (length//2) + 1
            temp = random.sample(range(len(self.tokenizer)-4), length)
            instance = [self.tokenizer.bos_token_id]
            label = [("a","$")]
            balance = 0
            for _ in range(length):
              instance.append(("a" if random.random() > 0.5 or balance < 1 else "b",))
              balance += 1 if instance[-1][0] == "a" else -1
              label.append((("a", "$") if balance == 0 else ("a", "b")))
            print(instance, "\t", label)
            instance = [self.mapping.get(x, x) for x in instance]
            label = [self.mapping.get(x, x) for x in label]
            instance.append(self.tokenizer.eos_token_id)
            label.append(self.tokenizer.pad_token_id)
           

            # positional 
            if self.max_test_length != -1:
                offset = random.randint(0, (self.max_test_length - length) * 2)
            else:
                offset = 0
            pos_ids = list(range(offset, len(instance)+offset))
            
            yield instance, pos_ids, label


class MajorityDataset(IterableDataset):
    def __init__(self, tokenizer: customTokenizer, length_range: tuple[int, int], max_test_length: int):
        super().__init__()
        self.tokenizer = tokenizer 
        self.range_min, self.range_max = length_range
        self.range_min = max(1, self.range_min)
        self.max_test_length = max_test_length
        assert len(tokenizer) - 4 >= max_test_length
        assert (max_test_length >= self.range_max) or (max_test_length == -1)    # the pos emb is initialized based on max_test_length
        assert self.tokenizer.bos_token_id not in [5, 6, 7, 8]
        assert self.tokenizer.pad_token_id not in [5, 6, 7, 8]
        self.mapping = {("a",) : 5, ("b",) : 6, ("a", "b") : 7, ("a", "$",) : 8, self.tokenizer.bos_token_id : self.tokenizer.bos_token_id}
    def __iter__(self):
        while True:
            length = random.randint(self.range_min, self.range_max)     
#            length = (length//2) + 1
            temp = random.sample(range(len(self.tokenizer)-4), length)
            instance = [self.tokenizer.bos_token_id]
            label = [("a","$")]
            balance = 0
            for _ in range(length):
              instance.append(("a" if random.random() > 0.5 else "b",))
              balance += 1 if instance[-1][0] == "a" else -1
              label.append((("a", "b", "$") if balance > 0 else ("a", "b")))
            print(instance, "\t", label)
            instance = [self.mapping.get(x, x) for x in instance]
            label = [self.mapping.get(x, x) for x in label]
            instance.append(self.tokenizer.eos_token_id)
            label.append(self.tokenizer.pad_token_id)
           

            # positional 
            if self.max_test_length != -1:
                offset = random.randint(0, (self.max_test_length - length) * 2)
            else:
                offset = 0
            pos_ids = list(range(offset, len(instance)+offset))
            
            yield instance, pos_ids, label

class MajorityLanguage(RegLanguage):

    def __init__(self) -> None:
        super().__init__()
        self.sigma = ["a", "b"]

    def belongs_to_lang(self, seq):
        balance = sum([1 if x == "a" else -1])
        return balance > 0

    def generate_pos_sample(self, min_length: int, max_length: int) -> str:
        while True:
           generated  = ["a" if random.random() > 0.5 else "b" for _ in range(random.randint(min_length, max_length))]
           if self.belongs_to_lang(generated):
              return "".join(generated)
    
    def is_valid_length(self, length):
        return (length >= 0)

data = MajorityDataset(customTokenizer(), (1, 10), 20).__iter__()

for _ in range(10):
   (next(data))

