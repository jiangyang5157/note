# Handler

- Handler + Looper for communication between Threads
- One thread can create one Looper to manage its Message Queue(FIFO)
- UI Thread is Main Thread, Android automatically creates a Message Queue
- Looper: Message exchange between Threads
- Handler: Push/receive Message into/from Looper(Message Queue)
