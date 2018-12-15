###############################################################################
# Implement your neural network here
###############################################################################
import torch.nn as nn


class MyNet(nn.Module):
    def __init__(self):
        super().__init__()
        ################################
        # your module goes here ...
        ################################
        self.conv = nn.Conv2d(3, 4, 3)
        pass

        #######################################################################
        # initialize your modules that contains parameters (weights and bias)
        #######################################################################
        pass

    def forward(self, input):
        return self.conv(input)
