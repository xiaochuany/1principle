# type: ignore
# flake8: noqa
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
def decision_tree(S):
    
    splits = get_splits(S)
    gains = [(compute_gain(S,split), split) for split in splits] # gain is typically measured in terms of purity improvement
    root = argmax(gains)[1] # argmin returns the tuple achieving the largest gain
    S1, S2 = partition(best_split)
    root.left, root.right = decision_tree(S1), decision_tree(S2)
    return root
#
#
#
#
#
#
#
#
#
#
#
#
#
