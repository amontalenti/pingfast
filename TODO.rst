TODO
====
* currently, `pingdom_sync` doesn't enable contact notifications for checks that it synchronizes; there is probably
  a way to do this with the API but we couldn't find it
* the checks are created in a random order in the secondary account; would be useful if they were in same order as
  primary account
* some checks don't need to be fast, they just need to be up; we should support "ignores" for some check_ids
