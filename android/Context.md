# Context

- Context is a abstruct class.
- Context size = Activity size + Service size + 1(Application)
- Context in Activity, Service, Application are different
    - Most of time, they can shared
    - Activity needs theme
    - Activity Context starts Activity, Dialog (except System Dialog)
    - `getApplicationContext()` and `getApplication()` returns same object but different type
