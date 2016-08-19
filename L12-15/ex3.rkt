;その1

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

;実行結果
;0
;1
;(+ 1 0)
;(+ (+ (* 2 (* 1 (** x 1))) (+ (* 4 1) (* 0 x))) 0)

;その2

(define fx '(+ (+ (** x 2) (* 4 x)) 3))
(define ** expt)

(define tangent
  (lambda (fx x)
    `(+ (* ,((eval `(lambda (x) ,(diff fx)) (interaction-environment)) x) x) ,(- ((eval `(lambda(x) ,fx) (interaction-environment)) x) (* ((eval `(lambda (x) ,(diff fx)) (interaction-environment)) x) x))
        )))

(tangent fx 0)
(tangent fx 4)

;実行結果
;(+ (* 4 x) 3)
;(+ (* 12 x) -13)

;その3

(define simple+
  (lambda (p q)
    (cond ((equal? q 0) p)
          ((equal? p 0) q)
          (else `(+ ,p ,q))
          )))

(define simple-
  (lambda (p q)
    (cond ((equal? q 0) p)
          ((equal? p 0) (- q))
          (else `(- ,p ,q))
          )))

(define simple*
  (lambda (p q)
    (cond ((or (equal? p 0) (equal? q 0)) 0)
          ((equal? q 1) p)
          ((equal? p 1) q)
          (else `(* ,p ,q))
          )))

(define simple**
  (lambda (p q)
    (cond ((equal? q 0) 1)
          ((equal? q 1) p)
          (else `(** ,p ,q))
          )))

(define simple
  (lambda (formula)
    (cond ((null? formula) `())
          ((pair? formula)
           (cond ((equal? (car formula) `+) (simple+ (simple (cadr formula)) (simple (caddr formula))))
                 ((equal? (car formula) `-) (simple- (simple (cadr formula)) (simple (caddr formula))))
                 ((equal? (car formula) `*) (simple* (simple (cadr formula)) (simple (caddr formula))))
                 ((equal? (car formula) `**) (simple** (simple (cadr formula)) (simple (caddr formula))))
                 ))
          ((or (symbol? formula) (number? formula)) formula)
          )))

`(+ 8 (* 0 x))
(simple `(+ 8 (* 0 x)))

(diff '(+ (+ (** x 2) (* 4 x)) 5))
(simple (diff '(+ (+ (** x 2) (* 4 x)) 5))) 

;実行結果
;(+ 8 (* 0 x))
;8
;(+ (+ (* 2 (* 1 (** x 1))) (+ (* 4 1) (* 0 x))) 0)
;(+ (* 2 x) 4)

;その4

(define diff2
   (lambda (formula)
    `(+ ,@(map diff (cdr formula)))
          ))

(define remove
  (lambda (predicate list)
    (cond ((null? list) '())
          ((predicate (car list)) (remove predicate (cdr list)))
          (else (cons (car list) (remove predicate (cdr list))))
          )))

(define simple2
 (lambda (formula)
    (cond ((equal? (car formula) `+)
           (map simple (remove (lambda(val) (equal? val 0)) formula))))
   )
          )

    

(define fx4 `(+ 1 (* 3 x) (* 2 (** x 2)) (* 5 (** x 3)) (* 2 (** x 4))))
(diff2 fx4)
(simple2 (diff2 fx4))

;実行結果
;(+
; 0
; (+ (* 3 1) (* 0 x))
; (+ (* 2 (* 2 (* 1 (** x 1)))) (* 0 (** x 2)))
; (+ (* 5 (* 3 (* 1 (** x 2)))) (* 0 (** x 3)))
; (+ (* 2 (* 4 (* 1 (** x 3)))) (* 0 (** x 4)))
;)
;(+ 3 (* 2 (* 2 x)) (* 5 (* 3 (** x 2))) (* 2 (* 4 (** x 3))))

