
# SW알고리즘개발 과제2

class Node:
    def __init__(self, elem, next=None):
        self.data = elem
        self.link = next


    def append(self, new):
        if new is not None:
            new.link = self.link
            self.link = new


    def popNext(self):
        deleted_node = self.link
        if deleted_node is not None:
            self.link = deleted_node.link
        return deleted_node


class Book:
    def __init__(self, book_id, title, author, year):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.year = year


    def __str__(self):
        return f"[책번호 : {self.book_id}, 제목 : {self.title}, 저자 : {self.author}, 출판 연도 : {self.year}]"


class LinkedList:
    def __init__(self):
        self.head = None


    def isEmpty(self):
        return self.head is None


    def append(self, book):
        new_node = Node(book)
        if self.isEmpty():
            self.head = new_node
        else:
            node = self.head
            while node.link is not None:
                node = node.link
            node.link = new_node


    def find_by_title(self, title):
        node = self.head
        while node is not None:
            if node.data.title == title:
                return node.data
            node = node.link
        return None


    def find_pos_by_title(self, title):
        if self.isEmpty():
            return None
        if self.head.data.title == title:
            return None
        node = self.head
        while node.link is not None:
            if node.link.data.title == title:
                return node
            node = node.link
        return None


    def find_by_id(self, book_id):
        node = self.head
        while node is not None:
            if node.data.book_id == book_id:
                return node.data
            node = node.link
        return None


    def delete_by_title(self, title):
        if self.isEmpty():
            return False
        if self.head.data.title == title:
            self.head = self.head.link
            return True
        prev = self.find_pos_by_title(title)
        if prev is None or prev.link is None:
            return False
        prev.popNext()
        return True


    def display_all(self):
        if self.isEmpty():
            print("현재 등록된 도서가 없습니다.")
            return
        node = self.head
        print("현재 등록된 도서 목록")
        while node is not None:
            print(node.data)
            node = node.link


class BookManagement:
    def __init__(self):
        self.books = LinkedList()

    def add_book(self, book_id, title, author, year):
        if self.books.find_by_id(book_id) is not None:
            print("중복된 책 번호입니다.")
            return
        new_book = Book(book_id, title, author, year)
        self.books.append(new_book)
        print(f"도서 '{title}'가 추가되었습니다.")

    def remove_book(self, title):
        if self.books.delete_by_title(title):
            print("도서가 삭제되었습니다.")
        else:
            print("해당 제목의 도서를 찾을 수 없습니다.")

    def search_book(self, title):
        found = self.books.find_by_title(title)
        if found:
            print("도서 정보:")
            print(found)
        else:
            print("해당 제목의 도서를 찾을 수 없습니다.")

    def display_books(self):
        self.books.display_all()

    def run(self):
        while True:
            print("\n=== 도서 관리 프로그램 ===")
            print("1. 도서 추가")
            print("2. 도서 삭제 (책 제목으로 삭제)")
            print("3. 도서 조회 (책 제목으로 조회)")
            print("4. 전체 도서 목록 출력")
            print("5. 종료")
            choice = input("메뉴를 선택하세요: ")

            if choice == '1':
                try:
                    book_id = int(input("책 번호를 입력하세요: "))
                    title = input("책 제목을 입력하세요: ")
                    author = input("저자를 입력하세요: ")
                    year = input("출판 연도를 입력하세요: ")
                    self.add_book(book_id, title, author, year)
                except ValueError:
                    print("책 번호는 숫자여야 합니다.")

            elif choice == '2':
                title = input("삭제할 책 제목을 입력하세요: ")
                self.remove_book(title)

            elif choice == '3':
                title = input("조회할 책 제목을 입력하세요: ")
                self.search_book(title)

            elif choice == '4':
                self.display_books()

            elif choice == '5':
                print("프로그램을 종료합니다.")
                break

            else:
                print("1~5 사이의 번호를 입력하세요.")



if __name__ == "__main__":
    manager = BookManagement()
    manager.run()