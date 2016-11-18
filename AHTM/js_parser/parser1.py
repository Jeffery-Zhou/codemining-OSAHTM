from slimit import minify
text = """
 var a = function( obj ) {
         for ( var name in obj ) {
                 return false;
         }
         return true;
 };
"""
print minify(text, mangle=True, mangle_toplevel=True)