from lower import lower
from upper import upper
import Matrix
from Rational import Rational as R



A = Matrix.Matrix([[R(2),    R(3),   R(3), R(1)],
                  [R(-1),   R(1),   R(1), R(1)],
                  [R(-4),   R(-6),  R(3), R(2)],
                  [R(-2),   R(-1),  R(1), R(1)]])



llower = lower(A)

uupper = upper(A)


print("lower :\n", llower)
print("upper :\n", uupper)
print("lower * upper :\n", llower * uupper)
