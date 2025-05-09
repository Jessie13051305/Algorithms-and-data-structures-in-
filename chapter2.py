#2.1 Google Map, Microsoft, Gmail
#2.2 Facebook
#2.3 Notepad doesn't show some function like: get_text(), revise_text() and so on.
#2.4
class Flower:
  def __init__(self, name = "Unknow", petal = 0, price = 0):
    """ Initialize a Flower instance"""

    """ Check type and through raise if the input doesn't expect"""
    if not isinstance(name, str):
      raise TypeError("Name must be a string")
    if not isinstance(petal, int) or petal < 0:
      raise TypeError("Petal must be a positive")
    if not isinstance(price, float) or price < 0:
      raise TypeError("Price must be a float")

    self._name = name
    self._petal = petal
    self._price = price

  def get_name(self):
    return self._name

  def get_petal(self):
    return self._petal

  def get_price(self):
    return self._price

if __name__ =='__main__':
  u = Flower('Roses', 12.5, 14 )
  print(u.get_name())

#2.5

