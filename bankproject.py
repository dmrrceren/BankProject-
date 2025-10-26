# -*- coding: utf-8 -*-
# Banka Kuyruğu - Öncelikli Kuyruk (Priority Queue) Uygulaması
# Dairesel Bağlı Listeler ile

class Node:
    def __init__(self, name):
        self.name = name
        self.next = None

class CircularQueue:
    def __init__(self):
        self.rear = None

    def is_empty(self):
        return self.rear is None

    def enqueue(self, name):
        new_node = Node(name)
        if self.is_empty():
            self.rear = new_node
            self.rear.next = new_node  # dairesel bağlantı
        else:
            new_node.next = self.rear.next
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        if self.is_empty():
            return None
        front = self.rear.next
        if self.rear == front:  # tek eleman varsa
            self.rear = None
        else:
            self.rear.next = front.next
        return front.name

    def display(self):
        if self.is_empty():
            return "Boş"
        result = []
        current = self.rear.next
        while True:
            result.append(current.name)
            current = current.next
            if current == self.rear.next:
                break
        return " -> ".join(result)


class BankQueue:
    def __init__(self):
        # 0: düşük, 1: orta, 2: yüksek öncelik
        self.queues = [CircularQueue(), CircularQueue(), CircularQueue()]

    def enqueue(self, name, priority):
        if 0 <= priority <= 2:
            self.queues[priority].enqueue(name)
            print(f"{name}, {priority}. öncelikli gruba eklendi.")
        else:
            print("Geçersiz öncelik seviyesi! (0 - düşük, 1 - orta, 2 - yüksek)")

    def dequeue(self):
        for i in range(2, -1, -1):  # yüksek öncelikten düşük olana
            if not self.queues[i].is_empty():
                name = self.queues[i].dequeue()
                print(f"{name}, {i}. öncelikli gruptan çıkarıldı.")
                return
        print("Tüm kuyruklar boş!")

    def show_queues(self):
        print("\n--- Kuyruk Durumu ---")
        print("2. (Yüksek):", self.queues[2].display())
        print("1. (Orta)  :", self.queues[1].display())
        print("0. (Düşük) :", self.queues[0].display())
        print("----------------------\n")


def main():
    banka = BankQueue()

    while True:
        print("=== Banka Kuyruğu Sistemi ===")
        print("1 - Yeni müşteri ekle (enqueue)")
        print("2 - Müşteri al (dequeue)")
        print("3 - Kuyrukları göster")
        print("4 - Çıkış")
        secim = input("Seçiminiz: ")

        if secim == "1":
            isim = input("Müşteri adı: ")
            print("Öncelik seçiniz: 0 - Düşük | 1 - Orta | 2 - Yüksek")
            oncelik = int(input("Öncelik: "))
            banka.enqueue(isim, oncelik)
        elif secim == "2":
            banka.dequeue()
        elif secim == "3":
            banka.show_queues()
        elif secim == "4":
            print("Program sonlandırıldı.")
            break
        else:
            print("Geçersiz seçim! Tekrar deneyin.\n")

# Programı başlat
if __name__ == "__main__":
    main()
