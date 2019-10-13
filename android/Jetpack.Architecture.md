# Jetpack Architecture

- Android/Fragment
    - ViewModel #LiveData(s)
        - Repository
            - Model #Room
                - SQLite
            - Remote Data Source
                - Retrofit
                    - Webservice

    :
    - Separation Of Concerns
        - Stable
        - Testable
    - Reactive
    - Single Source Of Truth

- Room

- ViewModel

- ViewModelFactory
    - Dagger2 Multibindings: Map<Key, Provider<Value>>
        - Key: ViewModel class
        - Value: ViewModel

- Repository
    - Take harvy data request logic from ViewModel

- LiveData
    - Immutable
    - `onActive()` called when there is any observer
    - `onInactive` called when there is no observer
    - Stick

- MutableLiveData
    - Mutable

- MediatorLiveData
    - LiveData subclass which may observe other LiveData objects and react on OnChanged events from them

- SingleLiveEvent
    - A lifecycle-aware observable that sends only new updates after subscription(explicit call to `setValue()`/`call()`), used for events like navigation and Snackbar messages.
    - Only one observer is going to be notified of changes.
        - Solution: Use an Event wrapper instead of SingleLiveEvent
    - Avoid harvy Activity <--Intent--> Fragment 

- Usually:
    - ViewModel use MutableLiveData, but it exposes the immutable LiveData.
    - Observe in `onCreate()`, bind LifecycleOwner.

- Lifecycle.Transformations
    - `static <X, Y> LiveData<Y> map(LiveData<X> source, final Function<X, Y> func)`
    - `static <X, Y> LiveData<Y> switchMap(LiveData<X> source, final Function<X, LiveData<Y>> func)`

- Navigation

- WorkManager
    - Long-running HTTP downloads?
        - YES: DownloadManager
        - NO: Deferrable?
            - NO: Foreground service
            - YES: Triggered by system condition?
                - YES: WorkManager
                - NO: Run at precise time?
                    - YES: AlarmManager
                    - NO: WorkManager
