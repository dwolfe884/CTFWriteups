## Description:
The extraterrestrials have upgraded their authentication system and now only them are able to pass. Did you manage to learn their language well enough in order to bypass the the authorization check?

This challenges has us placed in a python jail where we can provide very liminted input. Providing malformed input can get us a useful error message that gives us a little insight into what exactly this jail is doing.
```
File "/app/build_yourself_in.py", line 13, in main
    exec(text, {'__builtins__': None, 'print':print})
```
By using ().__class__.__bases__[0] you're able to access the object class in python. Object has an attribute called __subclasses__() which returns a list of all classes that have been used up to that point in the program. From here you can access individual classes with [n]. Interesting classes are 'str' at index 22 and os_wrap_close at 132. os_wrap_close.__init__.__globals__ returns a dict with all os functions including system. running system(ls) would get us all files. To do this we need a string... but we can't use any quotes. This is where the str function comes into play. We have access to that class at [22] and if we pass a dict object to the str function we can get a long string that can be indexed with numbers. Using ().__class__.__bases__[0].__subclasses__()[22](().__class__.__bases__[0].__subclasses__()[132].__init__.__globals__)[5] passes the giant dict of os functions to str function and gets the 5th character out of it which is an 'a'. By counting characters in that string and using '+' to concatinate several of these str() calls we can build a string for system and ls. Putting these long string builders into the original __globals__[system](ls) we run ls and see flag.txt. Then it's just a process of building 'cat flag.txt' and passing that in instead of ls