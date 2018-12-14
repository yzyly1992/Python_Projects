import math

def quadratic(a, b, c):
	if not isinstance(a and b and c, (int, float)):
		raise TypeError('bad operand typle')
	if a == 0:
		if b == 0:
			raise ValueError('equation has no meaning if a and b equals 0')
		else: x = - c / b
		return x

	else:
		x1 = (- b + math.sqrt(b * b - 4 * a * c)) / (2 * a)
		x2 = (- b - math.sqrt(b * b - 4 * a * c)) / (2 * a)
	
	return x1, x2

print('quadratic(2, 3, 1) =', quadratic(2, 3, 1))
print('quadratic(1, 3, -4) =', quadratic(1, 3, -4))
print(quadratic(0, 0, 0))

if quadratic(2, 3, 1) != (-0.5, -1.0):
    print('测试失败')
elif quadratic(1, 3, -4) != (1.0, -4.0):
    print('测试失败')
else:
    print('测试成功')