# Fragment State

- If we `replace()` or `remove()` a Fragment and don’t add the transaction to the backstack you run the risk of losing your Fragment’s state.

- `FragmentStatePagerAdapter`

- `FragmentManager.saveInstanceState(Fragment)`

- `Fragment.setInitialSavedState(Bundle)`
