import time
#This class represents a directed graph using adjacency matrix representation 
class Graph: 
	def __init__(self,graph): 
		self.graph = graph # residual graph 
		self. ROW = len(graph) 
		#self.COL = len(gr[0]) 
	'''Returns true if there is a path from source 's' to sink 't' in 
	residual graph. Also fills parent[] to store the path '''
	def BFS(self,s, t, parent): 
		# Mark all the vertices as not visited 
		visited =[False]*(self.ROW) 		
		# Create a queue for BFS 
		queue=[] 		
		# Mark the source node as visited and enqueue it 
		queue.append(s) 
		visited[s] = True		
		while queue: 
			#Dequeue a vertex from queue and print it 
			u = queue.pop(0) 		
			# Get all adjacent vertices of the dequeued vertex u 
			# If a adjacent has not been visited, then mark it 
			# visited and enqueue it 
			for ind, val in enumerate(self.graph[u]): 
				if visited[ind] == False and val > 0 : 
					queue.append(ind) 
					visited[ind] = True
					parent[ind] = u 
		# If we reached sink in BFS starting from source, then return 
		# true, else false
		#print(visited) 
		return True if visited[t] else False	
	# Returns tne maximum flow from s to t in the given graph 
	def FordFulkerson(self, source, sink): 
		#print("Surce:" + str(source) + "sink:" + str(sink) )
		# This array is filled by BFS and to store path 
		parent = [-1]*(self.ROW) 

		max_flow = 0 # There is no flow initially 

		# Augment the flow while there is path from source to sink 
		while self.BFS(source, sink, parent) : 

			# Find minimum residual capacity of the edges along the 
			# path filled by BFS. Or we can say find the maximum flow 
			# through the path found. 
            
			path_flow = float("Inf")
             
			s = sink 
			while(s != source): 
				path_flow = min (path_flow, self.graph[parent[s]][s]) 
				s = parent[s] 
			#print(max_flow)
			# Add path flow to overall flow 
			max_flow += path_flow 

			# update residual capacities of the edges and reverse edges 
			# along the path 
			v = sink 
			while(v != source): 
				u = parent[v] 
				self.graph[u][v] -= path_flow 
				self.graph[v][u] += path_flow 
				v = parent[v]
				#print(v , u)
				#print(u) 

		return max_flow 


# Create a graph given in the above diagram 

graph =		[[0, 1000, 0  , 500,0  , 0   ], 
		[ 0, 0  , 550 , 250 ,0  , 0   ], 
		[ 0, 0  , 0  , 0  ,250 , 650  ], 
		[ 0, 0  , 200 , 0  ,350 , 0   ], 
		[ 0, 0  , 0  , 0   ,0 , 500  ], 
		[ 0, 0  , 0  , 0  , 0 , 0   ]] 

g = Graph(graph) 

source = 0; sink = 4
print("\n")
print("For the given graph:")
for i in range(0,6):
	print(graph[i])
start = time.time()
print ("The maximum possible flow is %d " % g.FordFulkerson(source, sink)) 
end = time.time() - start
print(end)

