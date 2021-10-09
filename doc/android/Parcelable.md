# Parcelable

- Serializable from Java
    - Reflection is used during the process and lots of additional objects are created along the way.
    - Not efficient during R/W in hard drive, lots temporary var created, lots i/o operations
- Parcelable from Android
    - Parcelable was specifically designed in such a way that there is no reflection when using it.
    - Efficient (more than 10x faster), but it cannot be saved into hard drive


