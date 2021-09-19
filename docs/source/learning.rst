.. role:: strike
    :class: strike

=================
Learning to learn
=================

In this section, I'll explain more about
how the AI can learn by playing with you.
I've used 3 types of "learning algorithms"
in this project: Inclusive, Exclusive and
Both. When you open the game, you can change
the default algorithm and see how their
graphs differ from each other. If you're
lazy and don't want to lose to my fearsome
AI, that's okay (even I am tired of losing
that thing), just stick with me and you'll
understand the magic behind the monster.

How do humans learn?
====================

Remember when you was a kid and you wanted
so much that bar of chocolate, but your
mom said: "NO!"? At that moment, you learned
that sometimes, you can't have everything you
want whenever you want. That's one way we lovely
humans can learn, but there are another ways
(just two, to be honest) that are more interesting
if you think like a programmer.

The first one is the learning by reward. This
kind of happens every year when an entity called
"Santa Claus" rewards children based on their
behaviour along the year. If you were a good
boy/girl, you were rewarded with a new bicycle,
a brand new `Nintendo 64 <https://www.youtube.com/watch?v=pFlcqWQVVuU>`_
(pun intended), or anything like that. After opening
the presents under the christmas tree, you learn that
being a nice person can be rewarding, so you'll look
forward being a nice person every year.

Keeping up with the christmas example (and spirit :D),
the other way of learning is based on punishment.
Remember when I said that only the good boys/girls
won cool presents? That's right, the bad boys/girls
don't get anything, but their friends do. And when
they go outside to play and see the cool things their
neighbors got by just being nice, they may be tempted
to change their behaviour the next year and get some
presents too (or they may get mad at Mr. Santa Claus,
start growing green hair and change their names to
*Grinch*).

Meet Mr. Hippocampus
====================

Well, now that you know about how the human learning
process works, you shall teach your computer how to
learn too.

To start simple, we'll pick the game of hexapawn as
a learning base. The main reason for this is that
hexapawn's moves are pretty simple to predict, and
by knowing every single way that the game may end,
helps like, a lot, because you can see if your
AI is truly learning how to play or not.

So, let's start by calculating all game moves:

.. literalinclude:: ../../ai.py
    :linenos:
    :language: python
    :lines: 116-190

That's a lot of code right? But don't worry, it's
actually pretty simple to understand.

When started, the function will simulate the game
state based on the given movecode using the ``self.judge``
object within the Ai class. The judge will execute
the given movecode and then, the algorithm will check
all possible capture movements for the opposing color
(if the last move was a white pawn move, it'll check
for all possible moves for the black pawns, and so on),
generating a list of strings (movecodes). Then, the
algorithm will run the ``__make_nodes()`` function
again, carrying the given movecode plus one member
of the children list (the list of possible moves)
and do all this process again and again, until it
reaches a leaf (a game state where someone win).
In this case, it'll return a Node object containing
no children at all, which causes the application
call stack (its PROGRAM CALL STACK, not MOVE CALL
STACK. They're very different things) to go back
one level (the process is kept open until all
possible trees have been solved, i.e. reached
a leaf) and solve the next children (sorry, I
can't explain how a function that keeps calling
itself until some condition is met properly).

When all trees. subtrees, nodes and leaves are
found, tested and computed, you get that crazy image
that you saw in the last chapter.

If you understood what I tried to say above,
congratulations, you teached your computer how
to remember things and gave it some kind of
"brain". The only sad part is that it'll "think"
randomly and will never become self sentient and
conquer the world.

Mitosis
=======

Cell division time! Yay.

Well, not really.

Remember when I mentioned an "Inclusive" learning
method? It's very similar to cell division and
duplication (a. k. a. Mitosis).

Imagine that the "brain" that we gave to our little
frankenstein is made of genuine biological cells.
Now imagine that everytime a cell is identified as
"good", the brain forces it to make mitosis and create
clones of that cell, so your brain will incompusively
use them more often and making the chance of them
being chosen greater. (just imagine, because that's 
not what really happens under the hood when you 
learn something).

Well, yes, this is in fact a way of learning, but
there's one big problem with it: the chances of choosing
a "bad" node is minimal, but never zero, because the
bad nodes are kept inside the brain, and it may be
randomly picked by the AI. So this may work, but
it's not the best option if you want a 100% accurate
AI to play with.
 
So let's meet Mrs. Lobotomy

Lobotomy
========

For those who don't know, lobotomy is a neurological
surgery which gets your hippocampus (long-term memory)
removed from your brain. The analogy works here too.
Remember the "Exclusive" method? That's right, cutting
time!

This method will remove every single cell that is
identified as "bad" from the brain, preventing it
to make errors. So every time a losing node is 
identified, it'll be removed from the "brain" and
will no longer be possible to be made by the Ai.

Sounds a lot better than mitosis, right?

Well, it is and it isn't. Sure, it prevents the Ai
to repeat the same errors every time, but takes a
lot of time to test and find every single game 
possibility, thus creating the perfect hexapawn Ai.

But what if we mix and match both methods?

Two-Face (a. k. a. Harvey Dent)
===============================

By mixing both methods, our AI will be capable of
removing the nodes that 