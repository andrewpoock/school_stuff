(* 15 *)
fun myimplode lst = foldl (fn (x,s) => s ^ str(x)) "" lst;

(* 17 *)
fun max lst = foldl (fn (x,a) => if x > a then x else a) 0 lst;

(* 19 *)
fun member (item, lst) = foldl (fn (x,a) => if x = item then true else a) false lst;

(* 21 *)
fun less (n, lst) = foldr (fn (x,a) => if x < n then x::a else a) [] lst;

(* 23 *)
fun convert lst = foldr (fn ((x,y),(a,b)) => (x::a, y::b)) ([],[]) lst;

(* 25 *)
fun eval lst n:real = foldr (fn (x,a) => n*a+x) 0.0 lst;

(* 27 *)
fun myfoldr f a [] = a
    | myfoldr f a (x::xs) = f (x, foldr f a xs);