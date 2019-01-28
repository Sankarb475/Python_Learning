'''to run python in command prompt, use "python", (windows :considering you have set up environment variable)
The interactive prompt runs code and echoes results as you go, but it doesn’t save your code in a file
'''

#to get current working directory
>>> import os
>>> os.getcwd()
'/Users/sankar.biswas'

#changing current direcctory 
>>> os.chdir('/Users/sankar.biswas/Desktop/Python/coding')
>>> os.getcwd()
'/Users/sankar.biswas/Desktop/Python/coding'

# to run a python script from command prompt
python file1.py

#saving the output in a file 
python script1.py > saveit.txt

# "dir" - you can use it to fetch a list of all the names available inside a module
>>> import sys
>>> dir(sys)
['__breakpointhook__', '__displayhook__', '__doc__', '__excepthook__', '__interactivehook__', '__loader__', '__name__', '__package__', '__spec__', '__stderr__', 
 '__stdin__', '__stdout__', '_clear_type_cache', '_current_frames', '_debugmallocstats', '_framework', '_getframe', '_git', 
 '_home', '_xoptions', 'abiflags', 'api_version', 'argv', 'base_exec_prefix', 'base_prefix', 'breakpointhook', 'builtin_module_names', 
 'byteorder', 'call_tracing', 'callstats', 'copyright', 'displayhook', 'dont_write_bytecode', 'exc_info', 'excepthook', 'exec_prefix', 'executable', 'exit', 
 'flags', 'float_info', 'float_repr_style', 'get_asyncgen_hooks', 'get_coroutine_origin_tracking_depth', 'get_coroutine_wrapper', 
 'getallocatedblocks', 'getcheckinterval', 'getdefaultencoding', 'getdlopenflags', 'getfilesystemencodeerrors', 'getfilesystemencoding', 
 'getprofile', 'getrecursionlimit', 'getrefcount', 'getsizeof', 'getswitchinterval', 'gettrace', 'hash_info', 'hexversion', 'implementation', 'int_info', 'intern', 'is_finalizing', 'maxsize', 'maxunicode', 
 'meta_path', 'modules', 'path', 'path_hooks', 'path_importer_cache', 'platform', 'prefix', 'ps1', 'ps2', 'set_asyncgen_hooks', 
 'set_coroutine_origin_tracking_depth', 'set_coroutine_wrapper', 'setcheckinterval', 'setdlopenflags', 'setprofile', 'setrecursionlimit', 
 'setswitchinterval', 'settrace', 'stderr', 'stdin', 'stdout', 'thread_info', 'version', 'version_info', 'warnoptions']

 # the " exec(open('module.py').read())" built-in function call is another way to launch files from the interactive prompt without having to import and later reload

 #you can also find out the functions you can apply on a variable using "dir"
 >>> a = 234
>>> dir(a)
['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', 
 '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__gt__', 
 '__hash__', '__index__', '__init__', '__init_subclass__', '__int__', '__invert__', '__le__', '__lshift__', '__lt__', '__mod__'
 , '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', 
 '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', 
 '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', 
 '__trunc__', '__xor__', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'numerator', 'real', 'to_bytes']

# this will help you get a knowledge on the functionality of the function, dial 'q' to escape
>>> help(a.__abs__)

# Pattern Matching
>>> match = re.match('Hello[ \t]*(.*)world', 'Hello Python world')
>>> match
<re.Match object; span=(0, 18), match='Hello Python world'>
>>> match.group(1)
'Python '

>>> match = re.match('[/:](.*)[/:](.*)[/:](.*)', '/usr/home:lumberjack') 
>>> match.groups()
('usr', 'home', 'lumberjack')
>>> re.split('[/:]', '/usr/home/lumberjack') 
['', 'usr', 'home', 'lumberjack']








