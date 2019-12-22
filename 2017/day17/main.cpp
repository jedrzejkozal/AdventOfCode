#include <iostream>
#include <tuple>

class LockNode
{
public:
    LockNode(unsigned v)
    {
        value = v;
    }

    void insert(LockNode *new_node)
    {
        new_node->next_node = next_node;
        next_node = new_node;
    }

    unsigned value;
    LockNode *next_node;
};

LockNode *compute_spinlock(unsigned step, unsigned num_steps)
{
    LockNode *spinlock = new LockNode(0);
    spinlock->next_node = spinlock;

    for (unsigned i = 1; i < num_steps + 1; i++)
    {
        for (unsigned j = 0; j < step; j++)
        {
            spinlock = spinlock->next_node;
        }
        LockNode *new_node = new LockNode(i);
        spinlock->insert(new_node);
        spinlock = spinlock->next_node;
    }
    return spinlock;
}


int main()
{
    LockNode *spinlock = compute_spinlock(359, 50000000);

    // find zero
    while (spinlock->value != 0)
    {
        spinlock = spinlock->next_node;
    }

    unsigned solution2 = spinlock->next_node->value;
    std::cout << "part2 solution = " << solution2 << std::endl;
    return 0;
}
