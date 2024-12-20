class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1


class AVLTree:
    def __init__(self):
        self.root = None

    def height(self, node):
        if not node:
            return 0
        return node.height

    def balance(self, node):
        if not node:
            return 0
        return self.height(node.left) - self.height(node.right)

    def _insert(self, root, value):
        if not root:
            return Node(value)
        elif value < root.value:
            root.left = self._insert(root.left, value)
        else:
            root.right = self._insert(root.right, value)

        root.height = 1 + max(self.height(root.left), self.height(root.right))
        balance = self.balance(root)

        # Left rotation
        if balance > 1 and value < root.left.value:
            return self.right_rotate(root)

        # Right rotation
        if balance < -1 and value > root.right.value:
            return self.left_rotate(root)

        # Left-Right rotation
        if balance > 1 and value > root.left.value:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        # Right-Left rotation
        if balance < -1 and value < root.right.value:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    def _delete(self, root, value):
        if not root:
            return root

        if value < root.value:
            root.left = self._delete(root.left, value)
        elif value > root.value:
            root.right = self._delete(root.right, value)
        else:
            if not root.left:
                temp = root.right
                root = None
                return temp
            elif not root.right:
                temp = root.left
                root = None
                return temp

            temp = self.min_value_node(root.right)
            root.value = temp.value
            root.right = self.delete(root.right, temp.value)

        if not root:
            return root

        root.height = 1 + max(self.height(root.left), self.height(root.right))
        balance = self.balance(root)

        # Left rotation
        if balance > 1 and self.balance(root.left) >= 0:
            return self.right_rotate(root)

        # Right rotation
        if balance < -1 and self.balance(root.right) <= 0:
            return self.left_rotate(root)

        # Left-Right rotation
        if balance > 1 and self.balance(root.left) < 0:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        # Right-Left rotation
        if balance < -1 and self.balance(root.right) > 0:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    def left_rotate(self, z):
        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        z.height = 1 + max(self.height(z.left), self.height(z.right))
        y.height = 1 + max(self.height(y.left), self.height(y.right))

        return y

    def right_rotate(self, z):
        y = z.left
        T3 = y.right

        y.right = z
        z.left = T3

        z.height = 1 + max(self.height(z.left), self.height(z.right))
        y.height = 1 + max(self.height(y.left), self.height(y.right))

        return y

    def min_value_node(self, root):
        current = root
        while current.left:
            current = current.left
        return current

    def _search(self, root, value):
        if not root:
            return root
        if root.value == value:
            return root
        if root.value < value:
            return self._search(root.right, value)
        else:
            return self._search(root.left, value)

    def insert(self, value):
        self.root = self._insert(self.root, value)

    def delete(self, value):
        self.root = self._delete(self.root, value)

    def search(self, value):
        return self._search(self.root, value)


# Example usage:
if __name__ == "__main__":
    tree = AVLTree()
    tree.insert(10)
    tree.insert(20)
    tree.insert(30)
    tree.insert(40)
    tree.insert(50)

    print("Tree after insertion:")
    # In-order traversal to print the tree
    def inorder_traversal(root):
        if root:
            inorder_traversal(root.left)
            print(root.value),
            inorder_traversal(root.right)

    inorder_traversal(tree.root)
    print()

    tree.delete(20)
    print("Tree after deletion of 20:")
    inorder_traversal(tree.root)
    print()

    result = tree.search(30)
    if result:
        print("Node found")
    else:
        print("Node not found")

        
# class Node:
#     def __init__(self, key):
#         self.left = None
#         self.right = None
#         self.value = key
#
# class BinarySearchTree:
#     def __init__(self):
#         self.root = None
#
#     # Вставка нового элемента
#     def insert(self, key):
#         if self.root is None:
#             self.root = Node(key)
#         else:
#             self._insert(self.root, key)
#
#     def _insert(self, node, key):
#         if key < node.value:
#             if node.left is None:
#                 node.left = Node(key)
#             else:
#                 self._insert(node.left, key)
#         else:
#             if node.right is None:
#                 node.right = Node(key)
#             else:
#                 self._insert(node.right, key)
#
#     # Поиск элемента
#     def search(self, key):
#         return self._search(self.root, key)
#
#     def _search(self, node, key):
#         if node is None or node.value == key:
#             return node
#         elif key < node.value:
#             return self._search(node.left, key)
#         else:
#             return self._search(node.right, key)
#
#     # Удаление элемента
#     def delete(self, key):
#         self.root = self._delete(self.root, key)
#
#     def _delete(self, node, key):
#         if node is None:
#             return node
#         if key < node.value:
#             node.left = self._delete(node.left, key)
#         elif key > node.value:
#             node.right = self._delete(node.right, key)
#         else:
#             # Узел с одним или двумя потомками
#             if node.left is None:
#                 return node.right
#             elif node.right is None:
#                 return node.left
#             # Узел с двумя потомками
#             min_larger_node = self._find_min(node.right)
#             node.value = min_larger_node.value
#             node.right = self._delete(node.right, min_larger_node.value)
#         return node
#
#     def _find_min(self, node):
#         while node.left is not None:
#             node = node.left
#         return node
#
#     # Печать дерева в порядке возрастания
#     def inorder(self):
#         self._inorder(self.root)
#
#     def _inorder(self, node):
#         if node:
#             self._inorder(node.left)
#             print(node.value, end=" ")
#             self._inorder(node.right)
#
# # Пример использования
# bst = BinarySearchTree()
# bst.insert(50)
# bst.insert(30)
# bst.insert(20)
# bst.insert(40)
# bst.insert(70)
# bst.insert(60)
# bst.insert(80)
#
# print("Дерево в порядке возрастания:")
# bst.inorder()
#
# result = bst.search(40)
# print("\nПоиск 40:", "Найден" if result else "Не найден")
#
# bst.delete(20)
# print
