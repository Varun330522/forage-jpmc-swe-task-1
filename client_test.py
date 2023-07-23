import unittest
from client3 import getDataPoint,getRatio

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
      self.assertEqual(getDataPoint(quote), (quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'], (quote['top_bid']['price'] + quote['top_ask']['price'])/2))

  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
       self.assertEqual(getDataPoint(quote), (quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'], (quote['top_bid']['price'] + quote['top_ask']['price'])/2))


  """ ------------ Add more unit tests ------------ """
  def test_getRatio_PriceBIsZero(self):
    # When the price of stock A is zero, the ratio should be 0.
    price_a = 100.0
    price_b = 0.0
    ratio = getRatio(price_a, price_b)
    self.assertIsNone(ratio)

  def test_getRatio_PriceAIsZero(self):
        # When the price of stock A is zero, the ratio should be 0.
    price_a = 0.0
    price_b = 50.0
    ratio = getRatio(price_a, price_b)
    self.assertEqual(ratio, 0.0)

  def test_getRatio_PriceBAndABothAreZero(self):
        # When both prices of stock A and stock B are zero, the ratio should be None.
    price_a = 0.0
    price_b = 0.0
    ratio = getRatio(price_a, price_b)
    self.assertIsNone(ratio)

  def test_getRatio_NormalCase(self):
        # Test a normal case where both prices are non-zero.
    price_a = 200.0
    price_b = 150.0
    ratio = getRatio(price_a, price_b)
    self.assertEqual(ratio, price_a / price_b)



if __name__ == '__main__':
    unittest.main()
