(* 1 *)
fun il2rl lst = map real lst;

(* 2 *)
fun ordList (lst:char list) = map (fn x => ord x) lst;

(* 3 *)
fun squareList lst = map (fn x => x*x) lst;

(* 4 *)
fun multPairs lst = map (fn (a,b) => a*b) lst;

(* 5 *)
fun incList lst = fn y => map (fn x => x+y) lst;

(* 6 *)
fun sqSum lst = foldl (fn (x, a) => a + x * x) 0 lst;

(* 7 *)
fun bor lst = foldl (fn (x, y) => (x orelse y)) false lst;

(* 8 *)
fun band lst = foldl (fn (x, y) => (x andalso y)) true lst;

(* 9 *)
fun bxor lst = foldl (fn (x, y) => (x <> y)) false lst;

(* 10 *)
fun dupList lst = foldl (fn (x, a) => x::x::a) [] lst;

(* 11 *)
fun myLength lst = foldl (fn (x,a) => a+1) 0 lst;

(* 12 *)
fun il2absrl lst = il2rl(map (fn x => if x < 0 then ~x else x) lst)

(* 13 *)
fun trueCount lst = foldl (fn (x,a) => if x = true then a+1 else a) 0 lst;