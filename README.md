# Accuknox Django Trainee Assignment - 4 Projects

Each question has its own small Django project (Q1-Q3 are Django Signals, Q4 is the Rectangle class). To run any of them:

    pip install django
    cd q1_sync            (or q2_thread / q3_transaction)
    python manage.py migrate
    python manage.py run_demo

| Folder          | Question                                              | Answer        |
|-----------------|-------------------------------------------------------|---------------|
| q1_sync         | Are signals synchronous or asynchronous by default?   | Synchronous   |
| q2_thread       | Do signals run in the same thread as the caller?      | Yes           |
| q3_transaction  | Do signals run in the same DB transaction as caller?  | Yes           |
| q4_rectangle    | Rectangle class that can be iterated over             | See below     |

## How each one proves it
**Q1** - The receiver sleeps for 5 seconds. `create()` also takes 5 seconds and the
prints come in order (before -> receiver start -> receiver end -> after). The caller waits, so it is synchronous.

**Q2** - The caller and the receiver both print the thread name and id. They match,
even when I start my own new thread.

**Q3** - I wrap `Item.objects.create()` in `transaction.atomic()`, the receiver creates a
`Log` row, then I raise an error to force a rollback. Both the Item and the Log row disappear,
and `connection.in_atomic_block` is True inside the receiver, so it shares the caller's transaction.

**Q4** - `Rectangle(length, width)` stores both values. The `__iter__` method uses `yield`
to give `{'length': <value>}` first and then `{'width': <value>}`, so a `for` loop (or `list()`)
on the object gives the length followed by the width. Code is in `q4_rectangle/demo/rectangle.py`.
