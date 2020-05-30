(defun fact(n)
	(setq f 1)
	(loop for x from 1 to n
		do(setq f (* f x)))
	(write f))

(princ "Enter Number : ")
(setq n (read))
(fact n)

