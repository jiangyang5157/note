import unittest
from linked_list import *

class TestItem(unittest.TestCase):

    def setUp(self):
        self.n0 = LinkedListNode(0)
        self.empty_list = LinkedList()

        self.l1 = LinkedList()
        self.l1.insert_in_front(1)

        self.l2 = LinkedList()
        self.l2.insert_in_front(2)
        self.l2.insert_in_front(1)

        self.l3 = LinkedList()
        self.l3.insert_in_front(3)
        self.l3.insert_in_front(2)
        self.l3.insert_in_front(1)

        self.l99 = LinkedList()
        for i in range(99, 0, -1):
            self.l99.insert_in_front(i)

    def test_list_node(self):
        self.assertEqual(self.n0.data, 0)

    def test_empty_list_is_empty(self):
        self.assertEqual(self.empty_list.is_empty(), True)
        self.assertEqual(len(self.empty_list), 0)

    def test_is_not_empty(self):
        self.assertEqual(self.l1.is_empty(), False)
        self.assertEqual(len(self.l1), 1)

        self.assertEqual(self.l2.is_empty(), False)
        self.assertEqual(len(self.l2), 2)

        self.assertEqual(self.l3.is_empty(), False)
        self.assertEqual(len(self.l3), 3)

        self.assertEqual(self.l99.is_empty(), False)
        self.assertEqual(len(self.l99), 99)

    def test_str(self):
        self.assertEqual(str(self.empty_list), "[]")
        self.assertEqual(str(self.l1), "[1]")
        self.assertEqual(str(self.l2), "[1 -> 2]")
        self.assertEqual(str(self.l3), "[1 -> 2 -> 3]")
        self.assertEqual(str(self.l99), "[1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9 -> 10 -> 11 -> 12 -> 13 -> 14 -> 15 -> 16 -> 17 -> 18 -> 19 -> 20 -> 21 -> 22 -> 23 -> 24 -> 25 -> 26 -> 27 -> 28 -> 29 -> 30 -> 31 -> 32 -> 33 -> 34 -> 35 -> 36 -> 37 -> 38 -> 39 -> 40 -> 41 -> 42 -> 43 -> 44 -> 45 -> 46 -> 47 -> 48 -> 49 -> 50 -> 51 -> 52 -> 53 -> 54 -> 55 -> 56 -> 57 -> 58 -> 59 -> 60 -> 61 -> 62 -> 63 -> 64 -> 65 -> 66 -> 67 -> 68 -> 69 -> 70 -> 71 -> 72 -> 73 -> 74 -> 75 -> 76 -> 77 -> 78 -> 79 -> 80 -> 81 -> 82 -> 83 -> 84 -> 85 -> 86 -> 87 -> 88 -> 89 -> 90 -> 91 -> 92 -> 93 -> 94 -> 95 -> 96 -> 97 -> 98 -> 99]")

    def test_len(self):
        self.assertEqual(len(self.empty_list), 0)
        self.assertEqual(len(self.l1), 1)
        self.assertEqual(len(self.l2), 2)
        self.assertEqual(len(self.l3), 3)
        self.assertEqual(len(self.l99), 99)

    def test_for_loop(self):
        for (i, node) in enumerate(self.l3):
            self.assertEqual(node.data, i + 1)

    def test_insert_in_front(self):
        self.empty_list.insert_in_front(1)
        self.assertEqual(str(self.empty_list), '[1]')
        self.assertEqual(len(self.empty_list), 1)

        self.l1.insert_in_front(0)
        self.l1.insert_in_front(0)
        self.l1.insert_in_front(0)
        self.l1.insert_in_front(0)

        self.assertEqual(str(self.l1), '[0 -> 0 -> 0 -> 0 -> 1]')
        self.assertEqual(len(self.l1), 5)

    def test_remove_from_front(self):
        self.assertFalse(self.empty_list.remove_from_front())
        self.assertEqual(len(self.empty_list), 0)

        self.l1.remove_from_front()
        self.assertEqual(str(self.l1), '[]')
        self.assertEqual(len(self.l1), 0)

        self.l2.remove_from_front()
        self.assertEqual(str(self.l2), '[2]')
        self.assertEqual(len(self.l2), 1)

        self.l3.remove_from_front()
        self.assertEqual(str(self.l3), '[2 -> 3]')
        self.assertEqual(len(self.l3), 2)

    def test_insert_at_end(self):
        self.empty_list.insert_at_end(999)
        self.assertEqual(str(self.empty_list), '[999]')
        self.assertEqual(len(self.empty_list), 1)

        self.l1.insert_at_end(999)
        self.assertEqual(str(self.l1), '[1 -> 999]')
        self.assertEqual(len(self.l1), 2)

        self.l2.insert_at_end(999)
        self.assertEqual(str(self.l2), '[1 -> 2 -> 999]')
        self.assertEqual(len(self.l2), 3)

        self.l3.insert_at_end(999)
        self.assertEqual(str(self.l3), '[1 -> 2 -> 3 -> 999]')
        self.assertEqual(len(self.l3), 4)

    def test_remove_from_last(self):
        empty_list_result = self.empty_list.remove_from_last()
        self.assertFalse(empty_list_result)
        self.assertEqual(len(self.empty_list), 0)

        self.l1.remove_from_last()
        self.assertEqual(str(self.l1), '[]')
        self.assertEqual(len(self.l1), 0)

        self.l2.remove_from_last()
        self.assertEqual(str(self.l2), '[1]')
        self.assertEqual(len(self.l2), 1)

        self.l3.remove_from_last()
        self.assertEqual(str(self.l3), '[1 -> 2]')
        self.assertEqual(len(self.l3), 2)

    def test_insert_at_index_default(self):
        self.empty_list.insert_at_index(22)
        self.assertEqual(str(self.empty_list), '[22]')
        self.assertEqual(len(self.empty_list), 1)

    def test_insert_at_index_0(self):
        self.empty_list.insert_at_index(22, 0)
        self.assertEqual(str(self.empty_list), '[22]')
        self.assertEqual(len(self.empty_list), 1)

        self.l1.insert_at_index(22, 0)
        self.assertEqual(str(self.l1), '[22 -> 1]')
        self.assertEqual(len(self.l1), 2)

        self.l3.insert_at_index(22, 0)
        self.assertEqual(str(self.l3), '[22 -> 1 -> 2 -> 3]')
        self.assertEqual(len(self.l3), 4)

    def test_insert_at_index_1(self):
        self.l1.insert_at_index(22, 1)
        self.assertEqual(str(self.l1), '[1 -> 22]')
        self.assertEqual(len(self.l1), 2)

        self.l3.insert_at_index(22, 1)
        self.assertEqual(str(self.l3), '[1 -> 22 -> 2 -> 3]')
        self.assertEqual(len(self.l3), 4)

    def test_insert_at_index_2(self):
        self.l3.insert_at_index(22, 2)
        self.assertEqual(str(self.l3), '[1 -> 2 -> 22 -> 3]')
        self.assertEqual(len(self.l3), 4)

    def test_insert_at_index_3(self):
        self.l3.insert_at_index(22, 3)
        self.assertEqual(str(self.l3), '[1 -> 2 -> 3 -> 22]')
        self.assertEqual(len(self.l3), 4)

    def test_remove_at_index_default(self):
        empty_list_result = self.empty_list.remove_at_index()
        self.assertFalse(empty_list_result)

    def test_remove_at_index_0(self):
        self.l1.remove_at_index(0)
        self.assertEqual(str(self.l1), '[]')
        self.assertEqual(len(self.l1), 0)

        self.l3.remove_at_index(0)
        self.assertEqual(str(self.l3), '[2 -> 3]')
        self.assertEqual(len(self.l3), 2)

    def test_remove_at_index_1(self):
        self.l3.remove_at_index(1)
        self.assertEqual(str(self.l3), '[1 -> 3]')
        self.assertEqual(len(self.l3), 2)

    def test_remove_at_index_2(self):
        self.l3.remove_at_index(2)
        self.assertEqual(str(self.l3), '[1 -> 2]')
        self.assertEqual(len(self.l3), 2)

unittest.main()
