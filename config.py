# This file MUST be configured in order for the code to run properly

# Make sure you put all your input images into an 'assets' folder. 
# Each layer (or category) of images must be put in a folder of its own.

# CONFIG is an array of objects where each object represents a layer
# THESE LAYERS MUST BE ORDERED.

# Each layer needs to specify the following
# 1. id: A number representing a particular layer
# 2. name: The name of the layer. Does not necessarily have to be the same as the directory name containing the layer images.
# 3. directory: The folder inside assets that contain traits for the particular layer
# 4. required: If the particular layer is required (True) or optional (True). The first layer must always be set to true.
# 5. rarity_weights: Denotes the rarity distribution of traits. It can take on three types of values.
#       - None: This makes all the traits defined in the layer equally rare (or common)
#       - "random": Assigns rarity weights at random. 
#       - array: An array of numbers where each number represents a weight. 
#                If required is True, this array must be equal to the number of images in the layer directory. The first number is  the weight of the first image (in alphabetical order) and so on...
#                If required is True, this array must be equal to one plus the number of images in the layer directory. The first number is the weight of having no image at all for this layer. The second number is the weight of the first image and so on...

# Be sure to check out the tutorial in the README for more details.                

CONFIG = [
    {
        'id': 1,
        'name': 'Backgrounds',
        'directory': 'Backgrounds',
        'required': True,
        'rarity_weights': [10, 5, 5, 15, 35, 30]
    },
    {
        'id': 2,
        'name': 'Skins',
        'directory': 'Skins',
        'required': True,
        'rarity_weights': [20, 25, 25, 15, 15]
    },
    {
        'id': 3,
        'name': 'Eyes',
        'directory': 'Eyes',
        'required': True,
        'rarity_weights': [15, 20, 25, 25, 15]
    },
    {
        'id': 4,
        'name': 'Mouths',
        'directory': 'Mouths',
        'required': True,
        'rarity_weights': [25, 25, 15, 20, 15]
    },
    {
        'id': 5,
        'name': 'Clothes',
        'directory': 'Clothes',
        'required': True,
        'rarity_weights': [10, 10, 15, 15, 20, 15, 15]
    },
    {
        'id': 6,
        'name': 'Hairs',
        'directory': 'Hairs',
        'required': True,
        'rarity_weights': [20, 30, 30, 20]
    },
    {
        'id': 7,
        'name': 'Glasses',
        'directory': 'Glasses',
        'required': True,
        'rarity_weights': [25, 25, 15, 20, 15]
    },
    {
        'id': 8,
        'name': 'Hats',
        'directory': 'Hats',
        'required': True,
        'rarity_weights': [25, 25, 15, 20, 15]
    },
    {
        'id': 9,
        'name': 'Necks',
        'directory': 'Necks',
        'required': True,
        'rarity_weights': [30, 40, 30]
    },
    {
        'id': 10,
        'name': 'Random_objects',
        'directory': 'Random_objects',
        'required': True,
        'rarity_weights': [40, 30, 30]
    }
]
