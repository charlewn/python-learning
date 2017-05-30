def make_link(G, node1, node2):
	if node1 not in G:
		G[node1] = {} #g[0] = {}
	(G[node1])[node2] = 1 #(g[0])[0] = 1
	if node2 not in G: #1 not in g
		G[node2] = {} #g[1] = {}
	(G[node2])[node1] = 1 #(g[1])[0] = 1
	return G


a_ring = {}

n = 5

# Add in the edges
#0,1,2,3,4; 1%5 = 1, 2, 3, 4, 5
for i in range(n):
	make_link(a_ring, i, (i+1)%n)

#How many nodes?
print len(a_ring)

print sum([len(a_ring[node]) for node in a_ring.keys()])/2

print a_ring

#[name.upper() for name in udacity]
# f(n)<-ø(g(n)), is g(n)<-ø(f(n))
#{0: {1: 1, 4: 1}, 1: {0: 1, 2: 1}, 2: {1: 1, 3: 1}, 3: {2: 1, 4: 1}, 4: {0: 1, 3: 1}}