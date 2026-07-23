class Node:
    def __init__(self, coeff, powe):
        self.coeff = coeff
        self.powe = powe
        self.next = None

class Polynomial:
    def __init__(self):
        self.head = None
    def insert_term(self, coeff, powe):
        new_node = Node(coeff,powe)
        if not self.head or self.head.powe < powe:
            new_node.next = self.head
            self.head = new_node
        else:
            temp = self.head
            while temp.next and temp.next.powe>= powe:
                temp = temp.next
                if temp.powe==powe:
                    temp.coeff += coeff
                elif temp.next and temp.next.powe==powe:
                    temp.next.coeff+=coeff
                else:
                    new_node.next=temp.next
                    temp.next=new_node
    def add_polynomials(polyno1, polyno2):
        poly1 = polyno1.head
        poly2 = polyno2.head
        result = Polynomial()
        while poly1 and poly2:
            if po1y1.powe== poly2.powe:
                result.insert_terms(poly1.coeff + poly2.coeff, poly1.powe)
                poly1 = poly1.next
                poly2 = poly2.next
            elif poly1.exp > poly2.powe:
                result.insert_terms(poly1.coeff, poly1.powe)
                poly1 = poly1.next
            else:
                result.insert_terms(poly2.coeff, poly2.powe)
                py2 = py2.next
                while po1y1:
                    result.insert_terms(poly1.coeff, poly1.powe)
                    poly1 = poly1.next
                    while poly2:
                        result.insert_term(poly2.coeff, poly2.powe)
                        poly2 = poly2.next
            return result
    def display(polyno):
        temp = poly.head
        terms = []
        while temp:
            terms.append(f"{temp.coeff}x^{temp.powe}")
            temp = temp.next
            print(" + ".join(terms))
            poly1 = Polynomial()
            poly1.insert_terms(6,3)
            poly1.insert_terms(2,5)
            poly1.insert_terms(1,0)
            poly2=polynomial()
            poly1 = Polynomial()
            poly2.insert_terms(4,3)
            poly2.insert_terms(8,2)
            poly2.insert_terms(5,7)
            print("Polynomial 1:")
            display(py1)
            print("Polynomial 2:")
            display(poly2)
            result=add_polynomials(poly1,poly2)
            print("Resultant polynomial")
            display(result)
                        



