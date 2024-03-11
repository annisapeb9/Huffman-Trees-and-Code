#create by_ANNISA PERMATA BUNDA_22343037
import heapq 

class Node: 
	def __init__(self, freq, symbol, left=None, right=None): 
		# frekuensi simbol 
		self.freq = freq 

		# nama simbol (karakter) 
		self.symbol = symbol 

		# node kiri dari node saat ini 
		self.left = left 

		# node kanan dari node saat ini 
		self.right = right 

		# arah pohon (0/1) 
		self.huff = '' 

	def __lt__(self, nxt): 
		return self.freq < nxt.freq 

# fungsi utilitas untuk mencetak kode huffman 
# untuk semua simbol dalam pohon Huffman yang baru dibuat 
def cetakNode(node, val=''): 

	# kode huffman untuk node saat ini 
	newVal = val + str(node.huff) 

	# jika node bukan node tepi 
	# maka traverse di dalamnya 
	if(node.left): 
		cetakNode(node.left, newVal) 
	if(node.right): 
		cetakNode(node.right, newVal) 

		# jika node adalah node tepi maka 
		# tampilkan kode huffman-nya 
	if(not node.left and not node.right): 
		print(f"{node.symbol} -> {newVal}") 

# karakter untuk pohon huffman 
chars = ['a', 'b', 'c', 'd', 'e', 'f'] 

# frekuensi karakter 
freq = [5, 9, 12, 13, 16, 45] 

# daftar berisi node yang tidak digunakan 
nodes = [] 

# mengkonversi karakter dan frekuensi 
# menjadi node pohon huffman 
for x in range(len(chars)): 
	heapq.heappush(nodes, Node(freq[x], chars[x])) 

while len(nodes) > 1: 

	# mengurutkan semua node secara menaik 
	# berdasarkan frekuensinya 
	left = heapq.heappop(nodes) 
	right = heapq.heappop(nodes) 

	# memberikan nilai arah ke node-node ini 
	left.huff = 0
	right.huff = 1

	# menggabungkan 2 node terkecil untuk membuat 
	# node baru sebagai orang tua mereka 
	newNode = Node(left.freq+right.freq, left.symbol+right.symbol, left, right) 

	heapq.heappush(nodes, newNode) 

cetakNode(nodes[0])
