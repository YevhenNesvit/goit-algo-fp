class Node:

    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node

    def insert_after(self, prev_node: Node, data):
        if prev_node is None:
            print("Попереднього вузла не існує.")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, key: int):
        cur = self.head
        if cur and cur.data == key:
            self.head = cur.next
            cur = None
            return
        prev = None
        while cur and cur.data != key:
            prev = cur
            cur = cur.next
        if cur is None:
            return
        prev.next = cur.next
        cur = None

    def search_element(self, data: int) -> Node | None:
        cur = self.head
        while cur:
            if cur.data == data:
                return cur
            cur = cur.next
        return None

    def print_list(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

    def reverse_list(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def insertion_sort(self):
        if self.head is None or self.head.next is None:
            return

        sorted_head = None
        current = self.head

        while current:
            next_node = current.next

            if sorted_head is None or sorted_head.data >= current.data:
                current.next = sorted_head
                sorted_head = current
            else:
                temp = sorted_head
                while temp.next and temp.next.data < current.data:
                    temp = temp.next
                current.next = temp.next
                temp.next = current

            current = next_node

        self.head = sorted_head

    def merge_sorted_lists(self, other_list):
        result = LinkedList()
        current_self = self.head
        current_other = other_list.head

        while current_self and current_other:
            if current_self.data < current_other.data:
                result.insert_at_end(current_self.data)
                current_self = current_self.next
            else:
                result.insert_at_end(current_other.data)
                current_other = current_other.next

        while current_self:
            result.insert_at_end(current_self.data)
            current_self = current_self.next

        while current_other:
            result.insert_at_end(current_other.data)
            current_other = current_other.next

        self.head = result.head


llist = LinkedList()
other_llist = LinkedList()

# Вставляємо вузли в початок
llist.insert_at_beginning(5)
llist.insert_at_beginning(10)
llist.insert_at_beginning(15)
other_llist.insert_at_beginning(4)
other_llist.insert_at_beginning(3)
other_llist.insert_at_beginning(2)

# Вставляємо вузли в кінець
llist.insert_at_end(20)
llist.insert_at_end(25)
other_llist.insert_at_end(16)
other_llist.insert_at_end(27)

# Друк зв'язного списку
print("Зв'язний список:")
llist.print_list()
other_llist.print_list()

# Перевертаємо зв'язний список
llist.reverse_list()
print("Зв'язний список:")
llist.print_list()

# Сортуємо зв'язний список
llist.insertion_sort()
print("Зв'язний список:")
llist.print_list()

# Об'єднуємо два зв'язний списки
llist.merge_sorted_lists(other_llist)
print("Об'єднаний зв'язний список:")
llist.print_list()
