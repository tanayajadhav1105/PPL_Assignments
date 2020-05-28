(defun fact(n)
 (if(= n 0) 1
  (* n (fact(- n 1)))))
(princ "Enter Number : ")
(setq n (read))
(setq k (fact n))
(write k)

