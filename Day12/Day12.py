# Khởi tạo hàng đợi dùng list
queue = [1,4,5,6,2,9]
# Xem phần tử ở đầu hàng đợi
print(queue[0])
#Thêm phần tử vào cuối hàng đợi ~ enqueue() ~ O(1)
queue.append(7)
# Xóa phần tử ở đầu hàng đợi ~ dequeue() ~ O(1)
queue.pop(0)
#Kiểm tra hàng đợi queue có rỗng hay không
def is_empty(queue):
    if len(queue) == 0:
        return True
    else:
        return False

#Khởi tạo hàng đợi dùng thư viện collection queue
import queue
queue2 = queue.Queue(maxsize=5)
queue2.put('1')
queue2.put('2')
queue2.put('3')
queue2.put('4')
queue2.put('5')
# Kiểm tra hàng đợi có rỗng hay không
print(queue2.empty())
# Kiểm tra hàng đợi có đầy hay không
print(queue2.full())
#In độ dài max size của hàng đợi
print(queue2.maxsize)
# Lấy và xóa phần tử đầu tiên trong hàng đợi
n1 = queue2.get()
print(n1)
n2 = queue2.get()
print(n2)
#=================Chữa bài thực hành trên lớp===============
import queue
class MP3Player:
    def __init__(self) -> None:
        self.song_queue = queue.Queue()
        self.current_song = None

    def add_song(self,song):
        self.song_queue.put(song)
        print(f"Đã thêm bài hát {song} vào hàng đợi")
    
    def play_next_song(self):
        if self.song_queue.empty():
            print(f"Không có bài hát nào trong hàng đợi")
        else:
            self.current_song = self.song_queue.get()
            print(f"Đang phát bài hát {self.current_song}")
    
    def skip_song(self):
        if self.current_song is None:
            print(f"Không có bài hát nào đang phát.")
        else:
            print(f"Đã bỏ qua bài hát: {self.current_song}")
            self.current_song = None
            self.play_next_song()

mp3_player = MP3Player()

mp3_player.add_song("Bài hát 1")
mp3_player.add_song("Bài hát 2")
mp3_player.add_song("Bài hát 3")

mp3_player.play_next_song()

mp3_player.skip_song()

mp3_player.add_song("Bài hát 4")

mp3_player.play_next_song()
mp3_player.play_next_song()