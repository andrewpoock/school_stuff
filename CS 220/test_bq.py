# test_bq.py
#  Unit tests for a BoundedQueue implementation

import unittest

from bqueue import BoundedQueue


class TestBoundedQueue(unittest.TestCase):

    def test_initially_empty(self):
        q = BoundedQueue(50)
        self.assertAlmostEqual(q.size(), 0)

    def test_capacity(self):
        q = BoundedQueue(20)
        self.assertEqual(q.capacity(), 20)

        q = BoundedQueue(50)
        self.assertEqual(q.capacity(), 50)

    def test_enqueue_1(self):
        q = BoundedQueue(20)
        q.enqueue("One")
        self.assertEqual(q.size(), 1)
        self.assertEqual(q.front(), "One")

    def test_enqueue_several(self):
        q = BoundedQueue(50)
        for i in range(5):
            q.enqueue(i)
        self.assertEqual(q.size(), 5)
        self.assertEqual(q.front(), 0)

    def test_dequeue(self):
        q = BoundedQueue(50)
        for i in range(5):
            q.enqueue(i)
        for i in range(5):
            self.assertEqual(q.dequeue(), i)
            self.assertEqual(q.size(), 4-i)

    def test_wraps_around(self):
        q = BoundedQueue(7)
        for i in range(3):
            for i in range(5):
                q.enqueue(i)
            for i in range(5):
                self.assertEqual(q.dequeue(), i)
                self.assertEqual(q.size(), 4-i)

    def test_isfull(self):
        q = BoundedQueue(10)
        for i in range(10):
            self.assertFalse(q.isfull())
            q.enqueue("foo")
        self.assertTrue(q.isfull())

    def test_catches_overflow(self):
        q = BoundedQueue(10)
        for i in range(10):
            q.enqueue(i)
        with self.assertRaises(Exception) as context:
            q.enqueue(10)
        self.assertIn("Queue is full", str(context.exception))


if __name__ == "__main__":
    unittest.main()
