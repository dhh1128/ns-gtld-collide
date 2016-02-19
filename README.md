# ns-gtld-collide
Find collisions between namespaces in programming languages and global TLDs.
See http://j.mp/20J7HHp -- or view [our RSA 2016 talk](http://j.mp/1Qp32ei) --
for details about why these collisions are a security issue.

## usage
```
python collide.py tlds.txt classes.txt
```
  Given a list of gTLDs and a list of classes (points in the hierarchical
  namespace(s) of a programming ecosystem), report collisions. Both lists
  should be simple text files with one item per line, and comparison is not
  case-sensitive.
  
## sample files
tlds.txt is provided; you may want to refresh it if its last mod date is not recent.
Sample package/class hierarchies for java are also provided, although these only
include items from the standard JRE. These lists were essentially copy/pasted from
oracle docs; see http://j.mp/1XC3pBL for an example.

I couldn't find an easy way to generate an analogous list for the .NET framework,
but I would welcome contributions of that data -- or similar data for python,
ruby, and other programming ecosystems.

You might want to add company-specific libraries and classes to the list and see
what additional collisions are detected...
