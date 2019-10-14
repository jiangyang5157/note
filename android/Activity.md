# Activity

## LaunchMode
- Standard
    - Default mode
    - Activity will create a new instance and put it into the top of current Stack.

- SingleTop
    - Resuse instance by invoke `onNewIntent()` if the Activity is exists and it's in the top of the Stack.
        - Eg: news, reads page

- SingleTask
    - Resuse instance by invoke `onNewIntent()` if the Activity is exists in the Stack. It will removed all other Activity(s) that was on top of it.
        - Eg: browser main page

- SingleInstance
    - Activity will create a new instance and put it into a new Stack, and the instance can be shared by other App (`onNewIntent()` will be invoked).
        - Eg: treat as "App", alert, reminder app


## Exit all active Activity(s)
- Solution 1
    - API 16+: finishAffinity()
- Solution 2
    - SingleTop Activity as an entrance, and `intent.setFlags(Intent.FLAG_ACTIVITY_CLEAR_TOP)`, then destroy the Activity.
- Solution 3
    - SingleTask Activity as an entrance, all of Activity(s) above it will be destroyed, then destroy the Activity.