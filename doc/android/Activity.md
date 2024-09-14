# Activity

## LaunchMode
- Standard (default)
    - Create a new instance and put it into the top of current Stack.

- SingleTop
    - Resuse instance by invoke `onNewIntent()` if the Activity is exists and it's in the top of the Stack.
        - Eg: news, reads page

- SingleTask
    - Resuse instance by invoke `onNewIntent()` if the Activity is exists in the Stack. 
    - It will removed all other Activity(s) that was on top of it.
        - Eg: browser main page

- SingleInstance
    - Create a new instance and put it into a new Stack, `onNewIntent()` will be invoked.
    - The instance can be shared by other App
        - Eg: treat as "App", alert, reminder app


## Exit all active Activity(s)
- Solution 1
    - finishAffinity()
    - API 16+
- Solution 2
    - SingleTop Activity as an entrance with flag `Intent.FLAG_ACTIVITY_CLEAR_TOP`
    - Then destroy the Activity.
- Solution 3
    - SingleTask Activity as an entrance, all of Activity(s) above it will be destroyed
    - Then destroy the Activity.
