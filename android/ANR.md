# ANR

Cause:
- App can not response for user inputs in 5 seconds
- BroadcastReceiver cannot finished within 10 seconds
- Service cannot finished within 20 seconds

Solution:
- Don't stuck MainThread, don't do timeconsuming in onCreate() and onResume()
- Don't do timeconsuming task in BroadcastReceiver
- Don't do timeconsuming task in Service