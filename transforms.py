###############################################################################
# Define your transforms here.
# -------------------------------
#
# Transforms are not something necessarily needed to train a model.
# However, random transforms do help you to enrich the variety of your
# training data, which brings better generalization ability to your model.
#
# So, a balanced choice would be skipping them at the first stage, and
# after your model training procedures become smooth, consider add them in.
#
# Here we list some useful kinds of transforms here for your reference:
#    1. Random Horizontal Flip
#    2. Random Crop and Resize
#    3. Random Color Jitter
#    4. Resize
###############################################################################


class MyTransform:
    def __init__(self):
        #######################################################################
        # Some values your want to store in the class. If nothing, feel free
        # to skip it.
        #######################################################################
        pass

    def __call__(self):
        #######################################################################
        # The major part of a transform class. Better to handle both image
        # and label, and return the transformed ones
        #######################################################################
        pass
