# ANR

Cause:
- App can not response for user inputs in 5 seconds
    - Don't do timeconsuming in `onCreate()` and `onResume()`
- BroadcastReceiver cannot finished within 10 seconds
- Service cannot finished within 20 seconds
