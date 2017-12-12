import unittest

class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

  def append(self, val):
    current = self
    while current.next != None:
      current = current.next
    current.next = Node(val)
    return self

  def find(self, sought_val):
    current = self
    while current.next != None:
      if current.val == sought_val:
        return True
      current = current.next

    return current.val == sought_val


class NodeTest(unittest.TestCase):
  def setUp(self):
    self.root = Node(123)

  def test_node_attrs(self):
    self.assertEqual(self.root.val, 123)
    self.assertEqual(self.root.next, None)

  def test_append(self):
    self.assertEqual(self.root.append(7), self.root)
    self.assertEqual(self.root.next.val, 7)

    self.assertEqual(self.root.append(10), self.root)
    self.assertEqual(self.root.next.next.val, 10)

  def test_find(self):
    self.root = Node(0)
    self.assertTrue(self.root.find(0))

    vals = [89,12,3,1]
    for val in vals:
      self.root.append(val)

    for val in vals:
      self.assertTrue(self.root.find(val))

    self.assertFalse(self.root.find(123455))




if __name__ == '__main__':
  unittest.main()
