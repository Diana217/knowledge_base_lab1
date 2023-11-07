from owlready2 import *

namespace = 'http://test.org/pizza.owl'

onto = get_ontology(namespace)

with onto:
    class Pizza(Thing):
        def serve(self):
            print('Hmm, delicious pizza!')

    class has_toppings(Pizza >> str, FunctionalProperty):
        pass

    class has_cheese(Pizza >> str, FunctionalProperty):
        pass

    class has_spicy_level(Pizza >> str, FunctionalProperty):
        pass

    class has_size(Pizza >> str, FunctionalProperty):
        pass

    class has_cooking_time(Pizza >> int, FunctionalProperty):
        pass

    class has_price(Pizza >> float, FunctionalProperty):
        pass

    class is_gluten_free(Pizza >> bool, FunctionalProperty):
        pass

    class Margherita(Pizza):
        equivalent_to = [
            Pizza
            & has_toppings.only('Tomato,Mozzarella,Basil')
            & has_cheese.exactly('Mozzarella')
            & has_spicy_level.exactly('Mild')
            & has_size.exactly('Medium')
            & has_cooking_time.exactly(15)
            & has_price.exactly(10.99)
            & is_gluten_free.exactly(True)
        ]

        def serve(self):
            print("Margherita pizza served! A classic choice with Tomato, Mozzarella, and Basil toppings.")

    class Pepperoni(Pizza):
        equivalent_to = [
            Pizza
            & has_toppings.only('Tomato,Mozzarella,Pepperoni')
            & has_cheese.exactly('Mozzarella')
            & has_spicy_level.exactly('Medium')
            & has_size.exactly('Large')
            & has_cooking_time.exactly(18)
            & has_price.exactly(12.99)
            & is_gluten_free.exactly(False)
        ]

        def serve(self):
            print("Pepperoni pizza served! Loaded with Tomato, Mozzarella, and Pepperoni toppings.")

    class Vegetarian(Pizza):
        equivalent_to = [
            Pizza
            & has_toppings.only('Tomato,Mozzarella,Bell Peppers,Mushrooms,Onions')
            & has_cheese.exactly('Mozzarella')
            & has_spicy_level.exactly('Mild')
            & has_size.exactly('Medium')
            & has_cooking_time.exactly(16)
            & has_price.exactly(11.50)
            & is_gluten_free.exactly(True)
        ]

        def serve(self):
            print("Vegetarian pizza served! Packed with Tomato, Mozzarella, Bell Peppers, Mushrooms, and Onions.")

    class BBQChicken(Pizza):
        equivalent_to = [
            Pizza
            & has_toppings.only('BBQ Sauce,Grilled Chicken,Onions,Mozzarella')
            & has_cheese.exactly('Mozzarella')
            & has_spicy_level.exactly('Medium')
            & has_size.exactly('Large')
            & has_cooking_time.exactly(20)
            & has_price.exactly(13.75)
            & is_gluten_free.exactly(False)
        ]

        def serve(self):
            print("BBQ Chicken pizza served! A flavorful treat with BBQ Sauce, Grilled Chicken, Onions, and Mozzarella.")

    class Hawaiian(Pizza):
        equivalent_to = [
            Pizza
            & has_toppings.only('Tomato,Mozzarella,Ham,Pineapple')
            & has_cheese.exactly('Mozzarella')
            & has_spicy_level.exactly('Mild')
            & has_size.exactly('Medium')
            & has_cooking_time.exactly(17)
            & has_price.exactly(12.25)
            & is_gluten_free.exactly(True)
        ]

        def serve(self):
            print("Hawaiian pizza served! Sweet and savory with Ham, Pineapple, Tomato, and Mozzarella.")

print('Before:')
pizza1 = Margherita('pizza1')
print(pizza1.name)
pizza1.serve()

pizza1.has_toppings = 'Tomato,Mozzarella,Basil'
pizza1.has_cheese = 'Mozzarella'
pizza1.has_spicy_level = 'Mild'
pizza1.has_size = 'Medium'

print()

pizza2 = Pepperoni('pizza2')
print(pizza2.name)
pizza2.serve()

pizza2.has_toppings = 'Tomato,Mozzarella,Pepperoni'
pizza2.has_cheese = 'Mozzarella'
pizza2.has_spicy_level = 'Medium'
pizza2.has_size = 'Large'

print()

pizza3 = Vegetarian('pizza3')
print(pizza3.name)
pizza3.serve()

pizza3.has_toppings = 'Tomato,Mozzarella,Bell Peppers,Mushrooms,Onions'
pizza3.has_cheese = 'Mozzarella'
pizza3.has_spicy_level = 'Mild'
pizza3.has_size = 'Medium'

print()

pizza4 = BBQChicken('pizza4')
print(pizza4.name)
pizza4.serve()

pizza4.has_toppings = 'BBQ Sauce,Grilled Chicken,Onions,Mozzarella'
pizza4.has_cheese = 'Mozzarella'
pizza4.has_spicy_level = 'Medium'
pizza4.has_size = 'Large'

print()

pizza5 = Hawaiian('pizza5')
print(pizza5.name)
pizza5.serve()

pizza5.has_toppings = 'Tomato,Mozzarella,Ham,Pineapple'
pizza5.has_cheese = 'Mozzarella'
pizza5.has_spicy_level = 'Mild'
pizza5.has_size = 'Medium'

print()

# Saving ontology to a file
onto.save(file='pizza.owl', format="rdfxml")
