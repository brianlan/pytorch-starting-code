###############################################################################
# Create class for your dataset
# ------------------------------
#
#   1. Modify the class name which reflects your actual circumstances.
#   2. Implement __init__, __len__ and __getitem__
#   3. Test this class is correctly implemented by dataset[i] (presume dataset
#      is an instance of MyDataset and i is the index of data you wanna get)
###############################################################################
from torch.utils.data import Dataset


class MyDataset(Dataset):
    def __init__(self):
        #####################################################################
        # You can decide what to passed in as arguments to
        # initialize your Dataset instance.
        #
        # Normal choice would be data directory or a indices file which
        # stores all the locations to your data.
        #
        # Another one would be a transform which does online augmentation
        # to your data.
        #
        # NOTE: You'd better to consider both image and label together here.
        #####################################################################
        pass

    def __len__(self):
        #####################################################################
        # You should already have some kind of list in your class after
        # __init__ whose length should be equal the the number of your
        # images.
        #
        # Please return the length of it here. It is required by a
        # pytorch DataLoader.
        #####################################################################
        pass

    def __getitem__(self, index):
        #####################################################################
        # index should be an non-negative integer no more than the length of
        # your images.
        #
        # So, __getitem__ should return the index-th data (better to return
        # both an image and its corresponding label).
        #
        # You can also do the transform to both your image and label here
        # if the transform is provided in __init__.
        #####################################################################
        pass
