# H. Все наоборот

# Ограничение времени	1 секунда
# Ограничение памяти	64Mb
# Ввод	стандартный ввод или input.txt
# Вывод	стандартный вывод или output.txt

# Вася решил запутать маму —– делать дела в обратном порядке. Список его дел теперь хранится в двусвязном списке. 
# Напишите функцию, которая вернёт список в обратном порядке.
# Внимание: в этой задаче не нужно считывать входные данные. 
# Нужно написать только функцию, которая принимает на вход голову двусвязного списка и возвращает голову перевернутого списка. 
# Ниже дано описание структуры, которая задаёт вершину списка.
# Внимание! Решение надо отправлять только в виде файла с расширением, которое соответствует вашему языку. 
# Иначе даже корректно написанное решение не пройдет тесты.

# Формат ввода
# Функция принимает на вход единственный аргумент — голову двусвязного списка.
# Python:
# Если вы пишете на Python, функция должна называться solution и принимать на вход вершину node.
# Узел списка описывается следующим классом:

# class DoubleConnectedNode:  
#     def __init__(self, value, next=None, prev=None):  
#         self.value = value  
#         self.next = next  
#         self.prev = prev
# С++: 
# struct Node {  
#     Node(const std::string &value, Node* next, Node* prev) : value(value), next(next), prev(prev) {}  
 
#     std::string value;  
#     Node* next;  
#     Node* prev;  
# };  
# Node* solution(Node* head);
# Нужно подключить solution.h 

# Go: 
# type ListNode struct {  
#     data     string  
#     next  *ListNode  
#     prev  *ListNode  
# }  
# Ваша функция должна называться Solution.

# JS: 
# class Node {  
#   constructor(value = null, next = null, prev = null) {  
#     this.value = value;  
#     this.next = next;  
#     this.prev = prev;  
#   }  
# }
# Ваша функция должна называться solution. 

# Java:
# Файл должен содержать public class Solution с public static Node<String> solution(Node<String> head)

# class Node<V> {  
#     public V value;  
#     public Node<V> next;  
#     public Node<V> prev;  
 
#     public Node(V value, Node<V> next, Node<V> prev) {  
#         this.value = value;  
#         this.next = next;  
#         this.prev = prev;  
#     }  
# }
# Формат вывода
# Функция должна вернуть голову развернутого списка.
# Примечания
# Решение нужно отправлять в виде файла с расширением соответствующем вашему языку программирования. 
# Нужно выбирать компилятор make. Для Java файл должен называться Solution.java 
# Для остальных языков программирования это имя использовать нельзя (имя solution тоже).


class DoubleConnectedNode:
    def __init__(self, value, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev

def solution(head, tail=None):
    while head:
        head.next, tail, head = tail, head, head.next
    return tail