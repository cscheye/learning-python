import unittest
import argparse

parser = argparse.ArgumentParser(description='captcha sum of same-subsequent digits')
parser.add_argument('-c', '--captcha', help='sequence of digits')
parser.add_argument('-t', '--test', help='run tests')

class Captcha(object):
  def solve(self, sequence):
    count = 0
    for i in range(len(sequence) - 1):
      if sequence[i] == sequence[i+1]:
        count += int(sequence[i])

    if sequence[-1] == sequence[0]:
      count += int(sequence[0])

    return count


class CaptchaTest(unittest.TestCase):
  def setUp(self):
    self.captcha = Captcha()

  def test_solve(self):
    test_cases = [
      ['1122', 3],
      ['1111', 4],
      ['1234', 0],
      ['91212129', 9],
    ]

    for test_case in test_cases:
      sequence, captcha_sum = test_case
      self.assertEqual(self.captcha.solve(sequence), captcha_sum)


if __name__ == '__main__':
  # unittest.main()
  args = parser.parse_args()
  if args.test:
    print 'test'
  elif args.captcha:
    captcha = Captcha()
    print captcha.solve(args.captcha)
  else:
    parser.print_help()

