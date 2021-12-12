test_inp = [
    '3',
    'Job 1 50',
    'SomeJob 2 50',
    'AnotherJob 1 100',
    '2',
    'SomeJob 3 50',
    'OtherJob 2 50',
    '2',
    'SomeJob 2 60',
    'OtherJob 2 50',
    '2',
    'SomeJob 2 50',
    'OtherJob 2 50',
    '5',
    'q 3 20',
    'a 1 20',
    'y 4 50',
    'b 2 56',
    'w 1 40',
    '6',
    'a 2 34',
    'b 8 9',
    'd 1 10',
    'j 3 20',
    'p 1 10',
    'v 10 10',
    '3',
    'a 1 50',
    'b 1 50',
    'c 1 50',
    '4',
    'a 2 200',
    'b 3 200',
    'c 1 150',
    'd 2 300',
    '4',
    'a 3 300',
    'b 3 300',
    'c 3 301',
    'd 3 400',
    '5',
    'a 3 50',
    'b 2 40',
    'c 3 60',
    'd 6 30',
    'e 5 20',
    '6',
    'a 3 150',
    'b 2 100',
    'c 3 150',
    'd 1 100',
    'e 2 150',
    'f 3 200',
    '6',
    'a 3 150',
    'b 2 100',
    'c 1 150',
    'd 2 150',
    'e 3 150',
    'f 3 200',
    '6',
    'a 3 150',
    'b 2 100',
    'c 3 150',
    'd 1 180',
    'e 2 150',
    'f 3 200',
    '6',
    'a 3 150',
    'b 2 100',
    'c 3 150',
    'd 1 150',
    'e 2 180',
    'f 3 200',
    '3',
    'k 3 150',
    'f 1 100',
    'u 3 200',
    '4',
    'a 1 10',
    'b 2 10',
    'c 2 10',
    'd 3 10',
    '3',
    'a 1 10',
    'b 2 15',
    'c 2 20',
    '3',
    'a 2 10',
    'b 1 10',
    'c 2 20',
    "1",
    "a 1 10",
    "1",
    "a 15 10"
]
test_out = [
    ['AnotherJob SomeJob'],
    ['OtherJob SomeJob'],
    ['SomeJob OtherJob'],
    ['SomeJob OtherJob'],
    ['w b q y'],
    ['d a j v b', 'p a j v b'],
    ['a', 'b', 'c'],
    ['d a b'],
    ['d c a', 'd c b'],
    ['c b a d e'],
    ['f a c', 'f e a', 'f e c'],
    ['f e a', 'f c a', 'f d a', 'f e d', 'f d c', 'f a e'],
    ['f d a', 'f d c', 'f d e'],
    ['f e d', 'f e a', 'f e c'],
    ['k f u'],
    ['a b d', 'a c d', 'b c d'],
    ['b c'],
    ['b c', 'a c'],
    ["a"],
    ["a"],
]