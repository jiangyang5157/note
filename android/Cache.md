# Cache

- Local cache / Data Persistence
    - Hard drive
    - Sharedpreferences
    - Database / SQLite
    - ContentProvider
        - Implemented by SQLite, expose Uri
        - Shared/Open data to other applications
- Memory cache
- Network source

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


Decryption:
- ViewModel: Lifecycle.Transformations.switchMap() / map()
Encription
- Repository: eg: NetworkBoundResource
