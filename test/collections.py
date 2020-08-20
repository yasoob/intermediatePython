import unittest,json
from  collections import defaultdict,OrderedDict,Counter,deque,namedtuple
from collections.abc import Iterable
from enum import Enum
class TDD_COLLECTIONS(unittest.TestCase):
    def test_collections(self):
        colours = (
            ('Yasoob', 'Yellow'),
            ('Ali', 'Blue'),
            ('Arham', 'Green'),
            ('Ali', 'Black'),
            ('Yasoob', 'Red'),
            ('Ahmed', 'Silver'),
        )
        favourite_colours = defaultdict(list)
        for name, colour in colours:
            favourite_colours[name].append(colour)
        self.assertIsInstance(favourite_colours, defaultdict)
        self.assertIsInstance(favourite_colours, dict)
        self.assertEqual(favourite_colours['Yasoob'],['Yellow','Red'])
        self.assertEqual(favourite_colours['Ahmed'],['Silver'])
    def test_keyerror_solution(self):
        some_dict = {}
        self.assertRaises(KeyError,lambda:some_dict['colours']['favourite'] )
        tree = lambda: defaultdict(tree)
        some_dict = tree()
        some_dict['colours']['favourite'] = "yellow"
        self.assertEqual(json.dumps(some_dict),'{"colours": {"favourite": "yellow"}}')
    def test_OrderedDict(self):
        l=[("Red", 198),( "Green", 170),( "Blue", 160)]
        colours = OrderedDict(l)
        l1=[]
        for key, value in colours.items():
            l1.append((key, value))
        self.assertEqual(l1,l)
    def test_Counter(self):
        colours = (
            ('Yasoob', 'Yellow'),
            ('Ali', 'Blue'),
            ('Arham', 'Green'),
            ('Ali', 'Black'),
            ('Yasoob', 'Red'),
            ('Ahmed', 'Silver'),
        )
        favs = Counter(name for name, colour in colours)
        favs1 = Counter(name for  colour,name in colours)
        self.assertIsInstance(favs, Counter)
        self.assertIsInstance(favs, dict)
        self.assertEqual(favs,{'Yasoob':2,'Ali':2,'Arham':1,'Ahmed':1})
        self.assertEqual(favs1,{'Yellow': 1, 'Blue': 1, 'Green': 1, 'Black': 1, 'Red': 1, 'Silver': 1})
        line_count=[]
        with open('test/ternary_operators.py', 'rb') as f:
            line_count .append( Counter(f))
        self.assertIsInstance(line_count[0],dict)
    def test_deque(self):
        d = deque()
        d.append('1')
        d.append('2')
        d.append('3')
        self.assertIsInstance(d,deque)
        self.assertEqual(d,deque(['1','2','3']))
        self.assertEqual(len(d),3)
        self.assertEqual(d[0],'1')
        self.assertEqual(d[-1], '3')
        d = deque(range(5))
        self.assertEqual(len(d),5)
        self.assertEqual(d.popleft(),0)
        self.assertEqual(d.pop(),4)
        self.assertEqual(d, deque([1, 2, 3]))
        d = deque([0, 1, 2, 3, 5], maxlen=5)
        self.assertEqual(len(d),5)
        d.extend([6])
        self.assertEqual(len(d), 5)
        self.assertIsNone(d.append(4))
        self.assertEqual(len(d), 5)
        d = deque([1,2,3,4,5])
        d.extendleft([0])
        d.extend([6,7,8])
        self.assertEqual(d,deque([0,1,2,3,4,5,6,7,8]))
    def test_namedtuple(self):
        man = ('Ali', 30)
        self.assertEqual(man[0],'Ali')
        Animal = namedtuple('Animal', 'name age type')
        perry = Animal(name="perry", age=31, type="cat")
        self.assertIsInstance(perry,Animal)
        self.assertIsInstance(perry,tuple)
        self.assertEqual(perry.name,'perry')
        Animal = namedtuple('Animal', 'name age type')
        perry = Animal(name="perry", age=31, type="cat")
        def setPerry():
            perry.age = 42
        self.assertRaises(AttributeError,setPerry)
        self.assertEqual(perry[0],'perry')
        self.assertIsInstance(perry._asdict(),dict)
        self.assertEqual(perry._asdict(), {'name': 'perry', 'age': 31, 'type': 'cat'})
    def test_Enum(self):
        class Species(Enum):
            cat = 1
            dog = 2
            horse = 3
            aardvark = 4
            butterfly = 5
            owl = 6
            platypus = 7
            dragon = 8
            unicorn = 9
            # But we don't really care about age, so we can use an alias.
            kitten = 1
            puppy = 2
        Animal = namedtuple('Animal', 'name age type')
        perry = Animal(name="Perry", age=31, type=Species.cat)
        drogon = Animal(name="Drogon", age=4, type=Species.dragon)
        tom = Animal(name="Tom", age=75, type=Species.cat)
        charlie = Animal(name="Charlie", age=2, type=Species.kitten)
        self.assertEqual(charlie.type, Species.cat)
        self.assertEqual(charlie.type, Species['cat'])
        self.assertEqual(charlie.type, Species(1))
        self.assertEqual(charlie.type, Species.kitten)
        self.assertEqual(charlie.type, tom.type)
    def test_iterable(self):
        m = map(lambda x: x, [])
        self.assertIsInstance(m,Iterable)
if __name__ == '__main__':
    unittest.main()
