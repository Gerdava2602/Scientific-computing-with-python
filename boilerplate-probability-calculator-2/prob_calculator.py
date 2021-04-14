import copy
import random
# Consider using the modules imported above.

class Hat:
  def __init__(self,  **kwargs):
    self.contents = list()
    for key, value in kwargs.items():
      for v in range(value):
        self.contents.append(key)
  
  def draw(self, number):
    balls = copy.deepcopy(self.contents)
    removed = list()
    for i in range(number):
      if len(self.contents) > 0:
        removed.append(self.contents.pop(random.randint(0, len(self.contents)-1)))
      else:
        self.contents = balls
        return
    return removed

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  m = 0
  for n in range(num_experiments):
    content = copy.deepcopy(hat)
    drew = content.draw(num_balls_drawn)
    if drew:
      expected = list()
      for key, value in expected_balls.items():
        for v in range(value):
          expected.append(key)
      
      if has_it(drew, expected):
        m +=1
  if m == 0:
    return 1
  return m/num_experiments

def has_it(drew, expected):
  ex = copy.deepcopy(expected)

  for d in drew:
    for e in ex:
      if d == e:
        ex.remove(e)
    if len(ex) == 0:
      return True
  return False