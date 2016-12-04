class Vetor(object):
	
	def __init__(self, x, y, z):
		self.x = x
		self.y = y
		self.z = z

class Operacao(object):
	def __init__(self):
		pass
		
	@staticmethod
	def soma(u, v):
		return (u.x + v.x, u.y + v.y, u.z + v.z)

	@staticmethod
	def subtracao(u, v):
		return (u.x - v.x, u.y - v.y, u.z - v.z)

	@staticmethod
	def multiplicacao(valor, v):
		return (valor * v.x, valor * v.y, valor * v.z)

	@staticmethod
	def produtoEscalar(u, v):
		return (u.x * v.x + u.y * v.y + u.z * v.z)

	@staticmethod
	def saoParalelos(u, v):
		x = u.x/v.x
		y = u.y/v.y
		z = u.z/v.z

		if x == y and y == z :
			return True
		return False

teste = Vetor(2,3,4)
teste2 = Vetor(3,7,8)
print Operacao.soma(teste, teste2)