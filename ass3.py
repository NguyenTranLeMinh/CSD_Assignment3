class Person:
    def __init__(self, ID, name, birth, birthplace):
        self.id = str(ID)
        self.name = str(name)
        self.birth = str(birth)
        self.birthplace = str(birthplace)
    
    def __str__(self):
        return '\n'.join(['ID: '+self.id, 'Name: '+self.name, 'Birthday: '+self.birth, 'Birthplace: '+self.birthplace])

    def __lt__(self, person):
        return self.id < person.id

    def __eq__(self, person):
        return self.id == person.id

class TreeNode:
    def __init__(self, val=None):
        self.value = val
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.value)


class BST:
    def __init__(self, data=None):
        #self.root = None
        #self.list_node = []
        if data is not None:
            for value in data:
                self.insert(self.root, value)

    #@staticmethod
    def insert(self, cur: TreeNode, value: Person):
        if cur is None:
            return TreeNode(value)
        else:
            if value < cur.value:
                cur.left = self.insert(cur.left, value)
            elif cur.value < value:
                cur.right = self.insert(cur.right, value)
        return cur
    
    def inOrder(self, root):
        if root is None:
            return
        self.inOrder(root.left)
        print(root)
        self.inOrder(root.right)
    
    def search(self, root, ID):
        if root is None or ID == root.value.id:
            return root
        if ID < root.value.id:
            return self.search(root.left, ID)
        return self.search(root.right, ID)
    
    def delete(self, root, ID, message):
        if root is None:
            if len(message) == 0:
                message.append('The searched ID is not valid.')
            return root
        if ID < root.value.id:
            root.left = self.delete(root.left, ID, message)
        elif root.value.id < ID:
            root.right = self.delete(root.right, ID, message)
        else:
            if len(message) == 0:
                message.append(str(root.value))
            #self.list_node.remove(root.value.id)
            if root.left is None:
                temp = root.right
                root = None
                return temp
            if root.right is None:
                temp = root.left
                root = None
                return temp
            
            sub_tree = root.right
            while sub_tree.left:
                sub_tree = sub_tree.left
            # Bay gio, sub_tree la Min node trong nhanh phai (nhanh Max)
            # Overriding
            root.value.id = sub_tree.value.id
            root.value.name = sub_tree.value.name
            root.value.birth = sub_tree.value.birth
            root.value.birthplace = sub_tree.value.birthplace

            # delete sub_tree, assign for root.right for updating purpose
            root.right = self.delete(root.right, sub_tree.value.id, message)
            
        return root


class Main:
    # Class attribute
    # Shared params between objects
    path = 'CSD203x_asm3_FX10511/data.txt'
    max_request = 6
    input_stt = 'Lựa chọn của bạn (Vui lòng nhập STT tương ứng): '
    text = ['+-------------------Menu------------------+',
                     'Person Tree:',
                     '1. Load the data from the file.',
                     '2. Insert a new Person.',
                     '3. Inorder traverse.',
                     '4. Breadth-First Traversal traverse.',
                     '5. Search by Person ID.',
                     '6. Delete by Person ID.',
                     'Exit:',
                     '0. Exit',
                     '+-----------------------------------------.+']

    def __init__(self):
        self.choice = None
        self.root = None
        self.t = BST()

    def menu(self):
        print('\n'.join(Main.text))
    
    def get_choice(self):
        self.choice = input(Main.input_stt)
        self.validation()

    def validation(self):
        while 1:
            try:
                self.choice = int(self.choice)
                if 0 <= self.choice <= Main.max_request:
                    break
                else:
                    print(f'Vui lòng nhập STT từ 0-{Main.max_request}.')
            except ValueError:
                print('Vui lòng nhập 1 số nguyên.')
            self.get_choice()

    def response(self):
        if self.choice == 1:
            self.load_from_file()
        elif self.choice == 2:
            self.insert_new_person()
        elif self.choice == 3:
            self.t.inOrder(self.root)
        elif self.choice == 4:
            self.BFS()
        elif self.choice == 5:
            self.search()
        elif self.choice == 6:
            self.delete()
    
    def process(self):
        while self.choice != 0:
            self.menu()
            self.get_choice()
            self.response()

    def load_from_file(self, path=None):
        if path is None:
            path = Main.path
        with open(path) as f:
            for line in f:
                info = line.rstrip().split(',')
                #self.t.list_node.append(info[0])
                self.root = self.t.insert(self.root, Person(*info))
        print('The file is loaded successfully!')

    def insert_new_person(self):
        tmp = [1]
        for _ in tmp:
            tmp_id = input('ID: ')
            flag = True if self.t.search(self.root, tmp_id) else False
            if flag:
                tmp.append(1)
                print('This ID has been chosen, please choose another ID!')
        tmp_name = input('Name: ')
        tmp_birth = input('Birthday: ')
        tmp_birthplace = input('Birthplace: ')
        new_person = Person(tmp_id, tmp_name, tmp_birth, tmp_birthplace)
        self.root = self.t.insert(self.root, new_person)
        #self.t.list_node.append(tmp_id)
        print(new_person)

    def BFS(self):
        queue = [self.root]
        print('Breadth-First Traversal traverse: ')
        while queue:
            node = queue.pop(0)
            print(node)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    def search(self):
        ID = input('Please insert the ID: ')
        print(f'Search for ID = {ID}')
        out = self.t.search(self.root, ID)
        print(out if out else 'The searched ID is not valid.')

    def delete(self):
        ID = input('Please insert the ID: ')
        print(f'Delete the person with ID = {ID}')
        message = []
        self.root = self.t.delete(self.root, ID, message)
        print(*message)


if __name__ == "__main__":
    m = Main()
    m.process()