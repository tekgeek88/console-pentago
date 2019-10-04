Minimax and Minimax with Alpha Beta Pruning details:

Maximum Branching Factor
Without ignoring duplicate states = n_placements * n_tiles * n_directions = 36 * 4 * 2 = 288

MiniMax:
    Expanded Nodes:
    - Depth Limit 2 (d): 288    - Without ignoring duplicate states
    - Depth Limit 2 (d): 37     - After creating a transition set an only creating unique states
    - Depth Limit 3 (d): 3402   - After creating a transition set an only creating unique states

    - Time Complexity:  O(b^d)
    - Space Complexity: O(b*d)


AlphaBeta:
    Expanded Nodes:
    - Depth Limit 3 (d): 273    - After creating a transition set an only creating unique states
    - Depth Limit 4 (d): 9727   - After creating a transition set an only creating unique states
    - Depth Limit 5 (d): 87312  - After creating a transition set an only creating unique states

    Best Case: - In the case moves are selected with the highest utility value first
    - Time Complexity:  O(b^(d/2))
    - Space Complexity: O(b^(d/2))

    Worst Case: - Moves with low utility are expanded first the tree will be right heavy with alpha beta values
    - Time Complexity:  O(b^d)
    - Space Complexity: O(b*d)
