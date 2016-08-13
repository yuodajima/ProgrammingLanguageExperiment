(define diff 
  (lambda (shiki)
    (cond ((not (pair? shiki)) (if (number? shiki) 0 1))
          ((equal? (car shiki) '+) `(+ ,@(map diff (cdr shiki))))
          ((equal? (car shiki) '-) `(- ,@(map diff (cdr shiki))))
          ((equal? (car shiki) '*) `(+ (* ,(cadr shiki) ,(diff (caddr shiki))) (* ,(diff (cadr shiki)) ,(caddr shiki))))
          ((equal? (car shiki) '**) `(* ,(caddr shiki) (* ,(diff (cadr shiki)) (** ,(cadr shiki) ,(- (caddr shiki) 1)))))
          )))

(diff 1)
(diff 'x)
(diff '(+ x 5))
(diff '(+ (+ (** x 2) (* 4 x)) 3)) 



(define fx '(+ (+ (** x 2) (* 4 x)) 3))
(define ** expt)

(define tangent
  (lambda (fx x)
    `(+ (* ,((eval `(lambda (x) ,(diff fx)) (interaction-environment)) x) x) ,(- ((eval `(lambda(x) ,fx) (interaction-environment)) x) (* ((eval `(lambda (x) ,(diff fx)) (interaction-environment)) x) x))
        )))

(tangent fx 0)
