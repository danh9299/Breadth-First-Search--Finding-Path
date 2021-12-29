from queue import Queue
#Cây
graph = {
  'A' : ['B', 'C'],
  'B' : ['D','E'],
  'C' : ['F', 'G'],
  'D' : ['H', 'I'],
  'H' : ['K'],
  'E' : [],
  'F' : [],
  'G' : [],
  'K' : [],
  'I' : []
}

#Thuật toán t́m kiếm chiều rộng
def BFS(graph, start, end):
    #Tạo 1 set visit để lưu lại các nút đă được thăm
    visit = set()
    #Tạo 1 hàng đợi
    queue = Queue()

    #Đặt nút start vào hàng đợi và visit
    queue.put(start)
    visit.add(start)
    
    #Tạo thư viện để lưu nút cha của các nút được thăm
    parent = dict()
    #Nút bắt đầu xác định là không có nút cha (trong trường hợp đỉnh không phải nút cao nhất, đường đi không thể đi ngược lên)
    parent[start] = None

    #Thực hiện thuật toán
    path_found = False
    while not queue.empty():
        current_node = queue.get()
        if current_node == end:
            path_found = True
            break

        for next_node in graph[current_node]:
            if next_node not in visit:
                queue.put(next_node)
                parent[next_node] = current_node
                visit.add(next_node)
                
    #Hinh thành đường đi
    path = []
    if path_found:
        path.append(end)
        while parent[end] is not None:
            path.append(parent[end]) 
            end = parent[end]
        path.reverse()
    return path
#-------------------
#Phần main
#Người dùng nhập vào dữ liệu cho điểm bắt đầu và điểm kết thúc
start = (input("Nhập điểm bắt đầu: "))
start = start.upper()
while start not in graph:
    print("Điểm bắt đầu phải có trong cây!")
    start = input("Nhập lại điểm bắt đầu: ")
    start = start.upper()
end = input("Nhập điểm cần đến: ")
end = end.upper()
while end not in graph:
    print("Điểm đến phải có trong cây!")
    end = input("Nhập lại điểm cần đến: ")
    end = end.upper()
#Chạy thuật toán
path = BFS(graph, start, end)
#In ra đường đi
if path == []:
    print("Không tìm thấy đường đi",end="")
else:
    print("Đường đi:",end=" ")
    for x in path:
        if x == start:
            print(x,end="")
        else:
            print(" -> ",x)
            
