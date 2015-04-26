Title: Introducing the core devs of pgcli
Date: 2015-04-26
Category: Blog
Tags: python 
Slug: core-1

It is my pleasure to announce the core devs of the pgcli project. 

# [Daniel Rocco](https://github.com/drocco007)

Daniel made pgcli handle JSON, bytea, and large decimal values correctly. He improved the completion matching by adding sub-string matching. His creative solution to reducing completion noise is extremely useful. He also added numerous tests to cover a lot more branches in the code path. 

# [Darik Gamble](https://github.com/darikg)

Darik is a prolific committer who is credited for numerous feature additions in pgcli. He single handedly made pgcli [embeddable inside IPython]({filename}embedding-pgcli-in-ipython.md), which still blows my mind. He made pgcli behave more like psql, added schema support to completion (this is huge), view name completion, auto-escaping of tables/columns and numerous special command (`\dv, \df, \dn`). Darik's feature additions are creative and well-thought out.

# [Iryna Cherniavska](https://github.com/j-bennet)

Iryna is one of the earliest contributors to the project. She is credited for adding a rich set of tests to the completion engine and brought in mocks to test some of the tricky bits. She also added many of the special commands such as `\dv, \di, \e` and contributed to the [developer document](https://github.com/dbcli/pgcli/blob/master/DEVELOP.rst#adding-postgresql-special-meta-commands).

# [Karl-Aksel Puulmann](https://github.com/macobo)

Karl fixed some of the critical issues early on in the project, which paved the way to get this project widely accepted. Karl made pgcli handle unicode. He created robust testing fixtures to make it easy for contributors to add tests. Thanks to Karl, it is now possible to cancel queries that are in flight using Ctrl-C.

He also created an experimental [SQL completion engine](https://github.com/macobo/sqlcomplete) that can provide accurate suggestions based on actual grammar instead of the heuristics. It is still in the experimental phase and we hope to use it in pgcli in the future.

# Thanks

I'm extremely grateful to all of the core devs for their contributions so far and their willingness to play the role of core dev in the project. I'm quite lucky to be working with such amazing devs.
