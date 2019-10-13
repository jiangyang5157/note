# Cache

- Local cache
    - File
    - Database
    - Sharedpreferences
- Memory cache
- Network source
    - After downloaded, cache it into Local and Memory

Process:
- Load data from local cache into memory cache
    - If local data not exists
        - Download from network source, then cache it into local cache and memory cache
    - If local data "expired"
        - Download from network source, then cache it into local cache and memory cache
- Get data from memory
    - If memory data not exists
        - Get data from local, then cache is into memory
    - If memory data and local data not exists
        - Download from network source, then cache it into local cache and memory cache



Decription:
- ViewModel: Lifecycle.Transformations
Encription
- Repository: NetworkBoundResource