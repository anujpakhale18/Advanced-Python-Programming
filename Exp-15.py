import gc
import sys

def create_objects():
    a = []
    b = []
    a.append(b)
    b.append(a)
    return a, b

def display_memory():
    print("Memory used:", sys.getsizeof(objects), "bytes")

print("Initial Garbage Collection Count:", gc.get_count())

objects = create_objects()
print("\nAfter creating objects:")
display_memory()

del objects

gc.set_debug(gc.DEBUG_STATS)

collected = gc.collect()

print("\nGarbage collected:", collected)
print("After garbage collection:")
print("Garbage Collection Count:", gc.get_count())

gc.set_debug(0)

print("\nGarbage collection completed.")