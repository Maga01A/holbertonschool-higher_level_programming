#!/usr/bin/python3
def multiple_returns(senctence):
    if senctence == "":
        return (0, None)
    else:
        return (len(senctence), senctence[0])
